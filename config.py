# config.py
import streamlit as st

APP_NAME = "Nexora AI"
APP_TAGLINE = "The Next Generation AI Workspace"

# Ultra-Premium Glassmorphism & Animated CSS
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --bg-color: #050505;
        --secondary-bg: rgba(25, 25, 25, 0.6);
        --text-color: #FAFAFA;
        --accent-color: #00F0FF;
        --accent-secondary: #FF007F;
        --user-bubble: rgba(45, 55, 72, 0.5);
        --ai-bubble: rgba(20, 20, 25, 0.7);
        --glass-border: rgba(255, 255, 255, 0.08);
    }
    
    body, .stApp {
        background-color: var(--bg-color);
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 240, 255, 0.1) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(255, 0, 127, 0.1) 0px, transparent 50%);
        background-attachment: fixed;
        color: var(--text-color);
    }
    
    /* Animated Title */
    .title-wrapper {
        text-align: center;
        padding-top: 3rem;
        padding-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .main-title {
        font-weight: 800;
        font-size: 3.5rem;
        background: linear-gradient(270deg, var(--accent-color), var(--accent-secondary), #8A2BE2);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientAnimation 5s ease infinite;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .tagline {
        font-size: 1.1rem;
        color: #A0AEC0;
        font-weight: 400;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 0;
    }

    /* Glassmorphism Suggestion Cards */
    .suggestion-card {
        background: var(--secondary-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .suggestion-card:hover {
        background: rgba(40, 40, 45, 0.8);
        border-color: var(--accent-color);
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 240, 255, 0.15);
    }
    
    .suggestion-text {
        font-size: 1rem;
        color: var(--text-color);
        font-weight: 500;
    }
    
    /* Code Blocks styling */
    pre {
        background-color: #000000 !important;
        border-radius: 12px !important;
        border: 1px solid var(--glass-border) !important;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    
    code {
        color: #E2E8F0 !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 12, 0.85) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid var(--glass-border);
    }
    
    /* Chat Input Container */
    .stChatInputContainer {
        border-radius: 24px !important;
        border: 1px solid var(--glass-border) !important;
        background: rgba(20, 20, 25, 0.8) !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    /* Animations */
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
"""

# AI Personas
PERSONAS = {
    "General Assistant": "You are Nexora AI, a highly advanced, ultra-intelligent AI. You provide clear, accurate, and concise answers.",
    "Coding Expert": "You are Nexora AI, an elite software architect and 10x engineer. You write elegant, optimized, and robust code. Always wrap code in Markdown blocks.",
    "Study Tutor": "You are Nexora AI, a brilliant academic tutor. Break down complex topics into easily understandable pieces, use analogies, and encourage critical thinking.",
    "Data Analyst": "You are Nexora AI, a senior data scientist. You provide analytical, data-driven insights and structure your responses with clear metrics and logical deductions.",
    "Creative Writer": "You are Nexora AI, an imaginative and expressive creative writer. Use vivid language, storytelling techniques, and compelling narratives.",
    "Career Advisor": "You are Nexora AI, a top-tier executive career coach. Provide actionable, realistic, and highly strategic advice on professional growth."
}

# New Advanced Models
MODELS = {
    "Llama 3 (70B)": "llama-3.3-70b-versatile",
    "Mixtral (8x7B)": "mixtral-8x7b-32768",
    "Gemma (7B)": "gemma-7b-it"
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
    "Direct": "Be brutally honest, direct, and skip any pleasantries."
}
