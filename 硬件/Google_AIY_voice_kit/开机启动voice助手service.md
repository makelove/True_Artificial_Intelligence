## 开机启动voice助手service,设置http_proxy

很简单
- 打开systemd/voice-recognizer.service。其他不变
```bash
[Service]
Environment="http_proxy=http://192.168.0.159:50493"
Environment="https_proxy=http://192.168.0.159:50493"
Environment=VIRTUAL_ENV=/home/pi/voice-recognizer-raspi/env
Environment=PATH=/home/pi/voice-recognizer-raspi/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/home/pi/voice-recognizer-raspi/env/bin/python3 -u src/assistant_grpc_demo.py
```
- 然后安装service
    - scripts/install-services.sh
- 启动service
    - sudo systemctl start voice-recognizer.service
    - 关闭sudo systemctl stop voice-recognizer.service
    - 开机启动 sudo systemctl enable voice-recognizer.service

- 检查是否成功安装
    - 查看service日志
        - journalctl -u voice-recognizer.service -b -e
    - 在assistant_grpc_demo.py开头打印环境变量
```python
logging.info(os.environ['http_proxy'])
logging.info(os.environ['https_proxy'])
```    
- 看到LED灯闪烁，便成功了。    