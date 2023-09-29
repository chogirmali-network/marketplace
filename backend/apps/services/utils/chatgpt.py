import requests
import os

def chat_gpt3(prompt, user):
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 60,
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
    response_json = response.json()
    return {
        'content': response_json['choices'][0]['message']['content'],
        'role': response_json['choices'][0]['message']['role'],
        'user': user,
    }

def save_chat_gpt3(chat_gpt3_dict):
    from services.models import ChatGPT
    chat_gpt = ChatGPT(**chat_gpt3_dict)
    chat_gpt.save()
    return chat_gpt