module.exports = {
  title: '个人学术网站',
  description: '物理与人工智能双专业本科生的学术思考、学习笔记和技术成果',
  base: '/opensource-academic-site/',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '思考感悟', link: './thoughts/' },
      { text: '笔记', link: './notes/' },
      { text: '代码', link: './code/' },
      { text: '人工智能', link: './ai/' }
    ],
    sidebar: {
      '/thoughts/': [
        { title: '思考感悟', collapsable: false, children: [''] }
      ],
      '/notes/': [
        { title: '笔记', collapsable: false, children: [''] }
      ],
      '/code/': [
        { title: '代码', collapsable: false, children: [''] }
      ],
      '/ai/': [
        { title: '人工智能', collapsable: false, children: [''] }
      ]
    },
    search: true,
    searchMaxSuggestions: 10,
    lastUpdated: '最后更新',
    smoothScroll: true
  },
  plugins: [
    '@vuepress/back-to-top',
    '@vuepress/medium-zoom',
    {
      name: 'katex',
      globalUIComponents: ['Katex']
    }
  ],
  markdown: {
    extendMarkdown: md => {
      md.use(require('markdown-it-katex'))
      md.use(require('markdown-it-copy'))
    },
    lineNumbers: true
  },
  // 性能优化
  evergreen: true,
  // 禁用预加载，减少不必要的网络请求
  shouldPrefetch: false
}