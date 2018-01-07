## Docker_使用USB

- 参考
    - [Developing Arduino with Docker](https://lk4d4.darth.io/posts/ino/)
    - [Getting a USB device to show up in a Docker container on OS X](https://gist.github.com/stonehippo/e33750f185806924f1254349ea1a4e68)
    
- 在macOS上不可行
    
- 运行
    - 需要先编译Linux内核，支持USB
        - Device Drivers -> USB support -> USB Modem (CDC ACM) support
    - 添加lsusb支持
        - apt-get install usbutils
    - docker run -it --rm --device=/dev/tty.usbserial ubuntu bash
    - 添加权限
        - docker run -it --rm --privileged --device=/dev/tty.usbserial ubuntu bash