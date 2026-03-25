# Java示例：Hello World

> 发布时间：2026-03-19
> 主题：Java

本文展示Java语言的经典Hello World程序。

## 基本Hello World程序

```java
// Java示例：Hello World
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## 程序解析

1. **类定义**：`public class HelloWorld` 定义了一个名为HelloWorld的公共类。在Java中，每个文件只能有一个公共类，且文件名必须与公共类名相同。

2. **主方法**：`public static void main(String[] args)` 是Java程序的入口点。所有Java程序都从这个方法开始执行。
   - `public`：表示这个方法可以被其他类访问。
   - `static`：表示这个方法属于类，而不是类的实例。
   - `void`：表示这个方法没有返回值。
   - `main`：方法名，固定为main。
   - `String[] args`：方法参数，是一个字符串数组，用于接收命令行参数。

3. **输出语句**：`System.out.println("Hello, World!");` 用于在控制台输出字符串"Hello, World!"。
   - `System`：是Java的一个内置类。
   - `out`：是System类的一个静态成员变量，表示标准输出流。
   - `println`：是PrintStream类的一个方法，用于输出字符串并换行。

## 编译和运行

1. **编译**：使用`javac`命令编译Java源文件。
   ```bash
   javac HelloWorld.java
   ```
   这将生成一个名为`HelloWorld.class`的字节码文件。

2. **运行**：使用`java`命令运行编译后的字节码文件。
   ```bash
   java HelloWorld
   ```
   这将在控制台输出"Hello, World!"。

## 命令行参数

我们可以修改HelloWorld程序，使其能够处理命令行参数：

```java
// Java示例：Hello World（带命令行参数）
public class HelloWorld {
    public static void main(String[] args) {
        if (args.length > 0) {
            System.out.println("Hello, " + args[0] + "!");
        } else {
            System.out.println("Hello, World!");
        }
    }
}
```

编译并运行：
```bash
javac HelloWorld.java
java HelloWorld Alice
```

输出：
```
Hello, Alice!
```

## 包声明

在实际项目中，我们通常会为Java类添加包声明：

```java
// Java示例：Hello World（带包声明）
package com.example;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

编译和运行：
```bash
# 编译
javac -d . HelloWorld.java

# 运行
java com.example.HelloWorld
```

## 总结

Hello World程序是学习任何编程语言的第一步，它展示了Java程序的基本结构和语法。通过这个简单的程序，我们可以了解Java的类定义、主方法、输出语句等基本概念。

在实际开发中，Java程序会更加复杂，但基本的结构和原理是相同的。掌握Hello World程序是学习Java的基础，也是理解Java语言特性的起点。