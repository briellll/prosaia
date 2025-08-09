import os

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates

load_dotenv()
app = FastAPI()

templates = Jinja2Templates('templates')
API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=API_KEY)  # type: ignore
model = genai.GenerativeModel('models/gemini-2.5-pro')  # type: ignore


@app.get('/')
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.websocket('/ws')
async def end_point_websocket(websocket: WebSocket):
    await websocket.accept()
    conversation_history = []
    try:
        while True:
            content = await websocket.receive_text()
            conversation_history.append(f'usuario: {content}')
            context  = '\n'.join(conversation_history)+'\nAssistente:'
            response_stream = model.generate_content(context, stream=True)
            response_model = ''
            for chunk in response_stream:
                if chunk.text:
                    await websocket.send_text(chunk.text)
                    response_model += chunk.text
            conversation_history.append(f'Assistente:{response_model}')
    except Exception as erro:
        print(f'erro no websocket: {erro}')
