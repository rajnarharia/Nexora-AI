# config.py
import streamlit as st

APP_NAME = "NovaMind AI"
APP_TAGLINE = "Your Intelligent AI Workspace"

# Premium Dark Theme CSS
CUSTOM_CSS = """
<style>
    /* Global Styles */
    :root {
        --bg-color: #0E1117;
        --secondary-bg: #1E2129;
        --text-color: #E0E6ED;
        --accent-color: #6C5CE7;
        --accent-hover: #8172F2;
        --user-bubble: #2D3748;
        --ai-bubble: #1A202C;
    }
    
    body {
        color: var(--text-color);
        background-color: var(--bg-color);
    }
    
    /* Headers & Tagline */
    .title-wrapper {
        text-align: center;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    
    .main-title {
        font-weight: 800;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #6C5CE7, #00D2D3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    .tagline {
        font-size: 1rem;
        color: #A0AEC0;
        font-weight: 400;
        letter-spacing: 0.5px;
        margin-top: 0;
    }

    /* Suggestion Cards */
    .suggestion-card {
        background-color: var(--secondary-bg);
        border: 1px solid #2D3748;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }
    
    .suggestion-card:hover {
        background-color: #2D3748;
        border-color: var(--accent-color);
        transform: translateY(-2px);
    }
    
    .suggestion-text {
        font-size: 0.95rem;
        color: var(--text-color);
        font-weight: 500;
    }
    
    /* Code Blocks */
    pre {
        background-color: #12151C !important;
        border-radius: 8px !important;
        border: 1px solid #2D3748 !important;
    }
    
    /* Adjust Streamlit specific containers */
    .stChatInputContainer {
        border-radius: 16px !important;
        border: 1px solid #2D3748 !important;
        background-color: var(--secondary-bg) !important;
    }
</style>
"""

# AI Personas
PERSONAS = {
    "General Assistant": "You are NovaMind AI, a highly capable, helpful, and professional AI assistant. You provide clear, accurate, and concise answers.",
    "Coding Expert": "You are NovaMind AI, a senior software engineer and coding expert. You write clean, efficient, and well-documented code. Always wrap code in Markdown blocks and explain the logic clearly.",
    "Study Tutor": "You are NovaMind AI, a patient and knowledgeable tutor. Break down complex topics into easily understandable pieces, use analogies, and encourage the user to think critically.",
    "Research Assistant": "You are NovaMind AI, an academic research assistant. Provide well-structured, objective, and analytical answers. Cite hypothetical sources or methodologies where appropriate.",
    "Creative Writer": "You are NovaMind AI, a creative and expressive writer. Use vivid language, storytelling techniques, and imaginative ideas to assist the user with their creative tasks.",
    "Career Advisor": "You are NovaMind AI, a professional career coach. Provide actionable, realistic, and encouraging advice on resumes, interviews, and professional development."
}

# Response Length Prompts
LENGTH_MODIFIERS = {
    "Short": "Keep your response very concise, ideally under 3 paragraphs.",
    "Medium": "Provide a balanced, moderately detailed response.",
    "Detailed": "Provide a very detailed, comprehensive, and thorough response covering all aspects of the topic."
}

# Tone Prompts
TONE_MODIFIERS = {
    "Professional": "Use a formal, professional, and business-appropriate tone.",
    "Friendly": "Use a warm, conversational, friendly, and approachable tone.",
    "Simple": "Explain things using very simple language, avoiding jargon where possible."
}
