import os
from dotenv import load_dotenv
from pathlib import Path
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv(dotenv_path=Path('.') / '.env')

# Set up LLM with OpenRouter
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",  # or "deepseek-ai/deepseek-coder"
    base_url="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY")
)

# Define calculator tool
def calculator_tool(input_str: str) -> str:
    try:
        return str(eval(input_str))
    except Exception as e:
        return f"Error: {str(e)}"

# Wikipedia tool
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

tools = [
    Tool(name="Calculator", func=calculator_tool, description="Useful for basic math."),
    Tool(name="Wikipedia", func=wiki_tool.run, description="Use this for general knowledge questions.")
]

# Setup memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    handle_parsing_errors=True,
    verbose=True
)

# CLI loop
print("🧠 Talk to your AI Agent! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Bye!")
        break

    try:
        result_data = agent.invoke({
            "input": user_input,
            "chat_history": memory.buffer
        })

        result = result_data["output"] if isinstance(result_data, dict) and "output" in result_data else str(
            result_data)

        # Add current exchange to memory manually if not already
        memory.save_context({"input": user_input}, {"output": result})

        # Display all chat history cleanly
        os.system('cls' if os.name == 'nt' else 'clear')  # clears screen each time for cleaner history
        print("🧠 Chat History:\n")
        for msg in memory.buffer:
            if msg.type == "human":
                print(f"You: {msg.content}")
            elif msg.type == "ai":
                print(f"AI: {msg.content}")
        print()
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
