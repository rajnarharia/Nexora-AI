# utils/ui_helpers.py
import streamlit as st

SUGGESTIONS = [
    "Explain Machine Learning in simple terms",
    "Help me write a Python script for web scraping",
    "Summarize the main principles of clean code",
    "Brainstorm 5 project ideas for my portfolio"
]

def display_suggestion_cards():
    """Displays suggestion cards in a grid and returns the clicked suggestion."""
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    clicked_suggestion = None
    
    with col1:
        if st.button("💡 Explain a complex topic", use_container_width=True, help=SUGGESTIONS[0]):
            clicked_suggestion = SUGGESTIONS[0]
        if st.button("📝 Help me write code", use_container_width=True, help=SUGGESTIONS[1]):
            clicked_suggestion = SUGGESTIONS[1]
            
    with col2:
        if st.button("📚 Summarize something", use_container_width=True, help=SUGGESTIONS[2]):
            clicked_suggestion = SUGGESTIONS[2]
        if st.button("🚀 Brainstorm project ideas", use_container_width=True, help=SUGGESTIONS[3]):
            clicked_suggestion = SUGGESTIONS[3]
            
    return clicked_suggestion

def display_chat_stats(messages):
    """Displays chat statistics in the sidebar."""
    if not messages:
        st.sidebar.info("No messages yet.")
        return
        
    user_count = sum(1 for msg in messages if msg["role"] == "user")
    ai_count = sum(1 for msg in messages if msg["role"] == "assistant")
    total_count = len(messages)
    
    st.sidebar.markdown("### 📊 Session Stats")
    col1, col2, col3 = st.sidebar.columns(3)
    col1.metric("User", user_count)
    col2.metric("AI", ai_count)
    col3.metric("Total", total_count)
