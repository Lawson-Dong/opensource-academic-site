# Windows PowerShell Git Common Commands 📝

This document records commonly used Git commands in Windows PowerShell for version control and code management.

## Git First Commit Steps - Complete Push Process

### 1. Enter Project Directory

```powershell
cd "D:\AI application experience\Agent_paper_explainer"
```

### 2. Initialize Git Repository (if not already initialized)

```powershell
git init
```

### 3. Add All Files

```powershell
git add .
```

### 4. Commit Files

```powershell
git commit -m "First commit: Agent paper explainer"
```

### 5. Add Remote Repository (Link to GitHub)

```powershell
git remote add origin git@github.com:Lawson-Dong/Agent_paper_explainer.git
```

### 6. Check Branch Name Before Pushing

```powershell
git branch
```

### 7. Push to GitHub

If the branch shows as main:

```powershell
git push -u origin main
```

If the branch shows as master:

```powershell
git push -u origin master
```

### If Remote Repository Already Exists

You can first check the existing remote repository:

```powershell
git remote -v
```

If origin already exists, you can remove it first and then add:

```powershell
git remote remove origin
git remote add origin git@github.com:Lawson-Dong/Agent_paper_explainer.git
```

### If Push Fails and Prompts to Pull First

```powershell
# If remote repository has content (e.g., has README), pull and merge first
git pull origin main --allow-unrelated-histories

# After resolving any conflicts, push again
git push -u origin main
```

### Verify Push Success

After successful push, visit the following address to view:

```
https://github.com/Lawson-Dong/Agent_paper_explainer
```

## Basic Commands

```bash
# Check Git version
git --version

# Check Git configuration
git config --list

# Check user configuration
git config user.name
git config user.email

# Set user information
git config --global user.name "Your Username"
git config --global user.email "Your Email"
```

## Repository Operations

```bash
# Initialize repository
git init

# Clone remote repository
git clone https://github.com/username/repository.git

# Check repository status
git status

# Check remote repository
git remote -v

# Add remote repository
git remote add origin https://github.com/username/repository.git

# Remove remote repository
git remote remove origin

# Modify remote repository address
git remote set-url origin https://github.com/username/new-repository.git
```

## File Operations

```bash
# Add all files
git add .

# Add specific file
git add filename

# Add specific directory
git add directoryname/

# Check files not added
git add -n .

# Check files already added
git diff --cached
```

## Commit Operations

```bash
# Commit changes
git commit -m "Commit message"

# Add and commit
git commit -am "Commit message"

# Amend last commit
git commit --amend

# View commit history
git log

# View concise commit history
git log --oneline

# View graphical commit history
git log --graph --oneline
```

## Branch Operations

```bash
# View all branches
git branch

# View remote branches
git branch -r

# View all branches (including remote)
git branch -a

# Create new branch
git branch branchname

# Switch branch
git checkout branchname

# Create and switch to new branch
git checkout -b branchname

# Delete local branch
git branch -d branchname

# Delete remote branch
git push origin --delete branchname

# Merge branch
git merge branchname
```

## Push and Pull

```bash
# Push to remote repository
git push

# Push to specific branch
git push origin branchname

# First push (set upstream branch)
git push -u origin branchname

# Force push (use with caution)
git push -f

# Pull remote updates
git pull

# Pull specific branch
git pull origin branchname

# Get remote updates (without merging)
git fetch

# Get updates for specific branch
git fetch origin branchname
```

## Undo Operations

```bash
# Undo working directory modifications
git checkout -- filename

# Undo staging area modifications
git reset HEAD filename

# Undo last commit (keep modifications)
git reset --soft HEAD~1

# Undo last commit (discard modifications)
git reset --hard HEAD~1

# Revert to specific commit
git reset --hard commithash

# View operation history
git reflog

# Restore to specific state
git reset --hard HEAD@{n}
```

## Tag Operations

```bash
# Create tag
git tag tagname

# Create annotated tag
git tag -a tagname -m "Tag description"

# View all tags
git tag

# View tag details
git show tagname

# Push tag to remote
git push origin tagname

# Push all tags to remote
git push origin --tags

# Delete local tag
git tag -d tagname

# Delete remote tag
git push origin --delete tag tagname
```

## View Differences

```bash
# View differences between working directory and staging area
git diff

# View differences between staging area and last commit
git diff --cached

# View differences between working directory and last commit
git diff HEAD

# View differences between two commits
git diff commit1 commit2

# View differences for specific file
git diff filename
```

## Stash Operations

```bash
# Stash current work
git stash

# Stash with description
git stash save "Stash description"

# View stash list
git stash list

# Apply most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{n}

# Drop stash
git stash drop stash@{n}

# Clear all stashes
git stash clear
```

## Common Combined Commands

```bash
# Complete commit process
git add .
git commit -m "Commit message"
git push

# Quick status check
git status -s

# View recent commits
git log -3 --oneline

# View file modification history
git log --follow filename

# View file content in specific commit
git show commithash:filename

# View detailed information for specific commit
git show commithash

# View current branch
git rev-parse --abbrev-ref HEAD

# View remote repository address
git config --get remote.origin.url
```

## PowerShell Specific Tips

```bash
# When using Git commands in PowerShell, if path contains spaces, enclose in quotes
cd "D:\AI application experience\vibe coding\Github Static Personal Website"

# View current directory
Get-Location

# List files in current directory
Get-ChildItem

# Check Git status in PowerShell
git status

# Use PowerShell aliases
# git status can be abbreviated as git st (if configured)
# git checkout can be abbreviated as git co (if configured)
```

## Common Issue Resolution

### 1. PowerShell Execution Policy Restriction

```bash
# View current execution policy
Get-ExecutionPolicy

# Temporarily modify execution policy (current session only)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Permanently modify execution policy (requires administrator privileges)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 2. Push Failure

```bash
# When push fails, pull updates first
git pull

# Resolve conflicts and push again
git add .
git commit -m "Resolve conflicts"
git push
```

### 3. Remote Repository Already Exists

```bash
# View current remote repository
git remote -v

# Remove old remote repository
git remote remove origin

# Add new remote repository
git remote add origin https://github.com/username/repository.git
```

## Learning Resources

- **Git Official Documentation**: [https://git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Help**: [https://docs.github.com/en](https://docs.github.com/en)
- **Git Cheat Sheet**: [https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---

*Master these Git commands to make version control more efficient!* 🚀