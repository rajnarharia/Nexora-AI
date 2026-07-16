import os
from dotenv import load_dotenv

# Load environment variables before anything else
load_dotenv()

import streamlit as st
import config
from services import ai_service
from utils import ui_helpers, export

# ------------------ App Config ------------------
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom CSS
st.markdown(config.CUSTOM_CSS, unsafe_allow_html=True)

# ------------------ Initialization ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "follow_up_suggestions" not in st.session_state:
    st.session_state.follow_up_suggestions = []
    
if "trigger_prompt" not in st.session_state:
    st.session_state.trigger_prompt = None

# Initialize Groq Client
client = ai_service.get_groq_client()

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("✨ " + config.APP_NAME)
    st.caption(config.APP_TAGLINE)
    
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.follow_up_suggestions = []
        st.rerun()
        
    st.divider()
    
    st.subheader("⚙️ Settings")
    persona = st.selectbox("AI Mode", options=list(config.PERSONAS.keys()))
    length = st.select_slider("Response Length", options=list(config.LENGTH_MODIFIERS.keys()), value="Medium")
    tone = st.select_slider("Response Tone", options=list(config.TONE_MODIFIERS.keys()), value="Professional")
    
    enhance_prompt = st.toggle("✨ Enhance Prompt (Beta)", help="Automatically improves your prompt for better results before sending.")
    
    st.divider()
    ui_helpers.display_chat_stats(st.session_state.messages)
    
    st.divider()
    st.subheader("💾 Export Chat")
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.messages:
            txt_data = export.export_chat_to_text(st.session_state.messages)
            st.download_button("TXT", data=txt_data, file_name="novamind_chat.txt", mime="text/plain", use_container_width=True)
        else:
            st.button("TXT", disabled=True, use_container_width=True)
    with col2:
        if st.session_state.messages:
            md_data = export.export_chat_to_markdown(st.session_state.messages)
            st.download_button("MD", data=md_data, file_name="novamind_chat.md", mime="text/markdown", use_container_width=True)
        else:
            st.button("MD", disabled=True, use_container_width=True)


# ------------------ Main UI ------------------
if not st.session_state.messages:
    # Welcome Screen
    st.markdown("<div class='title-wrapper'>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='main-title'>Welcome to {config.APP_NAME} 👋</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='tagline'>How can I help you today?</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Suggestion Cards
    clicked = ui_helpers.display_suggestion_cards()
    if clicked:
        st.session_state.trigger_prompt = clicked
        st.rerun()

else:
    # Chat Interface
    # Optional: Search
    search_query = st.sidebar.text_input("🔍 Search Chat", "")
    
    for idx, message in enumerate(st.session_state.messages):
        # Apply search filter if active
        if search_query and search_query.lower() not in message["content"].lower():
            continue
            
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Action buttons for AI responses (last message or any)
            if message["role"] == "assistant":
                # We use simple copy placeholders or columns since full JS clipboard is complex in standard Streamlit
                pass

# ------------------ Chat Input & Logic ------------------

# Check if a suggestion card triggered a prompt
prompt = st.chat_input("Type your message here...")

if st.session_state.trigger_prompt:
    prompt = st.session_state.trigger_prompt
    st.session_state.trigger_prompt = None

if prompt:
    if not client:
        st.error("⚠️ API Key is missing. Please check your .env file.")
    else:
        # 1. Clear old follow-ups
        st.session_state.follow_up_suggestions = []
        
        # 2. Optionally Enhance Prompt
        actual_prompt = prompt
        if enhance_prompt:
            with st.spinner("✨ Enhancing prompt..."):
                actual_prompt = ai_service.enhance_prompt_internally(client, prompt)
                
        # 3. Add user message to state and display
        st.session_state.messages.append({"role": "user", "content": prompt})
        if not st.session_state.trigger_prompt: # If it's a trigger, UI will re-render anyway, but let's draw it if manual
            with st.chat_message("user"):
                st.markdown(prompt)
                if enhance_prompt and actual_prompt != prompt:
                    st.caption(f"*Enhanced to:* {actual_prompt}")

        # 4. Generate AI Response
        with st.chat_message("assistant"):
            try:
                # We pass the history but we must use the actual_prompt for the latest user message
                messages_for_api = st.session_state.messages[:-1] + [{"role": "user", "content": actual_prompt}]
                
                stream = ai_service.get_chat_completion_stream(
                    client=client,
                    messages=messages_for_api,
                    persona=persona,
                    length=length,
                    tone=tone
                )
                
                response_content = st.write_stream(stream)
                
                # Append to session state
                st.session_state.messages.append({"role": "assistant", "content": response_content})
                
                # Generate Follow-ups silently
                st.session_state.follow_up_suggestions = ai_service.generate_follow_up_questions(
                    client, st.session_state.messages, response_content
                )
                
            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")

# ------------------ Follow-up Suggestions UI ------------------
if st.session_state.follow_up_suggestions:
    st.markdown("<div style='margin-top: 1rem;'><small><b>Suggested follow-ups:</b></small></div>", unsafe_allow_html=True)
    cols = st.columns(len(st.session_state.follow_up_suggestions))
    for i, suggestion in enumerate(st.session_state.follow_up_suggestions):
        with cols[i]:
            if st.button(suggestion, key=f"su_{i}", use_container_width=True):
                st.session_state.trigger_prompt = suggestion
                st.rerun()