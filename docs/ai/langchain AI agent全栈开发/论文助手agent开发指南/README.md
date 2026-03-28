# Paper Assistant Agent Development Tools Guide 📚

This guide introduces the tools that may be used during the development of paper assistant agents, including GROBID for paper parsing, Streamlit for building interactive web applications, Chroma for vector storage, and Docker sandbox for secure code execution.

---

## GROBID 🔍

GROBID (GeneRation Of BIbliographic Data) is an open-source machine learning library specifically designed for extracting structured information from academic papers.

### Key Features

- **PDF Parsing**: Convert academic paper PDFs to structured XML/TEI format
- **Metadata Extraction**: Automatically extract metadata such as title, authors, abstract, keywords, etc.
- **Citation Parsing**: Identify and extract reference information
- **Full-text Structuring**: Organize paper content by sections, paragraphs, figures, etc.
- **Table and Figure Processing**: Extract table and figure information

### Technical Features

- **Machine Learning Based**: Uses machine learning algorithms like CRF (Conditional Random Fields) for information extraction
- **High Performance**: Fast processing speed, supports batch processing
- **Customizable**: Can be trained to adapt to specific domain paper formats
- **Multi-language Support**: Supports academic papers in multiple languages
- **REST API**: Provides RESTful API interface for easy integration into other applications

### Installation and Usage

#### Method 1: Using Docker (Recommended)

```bash
# Pull GROBID Docker image
docker pull lfoppiano/grobid:0.7.3

# Start GROBID service
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.3
```

#### Method 2: Build from Source

```bash
# Clone GROBID repository
git clone https://github.com/kermitt2/grobid.git

# Enter directory
cd grobid

# Build project
./gradlew clean install

# Start service
./gradlew run
```

### API Usage Examples

#### Python Call Example

```python
import requests
import json

# GROBID service address
GROBID_URL = "http://localhost:8070/api"

# Parse PDF paper
def parse_paper(pdf_path):
    with open(pdf_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(
            f"{GROBID_URL}/processFulltextDocument",
            files=files,
            data={
                'consolidateHeader': '1',
                'consolidateCitations': '1',
                'includeRawCitations': '1',
                'includeRawAffiliations': '1'
            }
        )
    return response.text

# Parse metadata
def parse_metadata(pdf_path):
    with open(pdf_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(
            f"{GROBID_URL}/processHeaderDocument",
            files=files
        )
    return response.text
```

### Integration with LangChain

```python
from langchain.document_loaders import GrobidLoader

# Load paper using GrobidLoader
def load_paper_with_grobid(pdf_path):
    loader = GrobidLoader(
        grobid_url="http://localhost:8070/api",
        pdf_path=pdf_path,
        chunk_size=1000,
        chunk_overlap=100
    )
    documents = loader.load()
    return documents
```

---

## Streamlit 🚀

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

### Key Features

- **Rapid Prototyping**: Turn data scripts into shareable web apps in minutes
- **Pure Python**: Write apps entirely in Python, no frontend experience required
- **Live Reload**: Automatically update the app as you edit the code
- **Interactive Widgets**: Built-in support for sliders, buttons, text inputs, and more
- **Data Display**: Easy integration with pandas, matplotlib, plotly, and other data libraries
- **Caching**: Built-in caching mechanism for improved performance
- **Deployment**: Easy deployment to Streamlit Cloud or other platforms

### Installation

```bash
# Install Streamlit
pip install streamlit

# Or using uv
uv add streamlit
```

### Basic Usage

```python
import streamlit as st
import pandas as pd

# Set page title
st.title("Paper Assistant Agent")

# Add sidebar
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Select Model", ["GPT-4", "Claude", "DeepSeek"])

# Main content
st.header("Upload Paper")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # Display paper content
    st.subheader("Paper Content")
    st.text_area("Extracted Text", "Paper content will appear here...", height=300)
    
    # Q&A section
    st.subheader("Ask Questions")
    question = st.text_input("Enter your question about the paper")
    if st.button("Get Answer"):
        st.info("Answer will be generated here...")
```

### Running the App

```bash
# Run Streamlit app
streamlit run app.py

# The app will be available at http://localhost:8501
```

### Advanced Features

#### Session State

```python
import streamlit as st

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Add message to chat history
def add_message(role, content):
    st.session_state.chat_history.append({"role": role, "content": content})

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])
```

#### Caching

```python
import streamlit as st

@st.cache_data
def load_and_process_paper(pdf_path):
    """Cache the paper loading and processing"""
    # Expensive operation
    return processed_data

@st.cache_resource
def load_model():
    """Cache the model loading"""
    return model
```

#### Custom Components

```python
import streamlit as st
from streamlit.components.v1 import html

# Add custom HTML/CSS
html("""
<style>
.custom-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
}
</style>
<div class="custom-box">
    <h3>Custom Component</h3>
    <p>This is a custom HTML component</p>
</div>
""")
```

### Integration with LangChain

```python
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Initialize components
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# Streamlit interface
st.title("Paper Q&A Assistant")

# Chat interface
if prompt := st.chat_input("Ask about the paper"):
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        response = qa_chain({"question": prompt})
        st.write(response["answer"])
```

### Application Scenarios

- **Paper Analysis Dashboard**: Visualize paper statistics and insights
- **Interactive Q&A Interface**: Build conversational interfaces for paper Q&A
- **Data Visualization**: Display charts and graphs from paper data
- **Collaborative Tools**: Share paper analysis tools with team members
- **Prototype Deployment**: Quickly deploy ML models for paper processing

### Performance Optimization

- **Use Caching**: Cache expensive operations like model loading and data processing
- **Lazy Loading**: Load data and models only when needed
- **Pagination**: For large datasets, implement pagination
- **Async Operations**: Use async functions for I/O operations
- **Resource Management**: Properly manage memory and compute resources

---

## Chroma 🗄️

Chroma is an open-source embedding database designed for AI applications. It provides efficient storage and retrieval of vector embeddings, making it ideal for building semantic search and retrieval-augmented generation (RAG) systems.

### Key Features

- **Vector Storage**: Store and manage high-dimensional vector embeddings
- **Semantic Search**: Perform similarity search using vector embeddings
- **Metadata Support**: Store and filter documents with associated metadata
- **Multiple Distance Functions**: Support for cosine similarity, Euclidean distance, and more
- **Persistent Storage**: Save data to disk for persistence across sessions
- **Easy Integration**: Simple API for adding, querying, and managing documents
- **LangChain Compatible**: Native integration with LangChain framework

### Installation

```bash
# Install Chroma
pip install chromadb

# Or using uv
uv add chromadb
```

### Basic Usage

```python
import chromadb
from chromadb.config import Settings

# Create a client
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

# Create or get a collection
collection = client.create_collection(name="papers")

# Add documents
collection.add(
    documents=["Paper 1 content", "Paper 2 content"],
    metadatas=[{"title": "Paper 1"}, {"title": "Paper 2"}],
    ids=["id1", "id2"]
)

# Query documents
results = collection.query(
    query_texts=["What is machine learning?"],
    n_results=2
)
```

### Integration with LangChain

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Query the vector store
results = vectorstore.similarity_search("What is the main contribution?", k=3)
```

### Advanced Features

#### Persistent Storage

```python
import chromadb
from chromadb.config import Settings

# Create persistent client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection with persistence
collection = client.create_collection(name="papers")

# Data will be automatically saved to disk
```

#### Metadata Filtering

```python
# Query with metadata filter
results = collection.query(
    query_texts=["machine learning"],
    where={"category": "AI"},
    n_results=5
)

# Complex filters
results = collection.query(
    query_texts=["neural networks"],
    where={
        "$and": [
            {"year": {"$gte": 2020}},
            {"category": "deep learning"}
        ]
    },
    n_results=5
)
```

#### Custom Embeddings

```python
from chromadb.utils import embedding_functions

# Use custom embedding function
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.create_collection(
    name="papers",
    embedding_function=sentence_transformer_ef
)
```

### Application Scenarios

- **Document Retrieval**: Build semantic search for academic papers
- **Q&A Systems**: Power retrieval-augmented generation for paper Q&A
- **Similarity Matching**: Find similar papers based on content
- **Recommendation Systems**: Recommend related papers to users
- **Knowledge Management**: Organize and search large paper collections

### Performance Optimization

- **Batch Processing**: Add documents in batches for better performance
- **Indexing**: Use appropriate indexing strategies for large datasets
- **Embedding Caching**: Cache embeddings to avoid recomputation
- **Query Optimization**: Use metadata filters to reduce search space
- **Resource Management**: Monitor memory usage for large collections

---

## Docker Sandbox 🐳

Docker Sandbox provides isolated, secure environments for running applications and executing code. In the context of paper assistant agents, Docker sandbox is particularly useful for safely executing AI-generated code and managing dependencies.

### Key Features

- **Process Isolation**: Run applications in isolated containers separate from the host system
- **Security**: Prevent malicious or buggy code from affecting the host system
- **Dependency Management**: Package all dependencies within the container
- **Reproducibility**: Ensure consistent environments across different systems
- **Resource Control**: Limit CPU, memory, and network usage for containers
- **Easy Deployment**: Deploy applications with all dependencies included

### Use Cases in Paper Assistant Agents

#### 1. Safe Code Execution

When AI agents generate code (e.g., data analysis scripts, visualization code), running it in a Docker sandbox ensures safety:

```dockerfile
# Dockerfile for code execution sandbox
FROM python:3.11-slim

# Create non-root user for security
RUN useradd -m -u 1000 sandbox

# Set working directory
WORKDIR /app

# Install common data science libraries
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    scipy \
    sympy

# Switch to non-root user
USER sandbox

# Default command
CMD ["python"]
```

```bash
# Build the sandbox image
docker build -t code-sandbox .

# Run code in sandbox with resource limits
docker run --rm \
  --memory="512m" \
  --cpus="1.0" \
  --network=none \
  --read-only \
  -v "$(pwd)/code:/app/code:ro" \
  code-sandbox python /app/code/script.py
```

#### 2. GROBID Service Containerization

```dockerfile
# Dockerfile for GROBID service
FROM lfoppiano/grobid:0.7.3

# Expose GROBID port
EXPOSE 8070

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8070/api/isalive || exit 1
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  grobid:
    build: .
    ports:
      - "8070:8070"
    volumes:
      - grobid_data:/opt/grobid/data
    restart: unless-stopped
    
  paper-agent:
    build: ./agent
    depends_on:
      - grobid
      - chroma
    environment:
      - GROBID_URL=http://grobid:8070
      - CHROMA_URL=http://chroma:8000
      
  chroma:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
    volumes:
      - chroma_data:/chroma/chroma
      
volumes:
  grobid_data:
  chroma_data:
```

#### 3. Isolated Environment for Each User

```python
import docker
import uuid

class DockerSandbox:
    def __init__(self):
        self.client = docker.from_env()
    
    def create_sandbox(self, user_id: str):
        """Create an isolated sandbox for a user"""
        container_name = f"sandbox-{user_id}-{uuid.uuid4().hex[:8]}"
        
        container = self.client.containers.run(
            "code-sandbox",
            name=container_name,
            detach=True,
            mem_limit="512m",
            cpu_quota=50000,  # 50% of CPU
            network_mode="none",  # No network access
            read_only=True,
            tmpfs={"/tmp": "rw,noexec,nosuid,size=100m"},
            labels={"user_id": user_id, "type": "sandbox"}
        )
        return container
    
    def execute_code(self, container_id: str, code: str):
        """Execute code in the sandbox"""
        container = self.client.containers.get(container_id)
        
        # Write code to temporary file
        exec_result = container.exec_run(
            cmd=["python", "-c", code],
            timeout=30  # 30 second timeout
        )
        
        return {
            "exit_code": exec_result.exit_code,
            "output": exec_result.output.decode("utf-8"),
            "success": exec_result.exit_code == 0
        }
    
    def cleanup(self, container_id: str):
        """Remove sandbox container"""
        container = self.client.containers.get(container_id)
        container.stop()
        container.remove()
```

### Security Best Practices

#### 1. Non-Root User

Always run containers as non-root users:

```dockerfile
FROM python:3.11-slim

# Create non-root user
RUN groupadd -r sandbox && useradd -r -g sandbox sandbox

# Set permissions
WORKDIR /app
RUN chown -R sandbox:sandbox /app

# Switch to non-root user
USER sandbox
```

#### 2. Resource Limits

```bash
# Memory limit
docker run --memory="512m" --memory-swap="512m" image

# CPU limit
docker run --cpus="0.5" image

# Disk I/O limit
docker run --device-read-bps /dev/sda:1mb image
```

#### 3. Network Isolation

```bash
# No network access
docker run --network=none image

# Custom isolated network
docker network create isolated_network
docker run --network=isolated_network image
```

#### 4. Read-Only Filesystem

```bash
# Read-only root filesystem
docker run --read-only image

# Writable temporary directory
docker run --read-only --tmpfs /tmp:rw,noexec,nosuid,size=100m image
```

### Integration with Paper Assistant Agent

```python
from typing import Optional
import docker

class SafeCodeExecutor:
    """Safely execute AI-generated code using Docker sandbox"""
    
    def __init__(self):
        self.client = docker.from_env()
        self.sandbox_image = "paper-agent-sandbox"
    
    def execute_analysis_code(
        self,
        code: str,
        paper_data: dict,
        timeout: int = 60
    ) -> dict:
        """
        Execute analysis code in sandbox environment
        
        Args:
            code: Python code to execute
            paper_data: Paper data for analysis
            timeout: Maximum execution time in seconds
            
        Returns:
            Execution results including output and any errors
        """
        # Create temporary container
        container = self.client.containers.run(
            self.sandbox_image,
            command=["python", "-c", code],
            environment={"PAPER_DATA": json.dumps(paper_data)},
            detach=True,
            mem_limit="1g",
            cpu_quota=100000,
            network_mode="none",
            read_only=True,
            tmpfs={"/tmp": "rw,noexec,nosuid,size=500m"}
        )
        
        try:
            # Wait for execution with timeout
            result = container.wait(timeout=timeout)
            logs = container.logs().decode("utf-8")
            
            return {
                "success": result["StatusCode"] == 0,
                "exit_code": result["StatusCode"],
                "output": logs,
                "error": None if result["StatusCode"] == 0 else "Execution failed"
            }
        except Exception as e:
            return {
                "success": False,
                "exit_code": -1,
                "output": "",
                "error": str(e)
            }
        finally:
            # Cleanup
            container.stop()
            container.remove()
```

### Application Scenarios

- **Safe Code Execution**: Run AI-generated analysis code without security risks
- **Multi-tenant Isolation**: Provide isolated environments for different users
- **Dependency Management**: Package all required libraries in containers
- **Reproducible Research**: Ensure analysis results are reproducible across environments
- **Resource Management**: Control resource usage for computationally intensive tasks
- **Testing Environment**: Test agent behavior in isolated, controlled conditions

### Performance Optimization

- **Image Size**: Use slim base images and multi-stage builds to reduce image size
- **Layer Caching**: Optimize Dockerfile layer order for better caching
- **Volume Mounts**: Use volumes for data that needs to persist
- **Container Reuse**: Keep containers warm for faster execution
- **Resource Monitoring**: Monitor container resource usage and adjust limits

---

## Development Workflow

1. **Environment Setup**: Install GROBID service, Streamlit, and configure Docker
2. **Data Preparation**: Collect PDF papers to be processed
3. **Backend Development**: Use GROBID to parse papers and extract structured data
4. **Vector Store Setup**: Configure Chroma for document storage and retrieval
5. **Frontend Development**: Build interactive UI with Streamlit
6. **Sandbox Configuration**: Set up Docker sandbox for safe code execution
7. **Integration**: Connect all components (GROBID, Chroma, Streamlit, Docker)
8. **Testing and Verification**: Verify parsing accuracy, UI functionality, and sandbox security
9. **Deployment**: Deploy paper assistant agent service with Docker Compose

---

## Resource Links

### GROBID
- **GROBID Official Website**: [https://grobid.readthedocs.io/](https://grobid.readthedocs.io/)
- **GROBID GitHub Repository**: [https://github.com/kermitt2/grobid](https://github.com/kermitt2/grobid)
- **LangChain GrobidLoader Documentation**: [https://python.langchain.com/docs/integrations/document_loaders/grobid](https://python.langchain.com/docs/integrations/document_loaders/grobid)

### Streamlit
- **Streamlit Official Website**: [https://streamlit.io/](https://streamlit.io/)
- **Streamlit Documentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Streamlit Gallery**: [https://streamlit.io/gallery](https://streamlit.io/gallery)
- **Streamlit Cloud**: [https://streamlit.io/cloud](https://streamlit.io/cloud)

### Chroma
- **Chroma Official Website**: [https://www.trychroma.com/](https://www.trychroma.com/)
- **Chroma Documentation**: [https://docs.trychroma.com/](https://docs.trychroma.com/)
- **Chroma GitHub Repository**: [https://github.com/chroma-core/chroma](https://github.com/chroma-core/chroma)
- **LangChain Chroma Integration**: [https://python.langchain.com/docs/integrations/vectorstores/chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma)

### Docker
- **Docker Official Website**: [https://www.docker.com/](https://www.docker.com/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Docker Hub**: [https://hub.docker.com/](https://hub.docker.com/)
- **Docker Security Best Practices**: [https://docs.docker.com/develop/security-best-practices/](https://docs.docker.com/develop/security-best-practices/)

---

*Use these powerful tools to build intelligent paper assistant agents!* 🎉