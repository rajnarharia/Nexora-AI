from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def my_output(query):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.7,
        max_tokens=1024
    )

    return completion.choices[0].message.content

# ------------------ UI ------------------

st.set_page_config(page_title="Chat_Bot")
st.header("Chat_Bot")

user_input = st.text_input("Ask your question")

if st.button("Submit Query"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = my_output(user_input)

        st.subheader("Answer")
        st.write(answer)