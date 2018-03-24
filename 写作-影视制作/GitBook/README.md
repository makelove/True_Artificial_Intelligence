## GitBook

- GitBook是一个基于 Node.js 的命令行工具，可使用 Github/Git 和 Markdown 来制作精美的电子书，GitBook 并非关于 Git 的教程。
- GitBook支持输出多种文档格式：
·静态站点：GitBook默认输出该种格式，生成的静态站点可直接托管搭载Github Pages服务上；
·PDF：需要安装gitbook-pdf依赖；
·eBook：需要安装ebook-convert；
· 单HTML网页：支持将内容输出为单页的HTML，不过一般用在将电子书格式转换为PDF或eBook的中间过程；
·JSON：一般用于电子书的调试或元数据提取。
- 使用GitBook制作电子书，必备两个文件：README.md和SUMMARY.md

- 安装
```bash
npm install gitbook -g
npm install -g gitbook-cli
```

- GitBook 大致分为两种使用方式，即离线和在线。最简单的使用方式是使用GitBook Editor编辑GitBook ，然后使用相关命令编译成功HTML。
    - 使用命令创建基本GitBook
    - 使用网页在线编辑器创建、编辑GitBook。
    - 使用GitBookEditor客户端创建、编辑GitBook。
