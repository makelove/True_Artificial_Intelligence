## try-catch-exception

- 使用traceback获取详细的异常信息https://blog.csdn.net/handsomekang/article/details/9373035

- 输出结果是integer division or modulo by zero，只知道是报了这个错，但是却不知道在哪个文件哪个函数哪一行报的错。
```python
try:
    1/0
except Exception as e:
    print(e)
```
- 使用traceback模块,把全部错误消息打印出来
```python
import traceback
try:
    1/0
except Exception as e:
    traceback.print_exc()
'''
Traceback (most recent call last):
  File "<ipython-input-57-4137c775dcd6>", line 2, in <module>
    1/0
ZeroDivisionError: division by zero
'''    
```
- 把traceback的全部错误消息保存到变量，使用logging或print，file open输出
```python
import traceback
try:
    1/0
except Exception as e:
    x=traceback.format_exc()
    print(x)
```