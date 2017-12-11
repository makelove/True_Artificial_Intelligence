## Arduino-README

## 学习心得
- 使用Firmata进行串行数据通信
    - 利用Firmata协议，主机可以控制连接到Arduino上的设备，比如伺服电机，马达和LED等。可以用计算机发送命令给1个或多个Arduino，制作你自己的炫彩声光秀。
    - python库：https://github.com/tino/pyFirmata
    - 安装 pip install pyfirmata
    - 参考：[Python 与嵌入式系统系列 - Firmata](https://zhuanlan.zhihu.com/p/20174242)
```python
from pyfirmata import Arduino
import time
import sys

com_port='/dev/tty.usbmodem1421'
board = Arduino(com_port)

for i in range(10):
    board.digital[13].write(i % 2)
    time.sleep(1)

#
board.digital[13].write(1)#点亮LED
board.digital[13].write(0)#熄灭LED
board.exit()
```    

- 