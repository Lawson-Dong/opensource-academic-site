# TensorFlow代码示例

> 发布时间：2026-03-21
> 主题：TensorFlow

本文展示如何使用TensorFlow Keras定义和训练一个简单的神经网络。

## 基本神经网络

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# 定义简单的神经网络
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

## 代码解析

1. **导入库**：导入TensorFlow和Keras相关模块。

2. **定义网络结构**：使用`Sequential`模型创建一个线性堆叠的神经网络。
   - `Flatten`层：将输入的二维数据（28x28）展平为一维向量。
   - `Dense`层：全连接层，第一个Dense层有128个神经元，使用ReLU激活函数；第二个Dense层有10个神经元，使用softmax激活函数。

3. **编译模型**：配置模型的优化器、损失函数和评估指标。
   - `optimizer`：使用Adam优化器，这是一种常用的自适应学习率优化算法。
   - `loss`：使用稀疏分类交叉熵损失函数，适用于整数标签的分类任务。
   - `metrics`：使用准确率作为评估指标。

## 训练模型

以下是训练模型的代码示例：

```python
# 训练模型
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_val, y_val))

# 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')
```

## 数据加载

使用TensorFlow的`keras.datasets`加载MNIST数据集：

```python
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train, x_test = x_train / 255.0, x_test / 255.0

# 分割验证集
x_val, y_val = x_train[50000:], y_train[50000:]
x_train, y_train = x_train[:50000], y_train[:50000]
```

## 完整训练流程

将所有代码组合起来：

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train, x_test = x_train / 255.0, x_test / 255.0

# 分割验证集
x_val, y_val = x_train[50000:], y_train[50000:]
x_train, y_train = x_train[:50000], y_train[:50000]

# 定义模型
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_val, y_val))

# 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')

# 预测
predictions = model.predict(x_test)
```

## 模型保存和加载

```python
# 保存模型
model.save('mnist_model.h5')

# 加载模型
from tensorflow.keras.models import load_model
loaded_model = load_model('mnist_model.h5')

# 评估加载的模型
test_loss, test_acc = loaded_model.evaluate(x_test, y_test)
print(f'Loaded model accuracy: {test_acc:.4f}')
```

## 可视化训练过程

```python
import matplotlib.pyplot as plt

# 绘制训练和验证准确率
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# 绘制训练和验证损失
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
```

## 总结

TensorFlow Keras是一个高级神经网络API，它使得构建和训练神经网络变得更加简单和直观。通过本文的示例，我们学习了如何使用TensorFlow Keras定义一个简单的神经网络，如何加载和预处理数据，如何训练和评估模型，以及如何保存和加载模型。

TensorFlow是一个功能强大的深度学习框架，它提供了丰富的工具和API，支持从研究到生产的全流程。Keras作为TensorFlow的高级API，进一步简化了模型的构建和训练过程，使得深度学习变得更加 accessible。

随着深度学习的不断发展，TensorFlow也在不断更新和改进，为用户提供更多强大的功能和工具。通过学习TensorFlow，我们可以更好地理解和应用深度学习技术，解决各种复杂的问题。