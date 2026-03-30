# PyTorch 使用教程 🚀

本教程介绍PyTorch的基本使用方法，包括张量操作、自动求导、构建神经网络，以及训练一个简单的机器学习模型。

## 什么是PyTorch?

PyTorch是一个开源的机器学习框架，由Facebook开发，广泛用于深度学习研究和应用开发。它提供了强大的张量计算和自动求导功能，使深度学习模型的构建和训练变得更加简单。

## 环境搭建

### 安装PyTorch

```bash
# 使用pip安装PyTorch (CPU版本)
pip install torch torchvision torchaudio

# 使用pip安装PyTorch (CUDA 11.8版本)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 使用uv安装
uv add torch torchvision torchaudio
```

### 验证安装

```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # 检查是否支持CUDA
```

## 基本张量操作

### 创建张量

```python
import torch

# 创建标量
scalar = torch.tensor(5.0)
print(f"标量: {scalar}")
print(f"标量形状: {scalar.shape}")

# 创建向量
vector = torch.tensor([1.0, 2.0, 3.0])
print(f"向量: {vector}")
print(f"向量形状: {vector.shape}")

# 创建矩阵
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(f"矩阵: {matrix}")
print(f"矩阵形状: {matrix.shape}")

# 创建3维张量
tensor_3d = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])
print(f"3维张量: {tensor_3d}")
print(f"3维张量形状: {tensor_3d.shape}")

# 创建全零张量
zeros = torch.zeros((2, 3))
print(f"全零张量: {zeros}")

# 创建全一张量
ones = torch.ones((2, 3))
print(f"全一张量: {ones}")

# 创建随机张量
random_tensor = torch.rand((2, 3))
print(f"随机张量: {random_tensor}")
```

### 张量运算

```python
import torch

# 创建两个张量
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# 加法
c = a + b
print(f"a + b: {c}")

# 减法
d = a - b
print(f"a - b: {d}")

# 乘法 (逐元素)
e = a * b
print(f"a * b: {e}")

# 除法
f = a / b
print(f"a / b: {f}")

# 矩阵乘法
g = torch.matmul(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[5], [6]]))
print(f"矩阵乘法: {g}")

# 广播操作
h = torch.tensor([[1.0, 2.0], [3.0, 4.0]]) + torch.tensor([10.0, 20.0])
print(f"广播操作: {h}")
```

## 自动求导

```python
import torch

# 创建需要求导的张量
x = torch.tensor(3.0, requires_grad=True)
y = torch.tensor(5.0, requires_grad=True)

# 定义计算
z = 2 * x + y ** 2
print(f"z = {z}")

# 反向传播
z.backward()

# 查看梯度
print(f"x的梯度: {x.grad}")  # 应输出 2.0
print(f"y的梯度: {y.grad}")  # 应输出 10.0

# 禁用梯度跟踪
with torch.no_grad():
    w = x * y
    print(f"w = {w}")
    print(f"w.requires_grad = {w.requires_grad}")  # 应输出 False
```

## 构建简单的神经网络

### 基本网络结构

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# 创建网络实例
model = SimpleNet(input_size=2, hidden_size=10, output_size=1)
print(model)

# 测试网络
input_tensor = torch.tensor([[1.0, 2.0]])
output = model(input_tensor)
print(f"网络输出: {output}")
```

## 训练一个简单的线性回归模型

### 完整训练代码

```python
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

# 1. 生成模拟数据
np.random.seed(42)
x = np.random.rand(100, 1) * 10
y = 2 * x + 1 + np.random.randn(100, 1) * 0.5

# 转换为PyTorch张量
x_tensor = torch.from_numpy(x).float()
y_tensor = torch.from_numpy(y).float()

# 2. 定义模型
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # 输入维度1，输出维度1
    
    def forward(self, x):
        return self.linear(x)

model = LinearRegression()
print(model)

# 3. 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 4. 训练模型
epochs = 1000
losses = []

for epoch in range(epochs):
    # 前向传播
    outputs = model(x_tensor)
    loss = criterion(outputs, y_tensor)
    
    # 反向传播和优化
    optimizer.zero_grad()  # 清零梯度
    loss.backward()        # 反向传播
    optimizer.step()       # 更新参数
    
    # 记录损失
    losses.append(loss.item())
    
    # 每100个epoch打印一次
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# 5. 评估模型
with torch.no_grad():
    predicted = model(x_tensor).numpy()

print(f'模型参数:')
for name, param in model.named_parameters():
    print(f'{name}: {param.data.item()}')

# 6. 可视化结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='原始数据')
plt.plot(x, predicted, color='red', label='预测直线')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('线性回归')
plt.legend()
plt.show()

# 7. 保存模型
torch.save(model.state_dict(), 'linear_regression_model.pth')
print('模型已保存')

# 8. 加载模型
loaded_model = LinearRegression()
loaded_model.load_state_dict(torch.load('linear_regression_model.pth'))
print('模型已加载')

# 测试加载的模型
with torch.no_grad():
    test_input = torch.tensor([[5.0]])
    test_output = loaded_model(test_input)
    print(f'输入 5.0, 预测输出: {test_output.item()}')
    print(f'真实值应该接近: {2*5 + 1}')
```

## 训练一个简单的分类模型

### 完整训练代码

```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. 生成模拟分类数据
X, y = make_classification(
    n_samples=1000, n_features=20, n_classes=2, 
    n_informative=10, random_state=42
)

# 数据预处理
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 转换为PyTorch张量
X_train_tensor = torch.from_numpy(X_train).float()
y_train_tensor = torch.from_numpy(y_train).long()
X_test_tensor = torch.from_numpy(X_test).float()
y_test_tensor = torch.from_numpy(y_test).long()

# 2. 定义模型
class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = SimpleClassifier(input_size=20, hidden_size=32, output_size=2)
print(model)

# 3. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. 训练模型
epochs = 100
train_losses = []
test_losses = []

for epoch in range(epochs):
    # 训练模式
    model.train()
    
    # 前向传播
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    
    # 反向传播和优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # 记录训练损失
    train_losses.append(loss.item())
    
    # 测试模式
    model.eval()
    with torch.no_grad():
        test_outputs = model(X_test_tensor)
        test_loss = criterion(test_outputs, y_test_tensor)
        test_losses.append(test_loss.item())
    
    # 每10个epoch打印一次
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}')

# 5. 评估模型
model.eval()
with torch.no_grad():
    # 计算训练集准确率
    train_outputs = model(X_train_tensor)
    _, train_preds = torch.max(train_outputs, 1)
    train_accuracy = (train_preds == y_train_tensor).sum().item() / len(y_train_tensor)
    
    # 计算测试集准确率
    test_outputs = model(X_test_tensor)
    _, test_preds = torch.max(test_outputs, 1)
    test_accuracy = (test_preds == y_test_tensor).sum().item() / len(y_test_tensor)

print(f'训练集准确率: {train_accuracy:.4f}')
print(f'测试集准确率: {test_accuracy:.4f}')

# 6. 保存模型
torch.save(model.state_dict(), 'simple_classifier.pth')
print('模型已保存')
```

## PyTorch 常用技巧

### 1. 数据加载

```python
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y).long()
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 创建数据集和数据加载器
train_dataset = CustomDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# 使用数据加载器进行训练
for batch_idx, (data, targets) in enumerate(train_loader):
    # 训练代码
    pass
```

### 2. 模型评估

```python
def evaluate_model(model, data_loader, criterion):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data, targets in data_loader:
            outputs = model(data)
            loss = criterion(outputs, targets)
            total_loss += loss.item()
            
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
    
    accuracy = correct / total
    avg_loss = total_loss / len(data_loader)
    
    return accuracy, avg_loss
```

### 3. 使用GPU加速

```python
# 检查是否有可用的GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'使用设备: {device}')

# 将模型移到GPU
model.to(device)

# 将数据移到GPU
X_train_tensor = X_train_tensor.to(device)
y_train_tensor = y_train_tensor.to(device)
```

## 常见问题及解决方案

### 1. CUDA 内存不足

```python
# 减少批量大小
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)  # 减小batch_size

# 使用梯度累积
accumulation_steps = 4
for batch_idx, (data, targets) in enumerate(train_loader):
    outputs = model(data)
    loss = criterion(outputs, targets)
    loss = loss / accumulation_steps  # 缩放损失
    loss.backward()
    
    if (batch_idx + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### 2. 过拟合

```python
# 添加 dropout
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.5)  # 添加dropout
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.dropout(out)  # 使用dropout
        out = self.fc2(out)
        return out

# 使用L2正则化
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
```

## 进一步学习资源

- [PyTorch 官方文档](https://pytorch.org/docs/stable/index.html)
- [PyTorch 教程](https://pytorch.org/tutorials/)
- [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- [PyTorch 官方示例](https://github.com/pytorch/examples)
- [《深度学习入门之PyTorch》](https://github.com/L1aoXingyu/code-of-learn-deep-learning-with-pytorch)

---

*通过本教程，你应该已经掌握了PyTorch的基本使用方法和训练简单机器学习模型的技巧。继续深入学习，你可以构建更复杂的深度学习模型！* 🎉