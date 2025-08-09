# Prosa.IA

Prosa.IA é um projeto de assistente conversacional baseado em IA, construído com FastAPI e Gemini (Google Generative AI). Ele permite conversas em tempo real via WebSocket, utilizando uma interface web simples.

## Funcionalidades
- Interface web para conversação com IA
- Backend FastAPI
- Integração com Gemini (Google Generative AI)
- Comunicação em tempo real via WebSocket

## Pré-requisitos
- Python 3.13+
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências
- Chave de API do Google Generative AI (Gemini)

## Instalação

1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/briellll/prosaia.git
   cd prosaia
   ```

2. **Instale as dependências:**
   ```powershell
   poetry install
   ```

3. **Configure a chave de API:**
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

## Como iniciar o projeto

1. **Execute o servidor FastAPI:**
   ```powershell
   poetry run uvicorn src.prosaia.main:app --reload
   ```

2. **Acesse a interface web:**
   Abra o navegador e acesse [http://localhost:8000](http://localhost:8000)

## Estrutura do Projeto
```
prosaia/
├── src/
│   └── prosaia/
│       ├── main.py
│       └── __init__.py
├── templates/
│   └── index.html
├── tests/
│   └── __init__.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Testes
Para rodar os testes:
```powershell
poetry run pytest
```

## Licença
Este projeto está sob a licença MIT.

## Autor
Gabriel ([carloscgmorais@gmail.com](mailto:carloscgmorais@gmail.com))
