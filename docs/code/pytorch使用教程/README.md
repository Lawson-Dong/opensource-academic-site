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
import torch                                    # 导入PyTorch库
print(torch.__version__)                        # 打印当前PyTorch版本号
print(torch.cuda.is_available())                # 检查当前系统是否支持CUDA（即是否有可用的NVIDIA GPU）
```

## 基本张量操作

### 创建张量

```python
import torch                                    # 导入PyTorch库

# 创建标量（0维张量，只有一个数值）
scalar = torch.tensor(5.0)                      # 创建一个值为5.0的标量张量
print(f"标量: {scalar}")                        # 输出: 标量: tensor(5.)
print(f"标量形状: {scalar.shape}")              # 输出: 标量形状: torch.Size([])，标量没有维度

# 创建向量（1维张量）
vector = torch.tensor([1.0, 2.0, 3.0])         # 创建一个包含3个元素的一维张量
print(f"向量: {vector}")                        # 输出: 向量: tensor([1., 2., 3.])
print(f"向量形状: {vector.shape}")              # 输出: 向量形状: torch.Size([3])，表示长度为3

# 创建矩阵（2维张量）
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # 创建一个2行2列的二维张量
print(f"矩阵: {matrix}")                        # 输出: 矩阵: tensor([[1., 2.], [3., 4.]])
print(f"矩阵形状: {matrix.shape}")              # 输出: 矩阵形状: torch.Size([2, 2])，2行2列

# 创建3维张量（类似RGB图像，通道×高×宽）
tensor_3d = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])  # 2×2×2的三维张量
print(f"3维张量: {tensor_3d}")                  # 输出3维张量的所有元素
print(f"3维张量形状: {tensor_3d.shape}")        # 输出: 3维张量形状: torch.Size([2, 2, 2])

# 创建全零张量（常用于初始化偏置或掩码）
zeros = torch.zeros((2, 3))                     # 创建一个2行3列、所有元素为0的张量
print(f"全零张量: {zeros}")                     # 输出: tensor([[0., 0., 0.], [0., 0., 0.]])

# 创建全一张量（常用于初始化权重或掩码）
ones = torch.ones((2, 3))                       # 创建一个2行3列、所有元素为1的张量
print(f"全一张量: {ones}")                       # 输出: tensor([[1., 1., 1.], [1., 1., 1.]])

# 创建随机张量（值在[0, 1)之间均匀分布，常用于初始化权重）
random_tensor = torch.rand((2, 3))              # 创建一个2行3列、元素为随机数的张量
print(f"随机张量: {random_tensor}")              # 输出随机生成的2×3张量
```

### 张量运算

```python
import torch                                    # 导入PyTorch库

# 创建两个一维张量用于演示运算
a = torch.tensor([1.0, 2.0, 3.0])              # 创建向量a
b = torch.tensor([4.0, 5.0, 6.0])              # 创建向量b

# 逐元素加法：对应位置元素相加
c = a + b                                       # 等价于 torch.add(a, b)
print(f"a + b: {c}")                            # 输出: tensor([5., 7., 9.])

# 逐元素减法：对应位置元素相减
d = a - b                                       # 等价于 torch.sub(a, b)
print(f"a - b: {d}")                            # 输出: tensor([-3., -3., -3.])

# 逐元素乘法（Hadamard积）：对应位置元素相乘，不是矩阵乘法
e = a * b                                       # 等价于 torch.mul(a, b)
print(f"a * b: {e}")                            # 输出: tensor([ 4., 10., 18.])

# 逐元素除法：对应位置元素相除
f = a / b                                       # 等价于 torch.div(a, b)
print(f"a / b: {f}")                            # 输出: tensor([0.2500, 0.4000, 0.5000])

# 矩阵乘法：2×2矩阵乘以2×1向量，结果为2×1向量
g = torch.matmul(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[5], [6]]))
# 计算过程: [[1*5+2*6], [3*5+4*6]] = [[17], [39]]
print(f"矩阵乘法: {g}")                         # 输出: tensor([[17], [39]])

# 广播机制：将一维张量[10.0, 20.0]自动扩展为2×2，然后逐元素相加
h = torch.tensor([[1.0, 2.0], [3.0, 4.0]]) + torch.tensor([10.0, 20.0])
# 等价于: [[1,2],[3,4]] + [[10,20],[10,20]] = [[11,22],[13,24]]
print(f"广播操作: {h}")                         # 输出: tensor([[11., 22.], [13., 24.]])
```

## 自动求导

```python
import torch                                    # 导入PyTorch库

# 创建需要求导的张量，requires_grad=True告诉PyTorch需要跟踪该张量的所有操作
x = torch.tensor(3.0, requires_grad=True)       # x = 3.0，标记为需要计算梯度
y = torch.tensor(5.0, requires_grad=True)       # y = 5.0，标记为需要计算梯度

# 定义计算图：z = 2x + y²
z = 2 * x + y ** 2                             # z = 2*3 + 5² = 6 + 25 = 31
print(f"z = {z}")                               # 输出: z = tensor(31., grad_fn=<AddBackward0>)

# 反向传播：自动计算z对x和y的偏导数
z.backward()                                    # 计算梯度：dz/dx = 2, dz/dy = 2y = 10

# 查看计算得到的梯度
print(f"x的梯度: {x.grad}")                     # 输出: 2.0，因为 dz/dx = d(2x+y²)/dx = 2
print(f"y的梯度: {y.grad}")                     # 输出: 10.0，因为 dz/dy = d(2x+y²)/dy = 2y = 2×5 = 10

# 使用torch.no_grad()上下文管理器禁用梯度跟踪
# 在模型评估阶段使用，可以节省内存并加快计算速度
with torch.no_grad():                           # 进入不跟踪梯度的上下文
    w = x * y                                   # 计算w = 3 × 5 = 15，但不记录梯度
    print(f"w = {w}")                           # 输出: w = tensor(15.)
    print(f"w.requires_grad = {w.requires_grad}")  # 输出: False，w不会跟踪梯度
```

## 构建简单的神经网络

### 基本网络结构

```python
import torch                                    # 导入PyTorch库
import torch.nn as nn                           # 导入神经网络模块，包含层、损失函数等

# 定义一个简单的全连接神经网络，继承自nn.Module（所有PyTorch模型的基类）
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # 调用父类nn.Module的构造函数，必须执行这一步
        super(SimpleNet, self).__init__()
        # 定义第一层：全连接层，将输入从input_size维映射到hidden_size维
        self.fc1 = nn.Linear(input_size, hidden_size)   # 包含权重矩阵W和偏置向量b
        # 定义激活函数：ReLU，引入非线性，f(x) = max(0, x)
        self.relu = nn.ReLU()
        # 定义第二层：全连接层，将hidden_size维映射到output_size维
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    # 定义前向传播：数据通过网络的过程
    def forward(self, x):
        out = self.fc1(x)                       # 输入x经过第一层线性变换：out = Wx + b
        out = self.relu(out)                    # 经过ReLU激活函数，引入非线性
        out = self.fc2(out)                     # 经过第二层线性变换，得到最终输出
        return out                              # 返回网络输出

# 创建网络实例：输入维度2，隐藏层维度10，输出维度1
model = SimpleNet(input_size=2, hidden_size=10, output_size=1)
print(model)                                    # 打印网络结构，显示各层信息

# 测试网络：输入一个样本，查看输出
input_tensor = torch.tensor([[1.0, 2.0]])       # 创建一个1×2的输入张量（1个样本，2个特征）
output = model(input_tensor)                    # 将输入传入网络，执行前向传播
print(f"网络输出: {output}")                    # 输出网络的预测结果（随机初始化的权重，所以结果是随机的）
```

## 训练一个简单的线性回归模型

### 完整训练代码

```python
import torch                                    # 导入PyTorch库
import torch.nn as nn                           # 导入神经网络模块
import torch.optim as optim                     # 导入优化器模块（SGD、Adam等）
import matplotlib.pyplot as plt                 # 导入绘图库，用于可视化结果
import numpy as np                              # 导入NumPy，用于生成模拟数据

# ========== 1. 生成模拟数据 ==========
np.random.seed(42)                              # 设置随机种子，保证每次运行结果一致
x = np.random.rand(100, 1) * 10                # 生成100个[0, 10)之间的随机数作为特征x
y = 2 * x + 1 + np.random.randn(100, 1) * 0.5  # 生成标签y = 2x + 1 + 噪声，模拟真实数据

# 将NumPy数组转换为PyTorch张量（PyTorch模型只能处理张量）
x_tensor = torch.from_numpy(x).float()          # 将x转为float32类型的张量
y_tensor = torch.from_numpy(y).float()          # 将y转为float32类型的张量

# ========== 2. 定义模型 ==========
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        # 定义一个线性层：输入维度1（x），输出维度1（y）
        # 等价于 y = wx + b，PyTorch会自动初始化w和b
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.linear(x)                   # 前向传播：计算 y = wx + b

model = LinearRegression()                      # 实例化线性回归模型
print(model)                                    # 打印模型结构，可以看到权重和偏置的初始值

# ========== 3. 定义损失函数和优化器 ==========
# MSE损失函数：均方误差，计算预测值与真实值之间的平均平方差
# 公式：Loss = (1/n) × Σ(ŷᵢ - yᵢ)²
criterion = nn.MSELoss()

# 随机梯度下降优化器：用于更新模型参数（权重和偏置）
# model.parameters()：获取模型中所有需要训练的参数
# lr=0.01：学习率，控制每次参数更新的步长大小
optimizer = optim.SGD(model.parameters(), lr=0.01)

# ========== 4. 训练模型 ==========
epochs = 1000                                   # 训练轮数：整个数据集将被重复使用1000次
losses = []                                     # 用于记录每轮的损失值，方便后续分析

for epoch in range(epochs):                     # 遍历每个训练轮次
    # --- 前向传播 ---
    outputs = model(x_tensor)                   # 将所有数据输入模型，得到预测值
    loss = criterion(outputs, y_tensor)         # 计算预测值与真实值之间的MSE损失
    
    # --- 反向传播和参数更新 ---
    optimizer.zero_grad()                       # 清零上一步的梯度（PyTorch默认会累积梯度）
    loss.backward()                             # 反向传播：自动计算损失对每个参数的梯度
    optimizer.step()                            # 根据梯度更新参数：w = w - lr × gradient
    
    # --- 记录和打印 ---
    losses.append(loss.item())                  # loss.item()将单元素张量转为Python标量
    if (epoch + 1) % 100 == 0:                  # 每100轮打印一次训练进度
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# ========== 5. 评估模型 ==========
with torch.no_grad():                           # 禁用梯度跟踪（评估阶段不需要计算梯度）
    predicted = model(x_tensor).numpy()         # 用训练好的模型进行预测，并转为NumPy数组

# 打印模型学习到的参数（理想情况下应接近 w=2, b=1）
print(f'模型参数:')
for name, param in model.named_parameters():    # 遍历模型的所有命名参数
    print(f'{name}: {param.data.item()}')       # 打印参数名和值

# ========== 6. 可视化结果 ==========
plt.figure(figsize=(10, 6))                     # 创建10×6英寸的画布
plt.scatter(x, y, label='原始数据')              # 绘制散点图，显示原始数据点
plt.plot(x, predicted, color='red', label='预测直线')  # 绘制拟合的直线
plt.xlabel('X')                                 # 设置x轴标签
plt.ylabel('Y')                                 # 设置y轴标签
plt.title('线性回归')                            # 设置图表标题
plt.legend()                                    # 显示图例
plt.show()                                      # 显示图表

# ========== 7. 保存模型 ==========
# 只保存模型的参数（权重和偏置），不保存模型结构
# .pth是PyTorch模型文件的标准扩展名
torch.save(model.state_dict(), 'linear_regression_model.pth')
print('模型已保存')

# ========== 8. 加载模型 ==========
loaded_model = LinearRegression()               # 先创建一个相同结构的模型实例
loaded_model.load_state_dict(torch.load('linear_regression_model.pth'))  # 加载保存的参数
print('模型已加载')

# 测试加载的模型：输入x=5.0，预测y应该接近 2×5+1 = 11
with torch.no_grad():                           # 评估阶段不需要梯度
    test_input = torch.tensor([[5.0]])           # 创建测试输入
    test_output = loaded_model(test_input)       # 用加载的模型进行预测
    print(f'输入 5.0, 预测输出: {test_output.item()}')  # 打印预测结果
    print(f'真实值应该接近: {2*5 + 1}')          # 打印理论值：11
```

## 训练一个简单的分类模型

### 完整训练代码

```python
import torch                                    # 导入PyTorch库
import torch.nn as nn                           # 导入神经网络模块
import torch.optim as optim                     # 导入优化器模块
from sklearn.datasets import make_classification  # 导入sklearn的分类数据生成器
from sklearn.model_selection import train_test_split  # 导入数据集划分工具
from sklearn.preprocessing import StandardScaler     # 导入数据标准化工具

# ========== 1. 生成模拟分类数据 ==========
# 生成1000个样本，每个样本20个特征，分为2个类别
# n_informative=10：其中10个特征是有区分度的，其余10个是噪声特征
X, y = make_classification(
    n_samples=1000, n_features=20, n_classes=2,
    n_informative=10, random_state=42
)

# 数据标准化：将每个特征缩放到均值为0、标准差为1的范围
# 这对于神经网络的训练非常重要，可以加速收敛
scaler = StandardScaler()
X = scaler.fit_transform(X)                     # 计算均值和标准差，并应用标准化

# 划分训练集（80%）和测试集（20%）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 将NumPy数组转换为PyTorch张量
X_train_tensor = torch.from_numpy(X_train).float()  # 训练集特征，转为float32
y_train_tensor = torch.from_numpy(y_train).long()   # 训练集标签，转为long（CrossEntropyLoss要求）
X_test_tensor = torch.from_numpy(X_test).float()    # 测试集特征
y_test_tensor = torch.from_numpy(y_test).long()     # 测试集标签

# ========== 2. 定义模型 ==========
class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleClassifier, self).__init__()
        # 第一层：全连接层，将20维输入映射到32维隐藏层
        self.fc1 = nn.Linear(input_size, hidden_size)
        # ReLU激活函数：引入非线性，帮助网络学习复杂模式
        self.relu = nn.ReLU()
        # 第二层：全连接层，将32维隐藏层映射到2维输出（2个类别的分数）
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)                       # 线性变换：20维 → 32维
        out = self.relu(out)                    # ReLU激活：将负值变为0
        out = self.fc2(out)                     # 线性变换：32维 → 2维（输出logits）
        return out                              # 返回每个类别的原始分数（logits）

# 创建模型实例：输入20维，隐藏层32维，输出2维（2个类别）
model = SimpleClassifier(input_size=20, hidden_size=32, output_size=2)
print(model)                                    # 打印模型结构

# ========== 3. 定义损失函数和优化器 ==========
# 交叉熵损失函数：适用于多分类任务
# 内部会自动对输出进行softmax + log运算，所以模型输出不需要经过softmax
criterion = nn.CrossEntropyLoss()

# Adam优化器：自适应学习率优化器，比SGD收敛更快
# lr=0.001：初始学习率
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ========== 4. 训练模型 ==========
epochs = 100                                   # 训练100轮
train_losses = []                               # 记录每轮训练损失
test_losses = []                                # 记录每轮测试损失

for epoch in range(epochs):                     # 遍历每个训练轮次
    # --- 训练阶段 ---
    model.train()                               # 设置为训练模式（启用dropout和batch norm等）
    
    outputs = model(X_train_tensor)             # 前向传播：计算训练集的预测输出
    loss = criterion(outputs, y_train_tensor)   # 计算训练损失
    
    optimizer.zero_grad()                       # 清零梯度
    loss.backward()                             # 反向传播：计算梯度
    optimizer.step()                            # 更新参数
    
    train_losses.append(loss.item())            # 记录训练损失
    
    # --- 验证阶段 ---
    model.eval()                                # 设置为评估模式（禁用dropout和batch norm等）
    with torch.no_grad():                       # 禁用梯度跟踪，节省内存
        test_outputs = model(X_test_tensor)     # 计算测试集的预测输出
        test_loss = criterion(test_outputs, y_test_tensor)  # 计算测试损失
        test_losses.append(test_loss.item())    # 记录测试损失
    
    if (epoch + 1) % 10 == 0:                  # 每10轮打印一次
        print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}')

# ========== 5. 评估模型 ==========
model.eval()                                    # 设置为评估模式
with torch.no_grad():                           # 禁用梯度跟踪
    # 计算训练集准确率
    train_outputs = model(X_train_tensor)       # 训练集预测输出
    _, train_preds = torch.max(train_outputs, 1)  # 取每行最大值的索引作为预测类别
    train_accuracy = (train_preds == y_train_tensor).sum().item() / len(y_train_tensor)
    
    # 计算测试集准确率
    test_outputs = model(X_test_tensor)         # 测试集预测输出
    _, test_preds = torch.max(test_outputs, 1)   # 取每行最大值的索引作为预测类别
    test_accuracy = (test_preds == y_test_tensor).sum().item() / len(y_test_tensor)

print(f'训练集准确率: {train_accuracy:.4f}')     # 打印训练集准确率
print(f'测试集准确率: {test_accuracy:.4f}')      # 打印测试集准确率

# ========== 6. 保存模型 ==========
torch.save(model.state_dict(), 'simple_classifier.pth')  # 保存模型参数
print('模型已保存')
```

## PyTorch 常用技巧

### 1. 数据加载

```python
from torch.utils.data import Dataset, DataLoader  # 导入数据集和数据加载器

# 自定义数据集类，继承自Dataset（PyTorch数据集的基类）
class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()    # 将特征转为float32张量
        self.y = torch.from_numpy(y).long()     # 将标签转为long张量（分类任务需要）
    
    def __len__(self):
        return len(self.X)                      # 返回数据集的总样本数（必须实现）
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]         # 根据索引返回一个样本和对应标签（必须实现）

# 创建数据集实例
train_dataset = CustomDataset(X_train, y_train)

# 创建数据加载器：自动将数据分批次、打乱顺序
# batch_size=32：每批32个样本
# shuffle=True：每个epoch开始时打乱数据顺序，防止模型记忆数据顺序
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# 使用数据加载器进行训练
for batch_idx, (data, targets) in enumerate(train_loader):
    # data：当前批次的特征数据，形状为 [32, 20]
    # targets：当前批次的标签，形状为 [32]
    # 在这里编写训练代码...
    pass
```

### 2. 模型评估

```python
def evaluate_model(model, data_loader, criterion):
    """评估模型在给定数据集上的准确率和平均损失"""
    model.eval()                                # 设置为评估模式
    total_loss = 0                              # 累计损失
    correct = 0                                 # 正确预测数
    total = 0                                   # 总样本数
    
    with torch.no_grad():                       # 禁用梯度跟踪
        for data, targets in data_loader:       # 遍历每个批次
            outputs = model(data)               # 前向传播，得到预测输出
            loss = criterion(outputs, targets)  # 计算损失
            total_loss += loss.item()           # 累加损失值
            
            # torch.max(outputs, 1)：返回每行最大值及其索引
            # _：最大值（不需要），predicted：最大值的索引（即预测类别）
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)            # 累加当前批次的样本数
            correct += (predicted == targets).sum().item()  # 累加正确预测数
    
    accuracy = correct / total                  # 计算准确率
    avg_loss = total_loss / len(data_loader)    # 计算平均损失（按批次数平均）
    
    return accuracy, avg_loss                   # 返回准确率和平均损失
```

### 3. 使用GPU加速

```python
# 检查是否有可用的GPU，如果有则使用GPU，否则使用CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'使用设备: {device}')                    # 输出当前使用的设备

# 将模型的所有参数移到GPU上
model.to(device)                                # 之后模型的前向和反向传播都在GPU上执行

# 将数据移到GPU上（每次输入数据前都需要移到同一设备）
X_train_tensor = X_train_tensor.to(device)      # 训练集特征移到GPU
y_train_tensor = y_train_tensor.to(device)      # 训练集标签移到GPU
```

## 常见问题及解决方案

### 1. CUDA 内存不足

```python
# 方法一：减少批量大小，降低每次GPU需要处理的样本数量
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)  # 从32减小到16

# 方法二：使用梯度累积，模拟更大的batch_size
# 原理：将一个大批次分成多个小批次，分别计算梯度后累积，最后一次性更新参数
accumulation_steps = 4                         # 每4个小批次更新一次参数
for batch_idx, (data, targets) in enumerate(train_loader):
    outputs = model(data)                       # 前向传播
    loss = criterion(outputs, targets)          # 计算损失
    loss = loss / accumulation_steps            # 将损失除以累积步数，保证梯度均值不变
    loss.backward()                             # 反向传播，梯度会累积（因为没有调用zero_grad）
    
    if (batch_idx + 1) % accumulation_steps == 0:  # 每累积4步后更新一次参数
        optimizer.step()                        # 使用累积的梯度更新参数
        optimizer.zero_grad()                   # 清零梯度，为下一轮累积做准备
```

### 2. 过拟合

```python
# 方法一：添加Dropout层，在训练时随机丢弃一部分神经元
# 作用：防止神经元过度依赖某些特定特征，提高模型泛化能力
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # 第一层全连接
        self.relu = nn.ReLU()                   # ReLU激活函数
        self.dropout = nn.Dropout(p=0.5)        # Dropout层：训练时随机丢弃50%的神经元
        self.fc2 = nn.Linear(hidden_size, output_size)  # 第二层全连接
    
    def forward(self, x):
        out = self.fc1(x)                       # 线性变换
        out = self.relu(out)                    # ReLU激活
        out = self.dropout(out)                  # Dropout（仅在model.train()时生效）
        out = self.fc2(out)                     # 线性变换
        return out

# 方法二：使用L2正则化（权重衰减）
# 作用：在损失函数中添加参数的L2范数惩罚，防止参数值过大
# weight_decay=1e-4：权重衰减系数，值越大正则化越强
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