## Pycharm-使用正则表达式替换 代码

- https://www.jetbrains.com/help/pycharm/tutorial-finding-and-replacing-text-using-regular-expressions.html

```html
<new product="ij" category="105" title="Multiline search and replace in the current file" />
<new product="ij" category="105" title="Improved search and replace in the current file" />
<new product="ij" category="105" title="Regexp shows replacement preview" />
...
```
- 勾选Regex
- \stitle="(.*)?"\s*(/>*)
    - $2<title>$1</title>