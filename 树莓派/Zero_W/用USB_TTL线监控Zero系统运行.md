## 使用USB TTL线
- 参考
    - [Connect To A Raspberry Pi And Pi Zero With A USB To TTL Serial Cable](https://www.thepolyglotdeveloper.com/2017/02/connect-raspberry-pi-pi-zero-usb-ttl-serial-cable/)
    - [TTL线](https://www.amazon.com/gp/product/B00QT7LQ88/)
   
- 使用
    - 把系统TF卡插入电脑，编辑/boot/config.txt
        - enable_uart=1
    - 接线
        - 红色-5v
        - 黑色-GND
        - 白色-GPIO14(TXD0)
        - 绿色-GPIO15(RXD0)
- 把USB插入电脑
    - 在终端运行 screen /dev/cu.usbserial 115200
    - 按下Enter回车键，即可