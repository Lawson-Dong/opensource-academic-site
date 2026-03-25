# 技术学习日记 📚

这里记录了我的技术栈学习历程，采用Google Colab风格展示代码和文字内容。

## 目录

- [2026年2月24日](#2026年2月24日)
- [2026年2月25日](#2026年2月25日)

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

## 学习计划 🎯

- [x] 初始化Git仓库并关联GitHub
- [x] 配置SSH密钥
- [ ] 完成网站基本结构搭建
- [ ] 学习VuePress的高级配置
- [ ] 部署网站到GitHub Pages

## 学习资源 📖

- **Git**：Git官方文档、GitHub Help
- **SSH**：GitHub SSH设置指南
- **VuePress**：VuePress官方文档

---

*记录每一天的学习，积累每一点的进步！* 🚀