# 人工智能体工程：LangChain全栈开发 🤖

本指南介绍如何使用VSCode进行LangChain全栈开发，创建和部署AI Agent。

## 项目设置 📁

### 1. 新建项目文件夹

```bash
# 创建项目文件夹
mkdir langchain_agent_development

# 进入项目目录
cd langchain_agent_development
```

### 2. 在VSCode中打开项目

在VSCode中新建`app.py`文件，作为项目的主入口。

## 安装依赖 🔧

### 1. 安装uv

在VSCode的终端中执行以下命令安装uv：

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 使用uv管理Python版本

uv可以自动下载和管理Python版本，不需要系统预装Python：

```bash
# 查看uv管理的Python版本
uv python list

# 安装特定Python版本
uv python install 3.12

# 查看当前使用的Python
uv python find
```

### 3. 初始化项目

```bash
# 初始化项目，创建pyproject.toml
uv init
```

### 4. 安装依赖包

```bash
uv add python-dotenv langchain langchain-deepseek
```

### 5. 查看已安装的包

```bash
uv pip list
```

## 常见问题解决 🛠️

### 项目名称与依赖包重名

如果在安装依赖时出现以下错误：

```
error: Requirement name `langchain` matches project name `langchain`, but self-dependencies are not permitted without the `--dev` or `--optional` flags. If your project name (`langchain`) is shadowing that of a third-party dependency, consider renaming the project.
```

解决方法：

```bash
# 查看pyproject.toml中的项目名称
cat pyproject.toml

# 用VSCode打开编辑
code pyproject.toml

# 换一个名字（例如：langchain-agent-development）

# 确认文件已保存并修改成功
cat pyproject.toml
```

修改后重新安装依赖：

```bash
uv add python-dotenv langchain langchain-deepseek
```

## 项目文件结构 📁

### 1. 创建agent_langgraph.py

在项目根目录新建`agent_langgraph.py`文件，用于开发agent的功能。

### 2. 创建.env文件

在项目根目录新建`.env`文件用来关联API key：

```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxx
```

API Key获取：
- **DeepSeek**：[https://platform.deepseek.com/](https://platform.deepseek.com/)（token会便宜一点）
- **OpenAI**：[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)（API Key的格式相同）

### 3. AI Agent的API和API Key介绍

**AI Agent的API**是让智能体能够与外部系统、工具或大模型进行标准化交互的接口协议，相当于智能体的“手脚”和“感官”的调用入口。

**API Key**则是用于验证调用者身份、权限和计费凭证的密钥，相当于智能体使用API时的“身份证”和“通行证”。（人工智能时代这玩意属于隐私，跟你身份证号一样，不要随便给别人）

### 4. 创建quick_test.py

在项目根目录新建`quick_test.py`文件，用于运行测试代码，验证API key是否关联好以及agent的状态：

```python
# 测试环境准备
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

# 检查 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("错误：未找到 DEEPSEEK_API_KEY，请在 .env 文件中设置")
    exit(1)

print(f"API Key 已配置: {api_key[:10]}...")

# 测试模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key
)

# 在terminal输出
print("\n测试连接中...")
try:
    response = llm.invoke("你好，请简单介绍一下你自己，一句话即可")
    print(f"\n模型回复: {response.content}")
    print("\n✅ 模型连接成功！")
except Exception as e:
    print(f"\n❌ 连接失败: {e}")
```

## VSCode开发文件架构展示 📁

为了便利，在开发过程中，我们一般会将项目文件夹下的文件按照如下格式整理：

```
langchain/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── main.py                    # 主程序入口
├── tools/                     # 工具包目录
│   ├── __init__.py           # 包初始化文件
│   ├── math_tools.py         # 数学计算工具
│   ├── text_tools.py         # 文本处理工具
│   ├── file_tools.py         # 文件操作工具
│   ├── web_tools.py          # 网络相关工具
│   └── data_tools.py         # 数据处理工具
└── agents/                    # 智能体配置
    ├── __init__.py
    └── my_agent.py           # 智能体定义  
```

### 根目录文件介绍

#### .env - 环境变量配置

```python
# 存储敏感信息和配置
DEEPSEEK_API_KEY=sk-xxxxx
OPENAI_API_KEY=sk-xxxxx
DATABASE_URL=postgresql://localhost/mydb  
```

**作用**：
- 存放 API 密钥、数据库密码等敏感信息
- 不同环境（开发/测试/生产）使用不同配置
- 通过 .gitignore 排除，避免泄露

#### .gitignore - Git 忽略文件

```gitignore
# 虚拟环境
.venv/
venv/

# 环境变量
.env
.env.local

# Python 缓存
__pycache__/
*.pyc

# IDE 配置
.vscode/
.idea/

# 日志和临时文件
*.log
*.tmp
```

**作用**：
- 指定哪些文件不被 Git 追踪
- 防止提交敏感信息、临时文件、依赖包等

#### pyproject.toml - 项目配置文件

```toml
[project]
name = "langchain-tools"
version = "1.0.0"
description = "LangChain 智能体工具集"
requires-python = ">=3.8"
dependencies = [
    "langchain>=0.1.0",
    "langchain-deepseek>=1.0.0",
    "python-dotenv>=1.0.0",
    "langgraph>=0.0.20",
]

[project.scripts]
my-agent = "agents.my_agent:chat"  # 定义命令行入口
```

**作用**：
- 现代 Python 项目的标准配置文件
- 定义项目依赖、元数据、入口点
- 被 uv 和 pip 等工具识别

#### uv.lock - 依赖锁定文件

```python
# 自动生成，不要手动编辑
# 记录所有依赖的精确版本和哈希值
```

**作用**：
- 锁定所有依赖的精确版本
- 确保团队成员和环境使用完全相同的依赖
- 由 uv 自动维护

#### main.py - 主程序入口

```python
# 程序启动文件
from agents.my_agent import chat

if __name__ == "__main__":
    chat()
```

**作用**：
- 程序的统一入口点
- 通常只做启动工作，不包含业务逻辑
- 可以通过 python main.py 运行

## LangChain 平台介绍 📚

LangChain是一个集成了各种agent开发组件的平台，提供了完整的AI Agent开发生态系统。

### 相关链接

- **LangChain官网**：[https://www.langchain.com/](https://www.langchain.com/)
- **LangSmith**：[https://smith.langchain.com/o/4e44cff0-75d9-4635-9e90-cf134ecac629](https://smith.langchain.com/o/4e44cff0-75d9-4635-9e90-cf134ecac629)
  - 部署/开发/调试agent一站式平台
- **LangSmith Fleet**：提供更强大的Agent管理功能

## 开发流程 🚀

1. **项目初始化**：使用uv创建项目和虚拟环境
2. **安装依赖**：添加langchain和相关包
3. **编写代码**：在app.py中实现AI Agent逻辑
4. **测试运行**：验证Agent功能
5. **部署上线**：使用LangSmith部署和监控

## 示例代码 📝

```python
# app.py示例代码
import os
from dotenv import load_dotenv
from langchain_deepseek import DeepSeekLLM

# 加载环境变量
load_dotenv()

# 初始化LLM
llm = DeepSeekLLM(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 测试LLM
response = llm("Hello, LangChain!")
print(response)
```

---

*开始你的LangChain全栈开发之旅吧！* 🎉