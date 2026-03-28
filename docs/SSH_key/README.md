# GitHub SSH Key Configuration Guide 🔐

This guide introduces scenarios and detailed steps for configuring SSH keys on GitHub, including situations where VPN is needed.

## Scenarios for Configuring SSH Keys

### 1. Basic Scenarios

- **Git Command Line**: Interact with GitHub repositories via SSH protocol without entering username and password each time
- **Automation Scripts**: Use SSH keys for authentication in CI/CD pipelines, automated deployments, etc.
- **Multi-Device Management**: Use different SSH keys on multiple devices to access the same GitHub account
- **Team Collaboration**: Use SSH keys for secure code push and pull operations within teams

### 2. Scenarios Requiring VPN

- **Network Restrictions**: When the local network has restrictions on GitHub access
- **Access Speed**: When direct access to GitHub is slow
- **Stability**: When network connection is unstable, using VPN can improve connection stability

## Operation Steps

### 1. Generate SSH Key Pair

#### Generate in Windows PowerShell

```bash
# Open PowerShell
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_github_email@example.com"

# Press Enter to use default settings (you can skip setting a password)
# After generation, there will be two files:
# ~/.ssh/id_rsa - Private key (keep locally, never share)
# ~/.ssh/id_rsa.pub - Public key (upload to GitHub)
```

#### Generate in Git Bash

```bash
# Open Git Bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_github_email@example.com"

# Press Enter to use default settings (you can skip setting a password)
```

### 2. View and Copy Public Key

#### View in Windows PowerShell

```bash
# View public key content
cat ~/.ssh/id_rsa.pub

# Or open with Notepad
notepad ~/.ssh/id_rsa.pub
```

#### View in Git Bash

```bash
# View public key content
cat ~/.ssh/id_rsa.pub
```

### 3. Add Public Key to GitHub

1. Log in to GitHub
2. Click on your profile picture in the top right → Settings
3. Left sidebar → SSH and GPG keys
4. Click New SSH key
5. Fill in:
   - Title: Device name (e.g., My PC, Laptop)
   - Key: Paste the copied public key
6. Click Add SSH key

### 4. Test SSH Connection

#### Basic Test

```bash
# Run in PowerShell or Git Bash
ssh -T git@github.com

# If successful, you will see:
# Hi username! You've successfully authenticated...
```

#### Test When Using VPN

1. **Start VPN**: Ensure VPN is connected and working properly
2. **Test Connection**: Run the above command to test SSH connection
3. **Check Network**: If connection fails, check VPN settings and network connection

### 5. Configure Git to Use SSH

#### Change Repository Address to SSH

```bash
# View current remote address
git remote -v

# Remove HTTPS address
git remote remove origin

# Add SSH address
git remote add origin git@github.com:username/repository.git

# Confirm the change
git remote -v
```

#### Use SSH Directly When Cloning Repository

```bash
# Clone repository using SSH address
git clone git@github.com:username/repository.git
```

## Considerations When Using VPN

### 1. VPN Settings

- **Choose Appropriate VPN Server**: Select a server with low latency and high stability
- **Protocol Selection**: Prioritize secure protocols like OpenVPN or WireGuard
- **Port Settings**: Ensure the SSH port (default 22) is not blocked by VPN

### 2. SSH Configuration

#### Configure SSH Proxy

If VPN requires using a proxy, you can set it in the SSH configuration file:

```bash
# Edit SSH configuration file
notepad ~/.ssh/config
```

Add the following content:

```
Host github.com
  User git
  Hostname github.com
  IdentityFile ~/.ssh/id_rsa
  ProxyCommand connect-proxy -S 127.0.0.1:7890 %h %p
```

**Explanation**:
- `ProxyCommand`: Specifies the proxy command
- `connect-proxy`: Requires installing connect-proxy tool
- `127.0.0.1:7890`: Proxy server address and port

### 3. Troubleshooting

#### Connection Timeout

```bash
# Check network connection
ping github.com

# Check SSH connection
ssh -vT git@github.com

# Check VPN connection status
# Ensure VPN is working properly
```

#### Permission Denied

```bash
# Check private key permissions
chmod 600 ~/.ssh/id_rsa

# Check if public key is correctly added to GitHub
# Regenerate key pair and re-add
```

## Multiple Key Management

### 1. Generate Multiple SSH Key Pairs

```bash
# Generate second SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_github_email@example.com" -f ~/.ssh/id_rsa_work

# Generate third SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_github_email@example.com" -f ~/.ssh/id_rsa_personal
```

### 2. Configure SSH Config File

```bash
# Edit SSH configuration file
notepad ~/.ssh/config
```

Add the following content:

```
# Personal GitHub account
Host github.com-personal
  User git
  Hostname github.com
  IdentityFile ~/.ssh/id_rsa_personal

# Work GitHub account
Host github.com-work
  User git
  Hostname github.com
  IdentityFile ~/.ssh/id_rsa_work
```

### 3. Use Different Keys to Access Different Repositories

```bash
# Clone personal repository
git clone git@github.com-personal:username/personal-repo.git

# Clone work repository
git clone git@github.com-work:companyname/work-repo.git
```

## Security Best Practices

1. **Protect Private Keys**: Set private key file permissions to 600, never share with others
2. **Regular Key Updates**: Generate new SSH key pairs every 6-12 months
3. **Use Passphrases**: Set passphrases for SSH keys to increase security
4. **Delete Unused Keys**: Regularly clean up unused SSH keys on GitHub
5. **Use SSH Agent**: Use SSH agent to manage keys and avoid repeatedly entering passphrases

## Common Issues

### 1. SSH Key Lost

```bash
# Regenerate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_github_email@example.com"

# Add new public key to GitHub
# Update remote address of local repository
```

### 2. Unable to Push Code

```bash
# Check SSH connection
ssh -T git@github.com

# Check remote address
git remote -v

# Check branch permissions
# Ensure you have push permissions
```

### 3. Slow SSH Speed After VPN Connection

```bash
# Choose a closer VPN server
# Check network bandwidth
# Try using different VPN protocols
```

## Learning Resources

- **GitHub Official Documentation**: [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- **SSH Official Documentation**: [OpenSSH Documentation](https://www.openssh.com/docs/)
- **Git Official Documentation**: [Git on the Server - Generating Your SSH Public Key](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

---

*Configure SSH keys properly and enjoy a more secure and convenient GitHub experience!* 🚀