# HTML示例

> 发布时间：2026-03-14
> 主题：HTML

本文展示基本的HTML页面结构示例。

## 基本HTML页面

```html
<!-- HTML示例 -->
<!DOCTYPE html>
<html>
<head>
    <title>示例页面</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>这是一个HTML示例</p>
</body>
</html>
```

## 页面解析

1. **DOCTYPE声明**：`<!DOCTYPE html>` 声明了文档类型，告诉浏览器这是一个HTML5文档。

2. **HTML根元素**：`<html>` 标签是HTML文档的根元素，包含了整个页面的内容。

3. **头部**：`<head>` 标签包含了页面的元数据，如标题、样式、脚本等。
   - `<title>` 标签定义了页面的标题，显示在浏览器的标签栏中。

4. **主体**：`<body>` 标签包含了页面的主要内容，如文本、图片、链接等。
   - `<h1>` 标签定义了一个一级标题。
   - `<p>` 标签定义了一个段落。

## 完整HTML页面示例

以下是一个更完整的HTML页面示例，包含了更多的HTML元素：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>完整HTML示例</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            line-height: 1.6;
            color: #666;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        ul {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>HTML示例页面</h1>
        
        <p>这是一个完整的HTML页面示例，包含了各种HTML元素。</p>
        
        <h2>图片示例</h2>
        <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=beautiful%20landscape&image_size=square_hd" alt="风景图片">
        
        <h2>链接示例</h2>
        <p>访问 <a href="https://www.example.com" target="_blank">示例网站</a> 了解更多信息。</p>
        
        <h2>列表示例</h2>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
        
        <h2>表格示例</h2>
        <table border="1" style="width: 100%; border-collapse: collapse;">
            <tr>
                <th>姓名</th>
                <th>年龄</th>
                <th>职业</th>
            </tr>
            <tr>
                <td>张三</td>
                <td>25</td>
                <td>工程师</td>
            </tr>
            <tr>
                <td>李四</td>
                <td>30</td>
                <td>教师</td>
            </tr>
        </table>
        
        <h2>表单示例</h2>
        <form action="#" method="post">
            <label for="name">姓名：</label>
            <input type="text" id="name" name="name" placeholder="请输入姓名">
            <br><br>
            <label for="email">邮箱：</label>
            <input type="email" id="email" name="email" placeholder="请输入邮箱">
            <br><br>
            <input type="submit" value="提交">
        </form>
    </div>
</body>
</html>
```

## HTML5新特性

HTML5引入了许多新的元素和特性，如：

- **语义化标签**：`<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, `<footer>` 等
- **表单增强**：新的输入类型（如 `date`, `time`, `email`, `url` 等）
- **多媒体支持**：`<video>` 和 `<audio>` 标签
- **Canvas**：用于绘制图形的元素
- **SVG**：可缩放矢量图形
- **地理位置**：获取用户的地理位置
- **本地存储**：`localStorage` 和 `sessionStorage`
- **Web Workers**：在后台运行JavaScript

## 总结

HTML是构建网页的基础，它定义了网页的结构和内容。通过学习HTML，我们可以创建各种类型的网页，从简单的静态页面到复杂的交互式应用。

随着Web技术的发展，HTML也在不断演进，HTML5引入了许多新的特性和元素，使网页更加丰富和功能强大。掌握HTML是学习Web开发的第一步，也是理解Web技术的基础。