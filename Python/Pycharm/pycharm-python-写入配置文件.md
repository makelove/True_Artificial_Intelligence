## pycharm-python-写入配置文件

- 问题
    - Pycharm运行程序时，通常会使用python或虚拟环境来运行，
        - 例如 /Users/play/.py3/bin/python3.6 /Users/play/github/True_Artificial_Intelligence/Test/test1.py
        - 如果test1.py写入一些配置文件，则文件会保存在/Users/play/.py3/bin/中


- 解决
```python
import os

dirpath = os.path.dirname(__file__)
filepath = os.path.join(dirpath, 'test.txt')
open(filepath, 'r')
```