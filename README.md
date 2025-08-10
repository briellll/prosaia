# Prosa.IA

Prosa.IA é um projeto de assistente conversacional baseado em IA, construído com FastAPI e Gemini (Google Generative AI). Ele permite conversas em tempo real via WebSocket, utilizando uma interface web simples.

## Novidade: Sotaque Regional
Agora o Prosa.IA responde usando sotaques regionais brasileiros! Por padrão, o assistente utiliza o sotaque nordestino, com expressões típicas como “oxe”, “ocê”, “num” e “vixe”, tornando a conversa mais natural e divertida. Também é possível adaptar para outros sotaques, como o paulista, deixando a experiência ainda mais personalizada.

Essa funcionalidade foi implementada através de um mecanismo de prompt que insere o contexto e orienta o modelo a responder conforme o sotaque desejado.

## Funcionalidades
- Interface web para conversação com IA
- Backend FastAPI
- Integração com Gemini (Google Generative AI)
- Comunicação em tempo real via WebSocket
- Respostas personalizadas com sotaque regional (nordestino e paulista)

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
│       ├── __init__.py
│       └── prompt_engine.py  # Funções para personalizar o sotaque das respostas
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
