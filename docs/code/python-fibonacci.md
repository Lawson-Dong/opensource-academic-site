# Python示例：斐波那契数列

> 发布时间：2026-03-23
> 主题：Python

本文展示如何使用Python实现斐波那契数列的计算。

## 递归方法

递归是一种直观的实现方式：

```python
# Python示例：斐波那契数列（递归方法）
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 测试
for i in range(10):
    print(fibonacci(i))
```

递归方法的时间复杂度是 O(2^n)，因为对于每个n，都会计算两次较小的n值，导致重复计算。

## 迭代方法

迭代方法可以避免重复计算，提高效率：

```python
# Python示例：斐波那契数列（迭代方法）
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 测试
for i in range(10):
    print(fibonacci_iterative(i))
```

迭代方法的时间复杂度是 O(n)，空间复杂度是 O(1)，比递归方法高效得多。

## 记忆化方法

记忆化方法结合了递归的简洁性和迭代的效率：

```python
# Python示例：斐波那契数列（记忆化方法）
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# 测试
for i in range(10):
    print(fibonacci_memo(i))
```

记忆化方法的时间复杂度是 O(n)，空间复杂度是 O(n)。

## 生成器方法

生成器方法可以逐个生成斐波那契数列的元素，节省内存：

```python
# Python示例：斐波那契数列（生成器方法）
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 测试
for num in fibonacci_generator(10):
    print(num)
```

生成器方法的时间复杂度是 O(n)，空间复杂度是 O(1)。

## 矩阵快速幂方法

矩阵快速幂方法可以在 O(log n) 的时间复杂度内计算斐波那契数列：

```python
# Python示例：斐波那契数列（矩阵快速幂方法）
def matrix_pow(matrix, power):
    result = [[1, 0], [0, 1]]  # 单位矩阵
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
        power //= 2
    return result

def matrix_mult(a, b):
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
    ]

def fibonacci_matrix(n):
    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    result = matrix_pow(matrix, n-1)
    return result[0][0]

# 测试
for i in range(10):
    print(fibonacci_matrix(i))
```

矩阵快速幂方法的时间复杂度是 O(log n)，空间复杂度是 O(1)。

## 黄金分割方法

利用黄金分割率可以直接计算斐波那契数列：

```python
# Python示例：斐波那契数列（黄金分割方法）
import math

def fibonacci_golden(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))

# 测试
for i in range(10):
    print(fibonacci_golden(i))
```

黄金分割方法的时间复杂度是 O(1)，但由于浮点数精度的限制，对于较大的n可能会有误差。

## 总结

不同的实现方法各有优缺点，选择哪种方法取决于具体的应用场景：

- **递归方法**：简洁易懂，但效率低，适用于学习和理解递归概念。
- **迭代方法**：高效，适用于大多数实际应用。
- **记忆化方法**：结合了递归的简洁性和迭代的效率，适用于需要递归结构的场景。
- **生成器方法**：节省内存，适用于需要逐个处理斐波那契数列元素的场景。
- **矩阵快速幂方法**：最快，适用于计算较大的斐波那契数。
- **黄金分割方法**：直接计算，适用于不需要高精度的场景。