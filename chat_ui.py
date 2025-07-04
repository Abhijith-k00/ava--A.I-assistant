import os
import json
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config — sidebar open by default
st.set_page_config(
    page_title="AVA",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 340px !important;
            min-width: 340px !important;
            transition: all 0.3s ease-in-out;
        }

        [data-testid="stSidebar"][aria-expanded="false"] {
            display: none !important;
        }

        [data-testid="stSidebar"][aria-expanded="false"] ~ div.stApp {
            margin-left: 0 !important;
            width: 100% !important;
            max-width: 100% !important;
        }

        [data-testid="stChatMessage"] {
            padding: 0.5rem 1rem;
        }

        [data-testid="stChatMessageAvatar"] {
            display: none !important;
        }

        .assistant-message {
            background-color: #2b313e;
            border-radius: 0.5rem;
            padding: 0.75rem;
            margin: 0.25rem 0;
        }

        .user-message {
            padding: 0.75rem;
            margin: 0.25rem 0;
        }

        .sidebar-entry {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.4rem;
            margin-bottom: 0.4rem;
            overflow-wrap: anywhere;
        }

        .sidebar-entry button {
            font-size: 0.75rem;
            padding: 0.15rem 0.3rem;
            line-height: 1;
            white-space: nowrap;
        }
    </style>
""", unsafe_allow_html=True)



# Chat logs directory
CHAT_DIR = "chat_logs"
os.makedirs(CHAT_DIR, exist_ok=True)

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_title" not in st.session_state:
    st.session_state.chat_title = None
if "chat_id" not in st.session_state:
    st.session_state.chat_id = f"chat_{len(os.listdir(CHAT_DIR)) + 1}.json"
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# LLM setup
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    base_url="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY")
)
chat_agent = ConversationChain(llm=llm, memory=st.session_state.memory, verbose=False)

# Generate title from conversation
def generate_chat_title(messages):
    convo = "\n".join([m["content"] for m in messages[-3:]])
    system_prompt = (
        "Create a 3-5 word title summarizing this conversation. "
        "Be specific and avoid generic titles. Output only the title."
    )
    try:
        response = llm.invoke([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": convo}
        ])
        title = response.content.strip().replace('"', '').capitalize()
        return title if title else "New conversation"
    except Exception:
        return "New conversation"

# Sidebar UI
st.sidebar.title("💬 AVA")
if st.sidebar.button("➕ New Chat", use_container_width=True):
    st.session_state.messages = []
    st.session_state.chat_title = None
    st.session_state.chat_id = f"chat_{len(os.listdir(CHAT_DIR)) + 1}.json"
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
    st.rerun()

# Load chat history
try:
    chat_files = sorted([f for f in os.listdir(CHAT_DIR) if f.endswith('.json')], reverse=True)
except PermissionError:
    chat_files = []

for chat_file in chat_files:
    try:
        with open(os.path.join(CHAT_DIR, chat_file), "r") as f:
            data = json.load(f)
            title = data.get("title", "Untitled chat")
    except Exception:
        title = "Untitled chat"

    with st.sidebar.container():
        cols = st.columns([7, 1])
        if cols[0].button(title, key=f"load_{chat_file}", use_container_width=True):
            with open(os.path.join(CHAT_DIR, chat_file), "r") as f:
                data = json.load(f)
                st.session_state.messages = data["messages"]
                st.session_state.chat_title = data.get("title")
                st.session_state.chat_id = chat_file
                st.session_state.memory = ConversationBufferMemory(return_messages=True)
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        st.session_state.memory.chat_memory.add_user_message(msg["content"])
                    else:
                        st.session_state.memory.chat_memory.add_ai_message(msg["content"])
            st.rerun()

        if cols[1].button("🗑️", key=f"delete_{chat_file}"):
            try:
                os.remove(os.path.join(CHAT_DIR, chat_file))
            except Exception:
                pass
            if st.session_state.get("chat_id") == chat_file:
                st.session_state.messages = []
                st.session_state.chat_title = None
                st.session_state.chat_id = f"chat_{len(os.listdir(CHAT_DIR)) + 1}.json"
                st.session_state.memory = ConversationBufferMemory(return_messages=True)
            st.rerun()

# Chat UI
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #00c3ff; margin-bottom: 0.5rem;'>AVA</h1>
        <p style='color: #c0c0c0;'>Your Smart Assistant</p>
    </div>
    <hr style='background: #444; margin: 1rem 0;'>
""", unsafe_allow_html=True)

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-message'>{msg['content']}</div>", unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.memory.chat_memory.add_user_message(prompt)

    with st.spinner(""):
        response = chat_agent.predict(input=prompt).replace("Assistant:", "").strip()

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.memory.chat_memory.add_ai_message(response)

    if len(st.session_state.messages) == 2:
        st.session_state.chat_title = generate_chat_title(st.session_state.messages)

    with open(os.path.join(CHAT_DIR, st.session_state.chat_id), "w") as f:
        json.dump({
            "title": st.session_state.chat_title,
            "messages": st.session_state.messages
        }, f, indent=2)

    st.rerun()
