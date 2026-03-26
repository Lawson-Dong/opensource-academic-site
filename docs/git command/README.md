# Windows PowerShell的Git常用命令 📝

本文件记录了Windows PowerShell中常用的Git命令，用于版本控制和代码管理。

## 基础命令

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

## 仓库操作

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

## 文件操作

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

## 提交操作

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

## 分支操作

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

## 推送和拉取

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

## 撤销操作

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

## 标签操作

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

## 查看差异

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

## 储藏操作

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

## 常用组合命令

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

## PowerShell特定技巧

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

## 常见问题解决

### 1. PowerShell执行策略限制

```bash
# 查看当前执行策略
Get-ExecutionPolicy

# 临时修改执行策略（仅当前会话）
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 永久修改执行策略（需要管理员权限）
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 2. 推送失败

```bash
# 推送失败时，先拉取更新
git pull

# 解决冲突后再推送
git add .
git commit -m "解决冲突"
git push
```

### 3. 远程仓库已存在

```bash
# 查看当前远程仓库
git remote -v

# 删除旧的远程仓库
git remote remove origin

# 添加新的远程仓库
git remote add origin https://github.com/用户名/仓库名.git
```

## 学习资源

- **Git官方文档**：[https://git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Help**：[https://docs.github.com/en](https://docs.github.com/en)
- **Git Cheat Sheet**：[https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---

*掌握这些Git命令，让版本控制变得更加高效！* 🚀