import os
import time
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
    page_icon="🌌",
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
    st.title(f"🌌 {config.APP_NAME}")
    st.caption(config.APP_TAGLINE)
    
    # 1. Primary Action
    if st.button("✨ Initialize New Core", use_container_width=True, type="primary"):
        st.session_state.messages = []
        st.session_state.follow_up_suggestions = []
        st.rerun()
        
    st.divider()
    
    # 2. Search Chat (Always fixed at top of sidebar)
    search_query = st.text_input("🔍 Search Memory", placeholder="Find past messages...", help="Filters the chat history in real-time.")
    
    st.divider()
    
    # 3. AI Core Settings
    with st.expander("⚙️ Core Settings", expanded=True):
        selected_model_name = st.selectbox("LLM Engine", options=list(config.MODELS.keys()))
        selected_model = config.MODELS[selected_model_name]
        persona = st.selectbox("AI Persona", options=list(config.PERSONAS.keys()))
    
    # 4. Output Tuning
    with st.expander("🎛️ Output Tuning", expanded=False):
        length = st.select_slider("Length", options=list(config.LENGTH_MODIFIERS.keys()), value="Medium")
        tone = st.select_slider("Tone", options=list(config.TONE_MODIFIERS.keys()), value="Professional")
        context_window = st.slider("Max Tokens", min_value=256, max_value=8192, value=2048, step=256)
    
    # 5. Tools & Plugins
    with st.expander("🔌 Tools & Plugins", expanded=False):
        enhance_prompt = st.toggle("✨ Prompt Enhancer", help="Automatically optimizes prompt.", value=True)
        web_search = st.toggle("🌐 Web Search (Mock)", help="Simulates internet access.")
        data_upload = st.file_uploader("📂 Upload Dataset", type=["csv", "txt", "pdf"])
    
    st.divider()
    
    # 6. Analytics
    ui_helpers.display_chat_stats(st.session_state.messages)
    
    st.divider()
    
    # 7. Export
    st.subheader("💾 Export Chat")
    col1, col2 = st.columns(2)
    with col1:
        txt_disabled = len(st.session_state.messages) == 0
        if not txt_disabled:
            txt_data = export.export_chat_to_text(st.session_state.messages, app_name=config.APP_NAME)
            st.download_button("TXT", data=txt_data, file_name="nexora_session.txt", mime="text/plain", use_container_width=True)
        else:
            st.button("TXT", disabled=True, use_container_width=True)
    with col2:
        if not txt_disabled:
            md_data = export.export_chat_to_markdown(st.session_state.messages, app_name=config.APP_NAME)
            st.download_button("MD", data=md_data, file_name="nexora_session.md", mime="text/markdown", use_container_width=True)
        else:
            st.button("MD", disabled=True, use_container_width=True)


# ------------------ Main UI ------------------
if not st.session_state.messages:
    # Welcome Screen
    st.markdown("<div class='title-wrapper'>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='main-title'>Welcome to {config.APP_NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='tagline'>INITIALIZING {selected_model_name.upper()} CORE...</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Suggestion Cards
    clicked = ui_helpers.display_suggestion_cards()
    if clicked:
        st.session_state.trigger_prompt = clicked
        st.rerun()

else:
    # Chat Interface - Clean and sequential
    for idx, message in enumerate(st.session_state.messages):
        # Apply search filter if active
        if search_query and search_query.lower() not in message["content"].lower():
            continue
            
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ------------------ Chat Input & Logic ------------------

prompt = st.chat_input("Communicate with Nexora AI...")

if st.session_state.trigger_prompt:
    prompt = st.session_state.trigger_prompt
    st.session_state.trigger_prompt = None

if prompt:
    if not client:
        st.error("⚠️ System Failure: Groq API Key is missing. Please check your .env configuration.")
    else:
        st.session_state.follow_up_suggestions = []
        actual_prompt = prompt
        
        # Add file context if uploaded (Mock)
        if data_upload:
            actual_prompt = f"[Context: User uploaded {data_upload.name}]\n" + actual_prompt
            
        # Simulate web search
        if web_search:
            with st.spinner("🌐 Accessing the web..."):
                time.sleep(1)
                actual_prompt = f"[Web Context Retrieved]\n" + actual_prompt
        
        if enhance_prompt:
            with st.spinner("✨ Optimizing neural prompt..."):
                actual_prompt = ai_service.enhance_prompt_internally(client, actual_prompt, model=selected_model)
                
        # Append User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        if not st.session_state.trigger_prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
                if enhance_prompt and actual_prompt != prompt:
                    st.caption("*(Optimized prompt)*")

        # Generate Assistant Response
        with st.chat_message("assistant"):
            try:
                messages_for_api = st.session_state.messages[:-1] + [{"role": "user", "content": actual_prompt}]
                
                stream = ai_service.get_chat_completion_stream(
                    client=client,
                    messages=messages_for_api,
                    persona=persona,
                    length=length,
                    tone=tone,
                    model=selected_model,
                    context_window=context_window
                )
                
                response_content = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response_content})
                
                # Removed mock copy/reroll buttons to keep chat bubbles clean and continuous
                
                # Generate Follow-ups silently
                st.session_state.follow_up_suggestions = ai_service.generate_follow_up_questions(
                    client, st.session_state.messages, response_content, model=selected_model
                )
                
            except Exception as e:
                st.error(f"⚠️ Neural network overload: {str(e)}")

# ------------------ Follow-up Suggestions UI ------------------
if st.session_state.follow_up_suggestions:
    st.markdown("<div style='margin-top: 1rem;'><small style='color: #00F0FF;'><b>Suggested logic paths:</b></small></div>", unsafe_allow_html=True)
    cols = st.columns(len(st.session_state.follow_up_suggestions))
    for i, suggestion in enumerate(st.session_state.follow_up_suggestions):
        with cols[i]:
            if st.button(suggestion, key=f"su_{i}", use_container_width=True):
                st.session_state.trigger_prompt = suggestion
                st.rerun()