# 🤖 FURIA Fan Bot

Um bot para fãs do time de CS:GO da FURIA, feito com Python e a biblioteca `pyTelegramBotAPI`.  
Com ele você pode ver próximos jogos, simular a torcida, responder quizzes e muito mais.

**Acesse o bot:** [Clique aqui para abrir no Telegram](https://t.me/SEU_BOT)
---

# 🚀 Funcionalidades

- `/start` – Menu com botões interativos
- `/noticias` – Últimas notícias da FURIA
- `/gritar` – Simulador de torcida 🔥
- `/quizz` – Quiz com botões inline
- Botões inline com atualizações sobre jogos e ranking

---

# 🛠️ Tecnologias

- React
- Python 3.10+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- dotenv (`python-dotenv`)

---
### Clone o repositorio

```
git clone https://github.com/ursarah/telegram-chatbot.git
```


# ▶️ Como rodar
## Back end

1. Entre no repositorio:

```bash
cd backend
```

2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo **.env** e nomeei o seu token como **TOKEN_BOT**:

```.env
TOKEN_BOT=SEU_TOKEN_AQUI
```

4. Rode o codigo localmente:

```bash
python main.py
```

## Front end

1. Entre no repositorio:

```bash
cd frontend
```

2. Instale as dependencias:

```bash
npm install
```

3. Rode localmente:

```bash
npm run dev
```

4. Entre em http://localhost:5173/
