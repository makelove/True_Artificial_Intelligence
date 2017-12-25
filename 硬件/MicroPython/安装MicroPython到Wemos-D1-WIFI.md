## 安装MicroPython到Wemos-D1-WIFI
- 参考
    - [如何在 ESP8266 运行 MicroPython](https://www.wandianshenme.com/play/esp8266-install-micropython-python-in-hardware/)
    - [WeMos D1 mini玩转MicroPython](https://www.jianshu.com/p/7f75ec16428d)
    - 正确:http://garybake.com/getting-started-with-the-wemos-d1-and-micropython.html
    - [MicroPython on ESP8266 (五) : WiFi 連線與 WebREPL 測試](https://yhhuang1966.blogspot.jp/2017/05/micropython-on-esp8266-wifi_16.html)
    - 智能小车[MicroPython IoT Rover Based on WEMOS D1 (ESP-8266EX)](http://www.instructables.com/id/MicroPython-IoT-Rover-Based-on-WeMos-D1-ESP-8266EX/)
    
- 步骤
    - 从 MicroPython 官网的下载页面（http://micropython.org/download#esp8266） 下载最新的固件
        - esp8266-20171101-v1.9.3.bin
    - 烧录固件
        - pip install esptool
- 清除 flash
```bash
(.py3) pro:~ play$ esptool.py --port /dev/tty.wchusbserial1420 erase_flash
esptool.py v2.2
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 3.1s
Hard resetting...
```
- 烧录新的固件
    - 参考
        - https://gist.github.com/stigtsp/160567cdd265c67fafb09b1c47120fb9
```bash
(.py3) pro:~ play$ esptool.py --port /dev/tty.wchusbserial1420 write_flash -fm dio -fs 32m -ff 40m 0x00000 ~/Downloads/esp8266-20171101-v1.9.3.bin
WARNING: Flash size arguments in megabits like '32m' are deprecated.
Please use the equivalent size '4MB'.
Megabit arguments may be removed in a future release.
esptool.py v2.2
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash params set to 0x0240
Compressed 600888 bytes to 392073...
Wrote 600888 bytes (392073 compressed) at 0x00000000 in 35.0 seconds (effective 137.2 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting...
```

- 测试
    - screen /dev/tty.wchusbserial1420 115200
```python
>>> import esp
>>> esp.check_fw()
size: 600872
md5: 35e285a80516e70242ebf7d780d6c70f
True

#
>>> from machine import Pin
>>> led14 = Pin(14, Pin.OUT)
>>> led14.
init            value           off             on
irq             IN              OUT             OPEN_DRAIN
PULL_UP         IRQ_RISING      IRQ_FALLING
>>> led14.on()
>>> led14.off()
>>> led13 = Pin(13, Pin.OUT)
>>> led12 = Pin(12, Pin.OUT)
>>> led13.on()
>>> led13.off()
>>> led12.on()
>>> led12.off()
```    