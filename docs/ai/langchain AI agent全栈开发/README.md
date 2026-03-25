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