# utils/export.py
import datetime

def export_chat_to_text(messages, app_name="Nexora AI"):
    """Formats the chat history as a plain text string."""
    text_content = f"{app_name} - Chat Export\nDate: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    for msg in messages:
        role = "User" if msg["role"] == "user" else app_name
        text_content += f"[{role}]:\n{msg['content']}\n\n{'-'*40}\n\n"
        
    return text_content

def export_chat_to_markdown(messages, app_name="Nexora AI"):
    """Formats the chat history as a markdown string."""
    md_content = f"# {app_name} - Chat Export\n**Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    for msg in messages:
        role = "👤 **User**" if msg["role"] == "user" else f"🌌 **{app_name}**"
        md_content += f"{role}:\n\n{msg['content']}\n\n---\n\n"
        
    return md_content
