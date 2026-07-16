# NovaMind AI ✨

**Your Intelligent AI Workspace**

NovaMind AI is a premium, modern, and highly customizable AI assistant built with Streamlit and powered by the Groq API. It transforms standard chat interfaces into a professional workspace suitable for coding, research, studying, and more.

## 🚀 Features

- **Modern Professional UI**: A sleek, dark-themed interface with custom CSS for a premium feel.
- **AI Personality Modes**: Switch between General Assistant, Coding Expert, Study Tutor, Research Assistant, Creative Writer, and Career Advisor.
- **Smart Response Controls**: Adjust the length (Short, Medium, Detailed) and tone (Professional, Friendly, Simple) of the AI's responses.
- **Conversation Memory**: Remembers your chat history during the session for seamless follow-up questions.
- **Streaming Responses**: Real-time typewriter effect for faster reading and better UX.
- **Prompt Enhancer (Beta)**: Automatically refines and improves your prompt internally before sending it to the AI to get better results.
- **Smart Follow-up Suggestions**: Predicts and suggests 3 relevant follow-up questions after every AI response.
- **Export Conversation**: Download your entire chat history in TXT or Markdown format.
- **Chat Statistics**: Track your message counts directly in the sidebar.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model API**: [Groq](https://groq.com/) (Llama-3.3-70b-versatile)
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
   *Note: Never share your API key or commit the `.env` file to version control.*

## 🏃‍♂️ How to Run Locally

Run the application using Streamlit:
```bash
streamlit run app.py
```
The application will open automatically in your default web browser at `http://localhost:8501`.

## 📸 Screenshots
*(Add screenshots of the Welcome screen, Chat interface, and Sidebar settings here)*

---
Built with ❤️ using Streamlit & Groq.
