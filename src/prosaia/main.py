import os

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates('templates')

load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)  # type: ignore
model = genai.GenerativeModel('models/gemini-2.5-pro')  # type: ignore


@app.get('/')
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.websocket('/ws')
async def endpoint_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = model.generate_content(data)
            await websocket.send_text(response.text)
    except Exception as erro:
        print(f'Erro no websocket: {erro}')
