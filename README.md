# 💬 AVA — Your Smart AI Assistant

AVA is a context-aware AI assistant built using **Streamlit**, **Langchain**, and **Mistral-7B** (via OpenRouter).  
It supports memory, a clean chat interface, and local chat history with options to create or delete chats.

---

## 🚀 Features

- 🧠 Context-aware memory (remembers what you said)
- 🧼 Built with Streamlit for a clean web UI
- 💬 Uses `mistralai/mistral-7b-instruct` via OpenRouter
- 💾 Local chat history with auto-save and title generation
- ➕ "New Chat" and 🗑️ "Delete Chat" in the sidebar
- 🔐 Keeps your API key secure via `.env` file

---

## 📦 Folder Structure

\`\`\`
ava-chat/
├── .idea/                # PyCharm project settings (optional to commit)
├── .env.example          # Template for your OpenRouter API key
├── Pipfile               # Package manager file (for pipenv users)
├── Pipfile.lock          # Lock file for dependencies
├── agent_memory.pkl      # (Optional) saved memory file
├── chat_ui.py            # Main Streamlit chatbot app
\`\`\`

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Clone the Repository

git clone https://github.com/Abhijith-k00/ava--A.I-assistant.git

cd ava--A.I-assistant

---

### 🔹 Step 2: Add Your API Key

Create a \`.env\` file in the root folder and paste your OpenRouter API key:

OPENROUTER_API_KEY=your-real-api-key-here

> ⚠️ **Important:** Do NOT upload this file to GitHub.  
> Instead, share only \`.env.example\` for others to use.

---

### 🔹 Step 3: Install Dependencies

Make sure Python 3.10+ is installed. Then install required libraries:

> If you’re using Pipfile run:

pipenv install
 
Required packages include:

streamlit – for the web UI

langchain – for LLM agent orchestration

openai – to connect to OpenAI or compatible LLMs

python-dotenv – to manage API keys via .env files

---

### 🔹 Step 4: Run the App

To launch the chatbot interface:

streamlit run chat_ui.py

Your browser will open the app (usually at: http://localhost:8501)

---

## 📸 Screenshots

![Screenshot 2025-07-04 212900](https://github.com/user-attachments/assets/06664bf3-f8c0-408a-85e3-d6edef70ad99)
![Screenshot 2025-07-04 221201](https://github.com/user-attachments/assets/32793d8d-bd17-47f8-b6ca-0d758bc6025b)
![Screenshot 2025-07-04 221306](https://github.com/user-attachments/assets/eade9e62-b4fc-4e3b-bc67-b38cd69b9d80)

---

## 🧠 Model Info

This project uses the **\`mistralai/mistral-7b-instruct\`** model served via [OpenRouter](https://openrouter.ai), which supports OpenAI-style API calls.

You can swap models by editing this line in \`chat_ui.py\`:

\`\`\`python
model="mistralai/mistral-7b-instruct"
\`\`\`

---

## 🙌 Credits

Built with:

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenRouter](https://openrouter.ai)
EOF
