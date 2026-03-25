# PyTorch代码示例

> 发布时间：2026-03-25
> 主题：PyTorch

本文展示如何使用PyTorch定义和训练一个简单的神经网络。

## 基本神经网络

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 定义简单的神经网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 初始化模型、损失函数和优化器
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
```

## 代码解析

1. **导入库**：导入PyTorch的核心库和模块。

2. **定义网络结构**：创建一个继承自`nn.Module`的`Net`类，定义网络的层和前向传播函数。
   - `__init__`方法：初始化网络层，这里定义了两个全连接层。
   - `forward`方法：定义前向传播过程，包括数据扁平化、激活函数和输出。

3. **初始化模型**：创建`Net`类的实例。

4. **定义损失函数**：使用交叉熵损失函数，适用于分类任务。

5. **定义优化器**：使用随机梯度下降（SGD）优化器，设置学习率和动量。

## 训练模型

以下是训练模型的代码示例：

```python
# 训练模型
def train(model, train_loader, criterion, optimizer, epochs=5):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            # 清零梯度
            optimizer.zero_grad()
            
            # 前向传播
            outputs = model(inputs)
            
            # 计算损失
            loss = criterion(outputs, labels)
            
            # 反向传播
            loss.backward()
            
            # 更新参数
            optimizer.step()
            
            # 统计损失
            running_loss += loss.item()
            if i % 100 == 99:
                print(f'[Epoch {epoch + 1}, Batch {i + 1}] Loss: {running_loss / 100:.3f}')
                running_loss = 0.0

# 测试模型
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f'Accuracy: {100 * correct / total:.2f}%')
```

## 数据加载

使用PyTorch的`DataLoader`加载数据：

```python
import torchvision
import torchvision.transforms as transforms

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 加载训练数据
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# 加载测试数据
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
```

## 完整训练流程

将所有代码组合起来：

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 加载数据
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# 定义网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 初始化模型、损失函数和优化器
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 训练模型
def train(model, train_loader, criterion, optimizer, epochs=5):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            if i % 100 == 99:
                print(f'[Epoch {epoch + 1}, Batch {i + 1}] Loss: {running_loss / 100:.3f}')
                running_loss = 0.0

# 测试模型
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f'Accuracy: {100 * correct / total:.2f}%')

# 运行训练和测试
train(model, trainloader, criterion, optimizer, epochs=5)
test(model, testloader)
```

## 保存和加载模型

```python
# 保存模型
torch.save(model.state_dict(), 'model.pth')

# 加载模型
model = Net()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

## 总结

PyTorch是一个功能强大的深度学习框架，它提供了灵活的张量操作和自动微分功能，使得构建和训练神经网络变得更加容易。通过本文的示例，我们学习了如何使用PyTorch定义一个简单的神经网络，如何加载数据，如何训练和测试模型，以及如何保存和加载模型。

PyTorch的设计理念是"从研究到生产"，它既适合研究人员快速原型设计，也适合在生产环境中部署模型。随着深度学习的不断发展，PyTorch也在不断更新和改进，为用户提供更多强大的功能和工具。