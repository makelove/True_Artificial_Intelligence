## 编译内核-接入Arduino

- TX2默认没有支持Arduino，插入Arduino USB没有在dev里显示
- 同时插入【Arduino UNO R3】，【Arduino Mega 2560国产】，【Wemos D1 WIFI】
```bash
nvidia@gpu:~$ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 006: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter #Mega 2560
Bus 001 Device 004: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter #D1 WIFI
Bus 001 Device 003: ID 248a:8367
Bus 001 Device 005: ID 2341:0043 Arduino SA Uno R3 (CDC ACM)
Bus 001 Device 002: ID 14cd:8601 Super Top
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

- 如果 加载ch341模块，表示没有发现
```bash
nvidia@gpu:~/github/buildJetsonTX2Kernel$ sudo modprobe ch341
[sudo] password for nvidia:
modprobe: FATAL: Module ch341 not found in directory /lib/modules/4.4.38-tegra
```

- 解决
    - 参考 [Build Kernel and ttyACM Module – NVIDIA Jetson TX2](http://www.jetsonhacks.com/2017/07/31/build-kernel-ttyacm-module-nvidia-jetson-tx2/)
        - Youtube视频 [Build Kernel and ttyACM module - NVIDIA Jetson TX2](https://www.youtube.com/watch?v=tDZF7ntLbxc)