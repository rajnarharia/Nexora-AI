# Nexora AI 🌌

**The Next Generation AI Workspace**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-00F0FF?style=for-the-badge&logo=streamlit)](#) *(Replace `#` with your actual Streamlit Community Cloud or deployment link)*

Nexora AI is an ultra-premium, highly customizable AI assistant built with Streamlit and powered by advanced LLM Engines via the Groq API. It transforms standard chat interfaces into a professional workspace featuring glassmorphism design, advanced settings, and smart AI capabilities.

## 🚀 Features

- **Ultra-Premium Glassmorphism UI**: High-end styling with animated gradients, blur effects, and sleek dark mode aesthetics.
- **Dynamic Neural Engines**: Seamlessly switch between Llama 3 (70B), Mixtral (8x7B), and Gemma (7B) on the fly.
- **AI Persona Configuration**: Choose from General Assistant, Coding Expert, Study Tutor, Data Analyst, Creative Writer, and Career Advisor.
- **Advanced Context & Output Settings**: Adjust output length, tone, and control the exact max output tokens.
- **Plugins & Tools Simulation**: Visual toggles for Mock Web Search and File Upload context simulation for a complete SaaS feel.
- **Neural Prompt Enhancer**: Automatically refines and optimizes your prompt via an internal API call before generating the response.
- **Smart Follow-up Suggestions**: Generates contextual next-steps and logical paths after every AI response.
- **Advanced Analytics**: Track user messages, AI responses, and estimated token usage dynamically in the sidebar.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) with Custom Glassmorphism CSS
- **AI Engine**: [Groq API](https://groq.com/)
- **Environment Management**: python-dotenv

## ⚙️ Installation & Setup

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd path/to/project
   ```

2. **Create a virtual environment** (Optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Setup**:
   Create a `.env` file in the root directory and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

## 🏃‍♂️ How to Run Locally

Run the application using Streamlit:
```bash
streamlit run app.py
```
The application will open automatically in your default web browser at `http://localhost:8501`.

---
Built with 🌌 using Streamlit & Groq.
