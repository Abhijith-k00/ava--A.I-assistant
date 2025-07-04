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

\`\`\`bash
git clone https://github.com/Abhijith-k00/ava--A.I-assistant.git
cd ava--A.I-assistant
\`\`\`

---

### 🔹 Step 2: Add Your API Key

Create a \`.env\` file in the root folder and paste your OpenRouter API key:

\`\`\`env
OPENROUTER_API_KEY=your-real-api-key-here
\`\`\`

> ⚠️ **Important:** Do NOT upload this file to GitHub.  
> Instead, share only \`.env.example\` for others to use.

---

### 🔹 Step 3: Install Dependencies

Make sure Python 3.10+ is installed. Then install required libraries:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

> If you’re using Pipfile instead of requirements.txt, run:

\`\`\`bash
pipenv install
\`\`\`

---

### 🔹 Step 4: Run the App

To launch the chatbot interface:

\`\`\`bash
streamlit run chat_ui.py
\`\`\`

Your browser will open the app (usually at: http://localhost:8501)

---

## 📸 Screenshots

> Add screenshots of the app here. For example:
> - Chat UI interface
> - Sidebar with chat history
> - Response flow with memory

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
