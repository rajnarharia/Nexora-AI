# services/ai_service.py
import os
import streamlit as st
from groq import Groq
import config

def get_groq_client():
    """Initializes and returns the Groq client."""
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
            
    if not api_key:
        return None
    return Groq(api_key=api_key)

def enhance_prompt_internally(client, user_prompt, model="llama-3.3-70b-versatile"):
    """Uses a quick secondary API call to enhance the user's prompt."""
    if not client:
        return user_prompt
        
    enhancement_system_prompt = (
        "You are an expert prompt engineer. Your job is to take a short or unclear "
        "user prompt and rewrite it into a highly detailed, clear, and comprehensive "
        "prompt that will yield the best possible response from an AI. "
        "Preserve the original intent completely. Do not answer the prompt, ONLY return the enhanced prompt."
    )
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": enhancement_system_prompt},
                {"role": "user", "content": f"Enhance this prompt: '{user_prompt}'"}
            ],
            temperature=0.3,
            max_tokens=256
        )
        enhanced = completion.choices[0].message.content.strip()
        if enhanced.startswith('"') and enhanced.endswith('"'):
            enhanced = enhanced[1:-1]
        return enhanced
    except Exception as e:
        return user_prompt

def generate_follow_up_questions(client, conversation_history, latest_response, model="llama-3.3-70b-versatile"):
    """Generates 3 relevant follow-up questions based on the chat context."""
    if not client:
        return []
        
    system_prompt = (
        "Based on the conversation history and the latest AI response, suggest exactly 3 "
        "short, relevant follow-up questions the user could ask next. "
        "Return them as a simple numbered list (1., 2., 3.) without any other text or explanation."
    )
    
    context_msgs = conversation_history[-4:] if len(conversation_history) > 4 else conversation_history
    
    messages = [{"role": "system", "content": system_prompt}]
    for msg in context_msgs:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "assistant", "content": latest_response})
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        content = completion.choices[0].message.content.strip()
        
        questions = []
        for line in content.split('\n'):
            line = line.strip()
            if len(line) > 2 and line[0].isdigit() and (line[1] == '.' or line[1] == ')'):
                q = line[2:].strip()
                if q:
                    questions.append(q)
        
        return questions[:3]
    except Exception:
        return []

def get_chat_completion_stream(client, messages, persona, length, tone, model="llama-3.3-70b-versatile", context_window=2048):
    """Returns a streaming response from the Groq API."""
    if not client:
        raise ValueError("Groq client is not initialized. API key missing.")
        
    sys_prompt = f"{config.PERSONAS.get(persona, config.PERSONAS['General Assistant'])} "
    sys_prompt += f"{config.LENGTH_MODIFIERS.get(length, '')} "
    sys_prompt += f"{config.TONE_MODIFIERS.get(tone, '')}"
    
    api_messages = [{"role": "system", "content": sys_prompt}]
    
    for msg in messages:
        api_messages.append({"role": msg["role"], "content": msg["content"]})
        
    stream = client.chat.completions.create(
        model=model,
        messages=api_messages,
        temperature=0.7,
        max_tokens=context_window,
        stream=True
    )
    
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            yield content
