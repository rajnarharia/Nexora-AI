# utils/ui_helpers.py
import streamlit as st

SUGGESTIONS = [
    "Analyze a complex data trend",
    "Architect a scalable web application",
    "Explain Quantum Computing principles",
    "Draft a high-converting marketing copy"
]

def display_suggestion_cards():
    """Displays highly designed suggestion cards in a grid and returns the clicked suggestion."""
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    clicked_suggestion = None
    
    with col1:
        if st.button("📊 Analyze a data trend", use_container_width=True, help=SUGGESTIONS[0]):
            clicked_suggestion = SUGGESTIONS[0]
        if st.button("💻 Architect an app", use_container_width=True, help=SUGGESTIONS[1]):
            clicked_suggestion = SUGGESTIONS[1]
            
    with col2:
        if st.button("⚛️ Explain Quantum Computing", use_container_width=True, help=SUGGESTIONS[2]):
            clicked_suggestion = SUGGESTIONS[2]
        if st.button("✍️ Draft marketing copy", use_container_width=True, help=SUGGESTIONS[3]):
            clicked_suggestion = SUGGESTIONS[3]
            
    return clicked_suggestion

def display_chat_stats(messages):
    """Displays chat statistics in the sidebar."""
    if not messages:
        st.sidebar.info("Awaiting input...")
        return
        
    user_count = sum(1 for msg in messages if msg["role"] == "user")
    ai_count = sum(1 for msg in messages if msg["role"] == "assistant")
    total_count = len(messages)
    
    # Estimate tokens roughly (1 token ~ 4 chars)
    total_chars = sum(len(msg["content"]) for msg in messages)
    est_tokens = total_chars // 4
    
    st.sidebar.markdown("### 📈 Analytics")
    col1, col2, col3 = st.sidebar.columns(3)
    col1.metric("User", user_count)
    col2.metric("Nexora", ai_count)
    col3.metric("Tokens", f"~{est_tokens}")
