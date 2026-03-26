# 技术学习日记 📚

这里记录了我的技术栈学习历程，采用Google Colab风格展示代码和文字内容。

## 目录

- [2026年2月24日](#2026年2月24日)
- [2026年2月25日](#2026年2月25日)
- [2026年3月26日](#2026年3月26日)

## 2026年2月24日 📅

### 🚀 项目初始化与Git配置

今天开始了个人学术网站的搭建，使用Trae Vibe Coding创建了初版，但需要进行调试。

#### 调试路径

1. **创建虚拟本地服务器在本地调试**
2. **使用Git存档并同步代码到GitHub**（长期方案）

#### Git初次上传步骤

```bash
# 1. 切换到项目目录
cd "D:\AI application experience\vibe coding\Github静态个人网站"

# 2. 确认当前位置
pwd

# 3. 查看项目内容确认项目文件存在
dir

# 4. 初始化git仓库
# （1）初始化
git init
# （2）查看状态
git status

# 5. 添加并提交项目文件
# （1）添加所有文件
git add .
# （2）提交
git commit -m "Initial commit: 个人学术网站"

# 6. 关联远程仓库并推送
# （1）添加远程仓库
git remote add origin https://github.com/Lawson-Dong/opensource-academic-site.git
# （2）确认远程仓库配置
git remote -v
# （3）推送到 GitHub（首次推送）
git push -u origin main
```

#### 更换远程仓库步骤

```bash
# 1. 切换到项目目录
cd "D:\AI application experience\vibe coding\Github静态个人网站"

# 2. 查看当前的远程
git remote -v

# 3. 删除旧的远程仓库关联
git remote remove origin

# 4. 确认新的远程仓库配置
git remote -v
```

### 💡 技术概念

**IDE (Integrated Development Environment)** - 集成开发环境，如VSCode是当下最热门的IDE，集成了许多语言、环境和插件。

## 2026年2月25日 📅

### 🔐 SSH配置

今天主要配置了SSH密钥，用于Git与GitHub之间的安全通信。

#### SSH配置工作流

本地电脑 (项目) ←→ GitHub (远程仓库)
↓                                  ↓
SSH 密钥认证    SSH 密钥验证
↓                                  ↓
推送代码 (git push)     接收代码
拉取代码 (git pull)       存储代码

#### 1. 生成 SSH 密钥对

```bash
# 在 Git Bash 或 PowerShell 中运行
ssh-keygen -t rsa -b 4096 -C "你的GitHub邮箱"

# 一路按回车（使用默认路径，可以不设置密码）
# 生成后会有两个文件：
# ~/.ssh/id_rsa - 私钥（留本地，绝不泄露）
# ~/.ssh/id_rsa.pub - 公钥（上传到 GitHub）
```

#### 2. 查看并复制公钥

```bash
# 查看公钥内容
cat ~/.ssh/id_rsa.pub

# 或 Windows 用
notepad ~/.ssh/id_rsa.pub
```

#### 3. 添加公钥到 GitHub

1. 登录 GitHub
2. 点击右上角头像 → Settings
3. 左侧菜单 → SSH and GPG keys
4. 点击 New SSH key
5. 填写：
   - Title：设备名称（如 My PC、Laptop）
   - Key：粘贴刚才复制的公钥
6. 点击 Add SSH key

#### 4. 测试 SSH 连接

```bash
ssh -T git@github.com

# 成功后会显示：
# Hi 用户名! You've successfully authenticated...
```

#### 5. 将仓库地址改为 SSH

```bash
# 查看当前远程地址
git remote -v

# 删除 HTTPS 地址
git remote remove origin

# 添加 SSH 地址
git remote add origin git@github.com:用户名/仓库名.git

# 确认修改成功
git remote -v
```

#### 推送代码到 GitHub 的工作流

```bash
# 1. 你修改了代码后
cd "D:\AI application experience\vibe coding\Github静态个人网站"

# 2. 查看修改了什么（可选）
git status

# 3. 添加并提交
git add .
git commit -m "更新了个人简介"

# 4. 推送到 GitHub
git push
```

## 2026年3月26日 📅

### 🤖 LangChain AI Agent全栈开发

今天深入学习了LangChain AI Agent的全栈开发，包括项目设置、依赖管理、工具开发和互联网访问集成。

#### 1. 项目设置

```bash
# 创建项目文件夹
mkdir langchain_agent_development

# 进入项目目录
cd langchain_agent_development
```

#### 2. 安装uv包管理器

```bash
# 在VSCode的终端中执行以下命令安装uv
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 3. 使用uv管理Python版本

```bash
# 查看uv管理的Python版本
uv python list

# 安装特定Python版本
uv python install 3.12

# 查看当前使用的Python
uv python find
```

#### 4. 初始化项目

```bash
# 初始化项目，创建pyproject.toml
uv init
```

#### 5. 安装依赖包

```bash
# 安装LangChain相关依赖
uv add python-dotenv langchain langchain-deepseek langgraph

# 安装Tavily搜索引擎API（用于让智能体访问互联网）
uv add tavily-python
```

#### 6. 常见问题解决

**项目名称与依赖包重名错误**：

```bash
# 查看pyproject.toml中的项目名称
cat pyproject.toml

# 用VSCode打开编辑
code pyproject.toml

# 换一个名字（例如：langchain-agent-development）

# 确认文件已保存并修改成功
cat pyproject.toml
```

#### 7. 创建环境变量文件

```bash
# 创建.env文件
# 在项目根目录新建.env文件用来关联API key
```

```python
# .env文件内容
DEEPSEEK_API_KEY=sk-xxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxx
```

#### 8. 创建测试文件

```python
# quick_test.py - 测试环境准备
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

#### 9. 创建AI智能体

```python
# agent_langgraph.py - 基于LangGraph的智能体
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tavily import TavilyClient

load_dotenv()

# 初始化模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 初始化Tavily客户端
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# 定义工具
@tool
def calculator(expression: str) -> str:
    """计算数学表达式，例如 '2+3*4'"""
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

@tool
def get_text_length(text: str) -> str:
    """获取文本的字符长度"""
    return f"文本长度: {len(text)} 个字符"

@tool
def reverse_string(text: str) -> str:
    """反转字符串"""
    return f"反转结果: {text[::-1]}"

@tool
def search_internet(query: str) -> str:
    """搜索互联网获取最新信息，例如 '2024年奥运会举办地点'"""
    try:
        response = tavily_client.search(query=query, max_results=3)
        results = response.get('results', [])
        if not results:
            return "未找到相关信息"
        
        # 整理搜索结果
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get('title', '无标题')
            url = result.get('url', '无链接')
            content = result.get('content', '无内容')[:200] + '...' if result.get('content') else '无内容'
            formatted_results.append(f"{i}. {title}\n   链接: {url}\n   内容: {content}")
        
        return "\n".join(formatted_results)
    except Exception as e:
        return f"搜索错误: {str(e)}"

tools = [calculator, get_text_length, reverse_string, search_internet]

# 创建记忆（可选）
memory = MemorySaver()

# 创建智能体（使用 langgraph）
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,  # 添加记忆功能
)

# 主函数
def main():
    print("=" * 50)
    print("LangChain 智能体已启动（LangGraph 版本）！")
    print("输入 'quit' 退出")
    print("=" * 50)
    
    # 配置会话 ID（用于记忆）
    config = {"configurable": {"thread_id": "1"}}
    
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break
        
        try:
            # 调用智能体
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            # 获取最后一条消息（智能体的回复）
            last_message = response["messages"][-1]
            print(f"\n智能体: {last_message.content}")
        except Exception as e:
            print(f"\n错误: {e}")

if __name__ == "__main__":
    main()
```

#### 10. 项目文件结构

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

#### 11. 让智能体访问互联网 - 集成Tavily API

**Tavily API介绍**：
- Tavily是一个专门为AI应用（特别是大型语言模型和AI智能体）设计的搜索引擎API
- 它不是一个给普通用户使用的传统搜索引擎网站，而是一个为开发者提供的后端服务

**集成步骤**：

```bash
# 1. 访问Tavily官网注册账号
# https://tavily.com/

# 2. 在控制台获取API Key

# 3. 在.env文件中添加Tavily API Key
# TAVILY_API_KEY=tvly-xxxxxxxxxxx

# 4. 安装Tavily依赖
uv add tavily-python
```

**功能说明**：
- 集成了Tavily搜索引擎API，使智能体能够访问互联网
- 添加了`search_internet`工具，用于搜索最新信息
- 智能体可以根据用户的问题，自动调用搜索工具获取相关信息
- 搜索结果会被整理并以友好的格式呈现给用户

### 📝 Windows PowerShell的Git常用命令

今天学习了Windows PowerShell中常用的Git命令，用于版本控制和代码管理。

#### 基础命令

```bash
# 查看Git版本
git --version

# 查看Git配置
git config --list

# 查看用户配置
git config user.name
git config user.email

# 设置用户信息
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

#### 仓库操作

```bash
# 初始化仓库
git init

# 克隆远程仓库
git clone https://github.com/用户名/仓库名.git

# 查看仓库状态
git status

# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin https://github.com/用户名/仓库名.git

# 删除远程仓库
git remote remove origin

# 修改远程仓库地址
git remote set-url origin https://github.com/用户名/新仓库名.git
```

#### 文件操作

```bash
# 添加所有文件
git add .

# 添加指定文件
git add 文件名

# 添加指定目录
git add 目录名/

# 查看未添加的文件
git add -n .

# 查看已添加的文件
git diff --cached
```

#### 提交操作

```bash
# 提交更改
git commit -m "提交信息"

# 添加并提交
git commit -am "提交信息"

# 修改最后一次提交
git commit --amend

# 查看提交历史
git log

# 查看简洁的提交历史
git log --oneline

# 查看图形化的提交历史
git log --graph --oneline
```

#### 分支操作

```bash
# 查看所有分支
git branch

# 查看远程分支
git branch -r

# 查看所有分支（包括远程）
git branch -a

# 创建新分支
git branch 分支名

# 切换分支
git checkout 分支名

# 创建并切换到新分支
git checkout -b 分支名

# 删除本地分支
git branch -d 分支名

# 删除远程分支
git push origin --delete 分支名

# 合并分支
git merge 分支名
```

#### 推送和拉取

```bash
# 推送到远程仓库
git push

# 推送到指定分支
git push origin 分支名

# 首次推送（设置上游分支）
git push -u origin 分支名

# 强制推送（谨慎使用）
git push -f

# 拉取远程更新
git pull

# 拉取指定分支
git pull origin 分支名

# 获取远程更新（不合并）
git fetch

# 获取指定分支的更新
git fetch origin 分支名
```

#### 撤销操作

```bash
# 撤销工作区的修改
git checkout -- 文件名

# 撤销暂存区的修改
git reset HEAD 文件名

# 撤销最后一次提交（保留修改）
git reset --soft HEAD~1

# 撤销最后一次提交（不保留修改）
git reset --hard HEAD~1

# 回退到指定提交
git reset --hard 提交哈希值

# 查看操作历史
git reflog

# 恢复到指定状态
git reset --hard HEAD@{n}
```

#### 标签操作

```bash
# 创建标签
git tag 标签名

# 创建带注释的标签
git tag -a 标签名 -m "标签说明"

# 查看所有标签
git tag

# 查看标签详情
git show 标签名

# 推送标签到远程
git push origin 标签名

# 推送所有标签到远程
git push origin --tags

# 删除本地标签
git tag -d 标签名

# 删除远程标签
git push origin --delete tag 标签名
```

#### 查看差异

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最后一次提交的差异
git diff --cached

# 查看工作区与最后一次提交的差异
git diff HEAD

# 查看两个提交之间的差异
git diff 提交1 提交2

# 查看指定文件的差异
git diff 文件名
```

#### 储藏操作

```bash
# 储藏当前工作
git stash

# 储藏并添加说明
git stash save "储藏说明"

# 查看储藏列表
git stash list

# 应用最近的储藏
git stash pop

# 应用指定的储藏
git stash apply stash@{n}

# 删除储藏
git stash drop stash@{n}

# 清空所有储藏
git stash clear
```

#### 常用组合命令

```bash
# 完整的提交流程
git add .
git commit -m "提交信息"
git push

# 快速查看状态
git status -s

# 查看最近的提交
git log -3 --oneline

# 查看文件修改历史
git log --follow 文件名

# 查看文件在某次提交中的内容
git show 提交哈希值:文件名

# 查看某次提交的详细信息
git show 提交哈希值

# 查看当前分支
git rev-parse --abbrev-ref HEAD

# 查看远程仓库地址
git config --get remote.origin.url
```

#### PowerShell特定技巧

```bash
# 在PowerShell中使用Git命令时，如果路径包含空格，需要用引号括起来
cd "D:\AI application experience\vibe coding\Github静态个人网站"

# 查看当前目录
Get-Location

# 列出当前目录的文件
Get-ChildItem

# 在PowerShell中查看Git状态
git status

# 使用PowerShell的别名
# git status 可以缩写为 git st（如果配置了别名）
# git checkout 可以缩写为 git co（如果配置了别名）
```

## 学习计划 🎯

- [x] 初始化Git仓库并关联GitHub
- [x] 配置SSH密钥
- [x] 学习LangChain AI Agent全栈开发
- [x] 学习Windows PowerShell的Git常用命令
- [ ] 完成网站基本结构搭建
- [ ] 学习VuePress的高级配置
- [ ] 部署网站到GitHub Pages

## 学习资源 📖

- **Git**：Git官方文档、GitHub Help
- **SSH**：GitHub SSH设置指南
- **VuePress**：VuePress官方文档
- **LangChain**：[https://www.langchain.com/](https://www.langchain.com/)
- **LangSmith**：[https://smith.langchain.com/](https://smith.langchain.com/)
- **Tavily**：[https://tavily.com/](https://tavily.com/)
- **DeepSeek**：[https://platform.deepseek.com/](https://platform.deepseek.com/)

---

*记录每一天的学习，积累每一点的进步！* 🚀