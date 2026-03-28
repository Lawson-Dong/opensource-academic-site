# AI Agent Engineering: LangChain Full Stack Development 🤖

This guide introduces how to use VSCode for LangChain full stack development, creating and deploying AI Agents.

## Project Setup 📁

### 1. Create Project Folder

```bash
# Create project folder
mkdir langchain_agent_development

# Enter project directory
cd langchain_agent_development
```

### 2. Open Project in VSCode

Create a new `app.py` file in VSCode as the main entry point for the project.

## Install Dependencies 🔧

### 1. Install uv

Execute the following command in VSCode terminal to install uv:

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Use uv to Manage Python Versions

uv can automatically download and manage Python versions, no need to pre-install Python on the system:

```bash
# View Python versions managed by uv
uv python list

# Install specific Python version
uv python install 3.12

# View currently used Python
uv python find
```

### 3. Initialize Project

```bash
# Initialize project, create pyproject.toml
uv init
```

### 4. Install Dependency Packages

```bash
uv add python-dotenv langchain langchain-deepseek langgraph
```

### 5. View Installed Packages

```bash
uv pip list
```

## Common Issue Resolution 🛠️

### Project Name Conflicts with Dependency Package

If you encounter the following error when installing dependencies:

```
error: Requirement name `langchain` matches project name `langchain`, but self-dependencies are not permitted without the `--dev` or `--optional` flags. If your project name (`langchain`) is shadowing that of a third-party dependency, consider renaming the project.
```

Solution:

```bash
# View project name in pyproject.toml
cat pyproject.toml

# Open with VSCode to edit
code pyproject.toml

# Change to a different name (e.g., langchain-agent-development)

# Confirm file has been saved and modified successfully
cat pyproject.toml
```

Reinstall dependencies after modification:

```bash
uv add python-dotenv langchain langchain-deepseek langgraph
```

## Project File Structure 📁

### 1. Create agent_langgraph.py

Create a new `agent_langgraph.py` file in the project root directory for developing agent functionality.

### 2. Create .env File

Create a new `.env` file in the project root directory to associate API keys:

```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxx
```

API Key Acquisition:
- **DeepSeek**: [https://platform.deepseek.com/](https://platform.deepseek.com/) (tokens are cheaper)
- **OpenAI**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) (API Key format is the same)

### 3. AI Agent API and API Key Introduction

**AI Agent API** is an interface protocol that enables agents to interact with external systems, tools, or large models in a standardized manner, equivalent to the entry point for the agent's "hands and feet" and "senses".

**API Key** is a key used to verify caller identity, permissions, and billing credentials, equivalent to the agent's "ID card" and "pass" when using APIs. (In the AI era, this is private information, like your ID number, don't share it with others casually)

### 4. Create quick_test.py

Create a new `quick_test.py` file in the project root directory for running test code to verify if the API key is properly associated and the agent status:

```python
# Test environment preparation
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

# Check API Key
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: DEEPSEEK_API_KEY not found, please set it in .env file")
    exit(1)

print(f"API Key configured: {api_key[:10]}...")

# Test model
llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key
)

# Output in terminal
print("\nTesting connection...")
try:
    response = llm.invoke("Hello, please briefly introduce yourself in one sentence")
    print(f"\nModel response: {response.content}")
    print("\n✅ Model connection successful!")
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
```

### 5. Create agent_langgraph.py

Create a new `agent_langgraph.py` file in the project root directory for creating a LangGraph-based agent with tool calling and memory functionality:

```python
# agent_langgraph.py
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

# Initialize model
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# Define tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions, e.g., '2+3*4'"""
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

@tool
def get_text_length(text: str) -> str:
    """Get the character length of text"""
    return f"Text length: {len(text)} characters"

@tool
def reverse_string(text: str) -> str:
    """Reverse a string"""
    return f"Reversal result: {text[::-1]}"

tools = [calculator, get_text_length, reverse_string]

# Create memory (optional)
memory = MemorySaver()

# Create agent (using langgraph)
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,  # Add memory functionality
)

# Main function
def main():
    print("=" * 50)
    print("LangChain Agent Started (LangGraph Version)!")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    # Configure session ID (for memory)
    config = {"configurable": {"thread_id": "1"}}
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        try:
            # Call agent
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            # Get last message (agent's response)
            last_message = response["messages"][-1]
            print(f"\nAgent: {last_message.content}")
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```

**Functionality Description**:
- Use LangGraph to create React-style agents
- Integrated three tools: calculator, text length calculation, and string reversal
- Supports conversation memory, able to remember previous conversation content
- Provides interactive command-line interface for easy testing and use

### 6. Enable Agent to Access Internet - Integrate Tavily API

To enable the agent to access the internet and get the latest information, you can integrate Tavily API. Tavily is a search engine API specifically designed for AI applications (especially large language models and AI agents). It is not a traditional search engine website for ordinary users, but a backend service provided for developers.

**Integration Steps**:

1. **Get Tavily API Key**
   - Visit [Tavily Official Website](https://tavily.com/) to register an account
   - Get API Key in the console

2. **Add Tavily API Key to .env File**

```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxx
```

3. **Install Tavily Dependency**

```bash
uv add tavily-python
```

4. **Modify agent_langgraph.py File, Add Tavily Search Tool**

```python
# agent_langgraph.py (add Tavily search tool)
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tavily import TavilyClient

load_dotenv()

# Initialize model
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# Initialize Tavily client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Define tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions, e.g., '2+3*4'"""
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

@tool
def get_text_length(text: str) -> str:
    """Get the character length of text"""
    return f"Text length: {len(text)} characters"

@tool
def reverse_string(text: str) -> str:
    """Reverse a string"""
    return f"Reversal result: {text[::-1]}"

@tool
def search_internet(query: str) -> str:
    """Search the internet for latest information, e.g., '2024 Olympics location'"""
    try:
        response = tavily_client.search(query=query, max_results=3)
        results = response.get('results', [])
        if not results:
            return "No relevant information found"
        
        # Organize search results
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            url = result.get('url', 'No link')
            content = result.get('content', 'No content')[:200] + '...' if result.get('content') else 'No content'
            formatted_results.append(f"{i}. {title}\n   Link: {url}\n   Content: {content}")
        
        return "\n".join(formatted_results)
    except Exception as e:
        return f"Search error: {str(e)}"

tools = [calculator, get_text_length, reverse_string, search_internet]

# Create memory (optional)
memory = MemorySaver()

# Create agent (using langgraph)
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,  # Add memory functionality
)

# Main function
def main():
    print("=" * 50)
    print("LangChain Agent Started (LangGraph Version)!")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    # Configure session ID (for memory)
    config = {"configurable": {"thread_id": "1"}}
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        try:
            # Call agent
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            # Get last message (agent's response)
            last_message = response["messages"][-1]
            print(f"\nAgent: {last_message.content}")
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```

**Functionality Description**:
- Integrated Tavily search engine API, enabling the agent to access the internet
- Added `search_internet` tool for searching latest information
- Agent can automatically call search tools to get relevant information based on user questions
- Search results are organized and presented in a user-friendly format

## VSCode Development File Architecture Display 📁

For convenience during development, we generally organize files in the project folder in the following format:

```
langchain/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── main.py                    # Main program entry point
├── tools/                     # Tools package directory
│   ├── __init__.py           # Package initialization file
│   ├── math_tools.py         # Math calculation tools
│   ├── text_tools.py         # Text processing tools
│   ├── file_tools.py         # File operation tools
│   ├── web_tools.py          # Web-related tools
│   └── data_tools.py         # Data processing tools
└── agents/                    # Agent configuration
    ├── __init__.py
    └── my_agent.py           # Agent definition  
```

### Root Directory File Introduction

#### .env - Environment Variable Configuration

```python
# Store sensitive information and configuration
DEEPSEEK_API_KEY=sk-xxxxx
OPENAI_API_KEY=sk-xxxxx
TAVILY_API_KEY=tvly-xxxxx
DATABASE_URL=postgresql://localhost/mydb  
```

**Purpose**:
- Store API keys, database passwords, and other sensitive information
- Use different configurations for different environments (development/test/production)
- Exclude via .gitignore to avoid leakage

#### .gitignore - Git Ignore File

```gitignore
# Virtual environments
.venv/
venv/

# Environment variables
.env
.env.local

# Python cache
__pycache__/
*.pyc

# IDE configurations
.vscode/
.idea/

# Log and temporary files
*.log
*.tmp
```

**Purpose**:
- Specify which files should not be tracked by Git
- Prevent committing sensitive information, temporary files, dependency packages, etc.

#### pyproject.toml - Project Configuration File

```toml
[project]
name = "langchain-tools"
version = "1.0.0"
description = "LangChain Agent Tool Set"
requires-python = ">=3.8"
dependencies = [
    "langchain>=0.1.0",
    "langchain-deepseek>=1.0.0",
    "python-dotenv>=1.0.0",
    "langgraph>=0.0.20",
    "tavily-python>=0.1.0",
]

[project.scripts]
my-agent = "agents.my_agent:chat"  # Define command-line entry point
```

**Purpose**:
- Standard configuration file for modern Python projects
- Define project dependencies, metadata, entry points
- Recognized by tools like uv and pip

#### uv.lock - Dependency Lock File

```python
# Automatically generated, do not edit manually
# Records exact versions and hash values of all dependencies
```

**Purpose**:
- Lock exact versions of all dependencies
- Ensure team members and environments use exactly the same dependencies
- Automatically maintained by uv

#### main.py - Main Program Entry Point

```python
# Program startup file
from agents.my_agent import chat

if __name__ == "__main__":
    chat()
```

**Purpose**:
- Unified entry point for the program
- Usually only does startup work, does not contain business logic
- Can be run via python main.py

## First Development Project 🌟

[LangChain First Development Project](https://github.com/Lawson-Dong/langchain_develop_first) - An AI Agent development experimental project based on LangChain

## LangChain Platform Introduction 📚

LangChain is a platform that integrates various agent development components, providing a complete AI Agent development ecosystem.

### Related Links

- **LangChain Official Website**: [https://www.langchain.com/](https://www.langchain.com/)
- **LangSmith**: [https://smith.langchain.com/o/4e44cff0-75d9-4635-9e90-cf134ecac629](https://smith.langchain.com/o/4e44cff0-75d9-4635-9e90-cf134ecac629)
  - One-stop platform for deploying/developing/debugging agents
- **LangSmith Fleet**: Provides more powerful Agent management features

## Development Process 🚀

1. **Project Initialization**: Use uv to create project and virtual environment
2. **Install Dependencies**: Add langchain and related packages
3. **Write Code**: Implement AI Agent logic in app.py
4. **Test Run**: Verify Agent functionality
5. **Deploy Online**: Use LangSmith for deployment and monitoring

## Example Code 📝

```python
# app.py example code
import os
from dotenv import load_dotenv
from langchain_deepseek import DeepSeekLLM

# Load environment variables
load_dotenv()

# Initialize LLM
llm = DeepSeekLLM(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# Test LLM
response = llm("Hello, LangChain!")
print(response)
```

---

*Start your LangChain full stack development journey!* 🎉