# 数学公式示例

> 发布时间：2026-03-22
> 主题：数学

本文展示了一些常见的数学公式，包括行内公式和独立公式块。

## 行内公式

行内公式示例：\(E = mc^2\)，这是爱因斯坦的质能方程。

其他行内公式示例：

- 勾股定理：\(a^2 + b^2 = c^2\)
- 二次方程：\(ax^2 + bx + c = 0\)
- 指数函数：\(e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}\)
- 对数函数：\(\log_b(x) = \frac{\log_a(x)}{\log_a(b)}\)

## 独立公式块

### 高斯积分

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

### 微积分基本定理

$$
\frac{d}{dx} \left( \int_{a}^{x} f(t) dt \right) = f(x)
$$

### 麦克斯韦方程

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$

$$
\nabla \cdot \mathbf{B} = 0
$$

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

### 薛定谔方程

$$
i\hbar \frac{\partial}{\partial t} \Psi(\mathbf{r}, t) = \hat{H} \Psi(\mathbf{r}, t)
$$

### 熵增原理

$$
\Delta S \geq 0
$$

### 泰勒展开

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n
$$

### 傅里叶变换

$$
\mathcal{F}\{f(t)\} = F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

### 拉普拉斯变换

$$
\mathcal{L}\{f(t)\} = F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
$$

### 矩阵运算

矩阵乘法：

$$
(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

矩阵的特征值和特征向量：

$$
A \mathbf{v} = \lambda \mathbf{v}
$$

## 总结

LaTeX是一种强大的排版系统，特别适合于数学公式的排版。通过使用LaTeX，我们可以清晰、准确地表达各种复杂的数学公式。