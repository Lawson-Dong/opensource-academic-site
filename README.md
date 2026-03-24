# 个人学术网站

这是一个基于VuePress构建的个人学术网站，用于展示物理和人工智能双专业本科生的学术思考、学习笔记、代码项目及人工智能技术成果。

## 功能特性

- **思考感悟区**：支持Markdown格式内容输入，实现Markdown语法的完整解析与渲染
- **笔记区**：支持LaTeX格式数学公式与文本输入，实现LaTeX语法解析与科学公式渲染
- **代码区**：支持多语言代码块展示，兼容Python、Java、HTML、C++、C等编程语言的语法高亮
- **人工智能技术区**：支持多模态内容展示，包括PyTorch和TensorFlow框架的代码展示、AI Agent技能文档、图片演示功能、类Google Colab的文字与代码混合输入展示模式

## 技术实现

- **静态网站生成器**：VuePress
- **Markdown解析**：内置支持
- **LaTeX公式**：KaTeX
- **代码高亮**：Prism.js
- **响应式设计**：VuePress默认主题
- **搜索功能**：VuePress内置搜索

## 项目结构

```
.
├── docs/
│   ├── .vuepress/
│   │   ├── config.js         # VuePress配置文件
│   │   └── public/           # 静态资源目录
│   ├── thoughts/             # 思考感悟区
│   ├── notes/                # 笔记区
│   ├── code/                 # 代码区
│   ├── ai/                   # 人工智能技术区
│   └── README.md             # 网站首页
├── package.json              # 项目依赖配置
└── .gitignore                # Git忽略文件
```

## 本地开发

1. 安装依赖
   ```bash
   npm install
   ```

2. 启动开发服务器
   ```bash
   npm run dev
   ```

3. 访问 http://localhost:8080 查看网站

## 构建部署

1. 构建静态文件
   ```bash
   npm run build
   ```

2. 部署到GitHub.io
   - 将 `docs/.vuepress/dist` 目录下的文件推送到 GitHub 仓库的 `gh-pages` 分支
   - 或者使用 GitHub Actions 自动部署

## 内容更新

- 在对应目录下创建或修改 Markdown 文件
- 提交到 GitHub 仓库
- 自动或手动部署到 GitHub.io

## 依赖项

- vuepress: ^1.9.7
- @vuepress/plugin-back-to-top: ^1.9.7
- @vuepress/plugin-medium-zoom: ^1.9.7
- markdown-it-katex: ^2.0.3
- markdown-it-copy: ^0.1.0