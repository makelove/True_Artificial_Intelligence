## 安装MicroPython到Wemos-D1-Mini
- 参考
    - https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/setup.html
    
- 步骤跟Wemos-D1-WIFI相同
- 清除 flash
```bash
(.py3) pro:~ play$ esptool.py --port /dev/tty.wchusbserial1420 --baud 115200 write_flash --flash_size=detect 0 ~/Downloads/firmware-combined.bin
esptool.py v2.2
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Auto-detected Flash size: 4MB
Flash params set to 0x0040
Compressed 613928 bytes to 398859...
Wrote 613928 bytes (398859 compressed) at 0x00000000 in 35.4 seconds (effective 138.6 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting...
```    

- 测试
    - 参考
        - https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html
        - https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
    - screen /dev/tty.wchusbserial1420 115200
```python
>>> print('Hello world! MicroPython')
Hello world! MicroPython
>>>
#
>>> import esp
>>> esp.check_fw()
size: 613912
md5: 29bfc564254dc311704c4d51a6d2eed9
True
#

#
import network
>>> sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#8 ets_task(4020ed88, 28, 3fff9fb0, 10)
>>> sta_if.scan()
[(b'ChinaNet-U7sn', b'\x14\xa0\xf8CyT', 1, -73, 4, 0), (b'TP-LINK_A2BE', b'\xf4\x83\xcd\x83\xa2\xbe', 1, -93, 4, 0), (b'911', 
b' k\xe7\xcb\x98\xee', 3, -58, 4, 0), (b'Xiaomi_540', b'x\x11\xdc\x03\x8c\xf2', 4, -64, 4, 0), (b'CU_hca9', b'd\x13l\xddV\xa8', 6, -70, 4, 0), (b'xxx42', b'\x8c\xa6\xdf\x08\xb5X', 6, -82, 4, 0), (b'gehua01141705110123112', b'\x00\x1fd/@\xfc', 6, -81, 3, 0), (b'HUAWEI-R6RFKQ', b'<\xfaC0\xe5r', 6, -88, 3, 0), (b'xxx41', b'\xd4\xee\x07Y\xb9z', 8, -65, 4, 0), (b'HHT_200_1_36_47_', b'\xac\xcf#\xbb\x9e\x1c', 11, -58, 3, 0), (b'ChinaNet-eeg7', b'\xe4\xc2\xd1d\xf0,', 11, -64, 4, 0), (b'CMCC-DrS3', b'\xbc?\x8fO\xdet', 11, -77, 4, 0), (b'HHT_200_1_21_70_', b'\xac\xcf#\xb0\x9b\xd8', 11, -84, 3, 0)]
>>> sta_if.connect(
>>> sta_if.connect("xxx41", "xxxxxx")
>>> import network
>>> sta_if.isconnected()
True


#
>>> help()
Welcome to MicroPython!

For online docs please visit http://docs.micropython.org/en/latest/esp8266/ .
For diagnostic information to include in bug reports execute 'import port_diag'.

Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection
# Change name/password of ESP8266's AP:
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="<AP_NAME>", authmode=network.AUTH_WPA_WPA2_PSK, password="<password>")

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
```

-
```python
#LED
from machine import Pin
led = Pin(2, Pin.OUT)
led(0)#熄灭pin.on()
led(1)#点亮pin.off()
#
from time import sleep
for i in range(10):
    led(1)
    sleep(1)
    led(0)
    sleep(0.5)

#PWM
from machine import Pin, PWM
import time

pwm = PWM(Pin(2))
pwm.duty(896)
time.sleep(1)
pwm.duty(512)
time.sleep(1)
pwm.duty(0)

```