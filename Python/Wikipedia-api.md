## 百科全书Wikipedia-api
- 参考
    - https://github.com/goldsmith/Wikipedia
    - 文档https://wikipedia.readthedocs.org/
    
- 安装
    - pip install wikipedia
- 使用
```python
import wikipedia

wikipedia.languages()
'''
'zh': '中文',
 'zh-classical': '文言',
 'zh-cn': '中文（中国大陆）\u200e',
 'zh-hans': '中文（简体）\u200e',
 'zh-hant': '中文（繁體）\u200e',
 'zh-hk': '中文（香港）\u200e',
'''
wikipedia.set_lang('zh')

In [15]: wikipedia.summary("爱因斯坦", sentences=2)
Out[15]: '阿尔伯特·爱因斯坦，或譯亞伯特·爱因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日）是20世纪猶太裔理論物理學家，创立了現代物理學的兩大支柱之一的相对论，也是質能等價公式（E = mc2）的發現者。他在科學哲學領域頗具影響力。'


In [20]: wikipedia.search('纽约',results=5,suggestion=T
    ...: rue)
Out[20]: (['纽约', '纽约证券交易所', '纽约时报', '纽约市立大学', '纽约大学'], None)

In [21]: wikipedia.random(pages=10)
Out[21]:
['陳于階',
 '蓝翅希鹛',
 '塞加',
 '库埃瓦斯德圣克莱门特',
 '国话先锋剧场',
 
 
```    