## 安装x11vnc
- 参考
    - [Ubuntu16.04安装x11VNC远程桌面](http://blog.csdn.net/songbaiyao/article/details/72858087)
  

- 安装x11vnc
    - sudo apt-get install x11vnc
- 设置密码
    - x11vnc -storepasswd
- 修改配置文件
```bash
sudu vim /lib/systemd/system/x11vnc.service

[Unit]
Description=Start x11vnc at startup.
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -auth guess -forever -loop -noxdamage -repeat -rfbauth /home/<USERNAME>/.vnc/passwd -rfbport 5900 -shared

[Install]
WantedBy=multi-user.target
```

- 启动服务
    - sudo systemctl daemon-reload
    - sudo systemctl enable x11vnc.service
    - sudo systemctl start x11vnc.service