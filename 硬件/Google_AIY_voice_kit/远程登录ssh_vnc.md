## 远程登录ssh_vnc

- ssh
    - ssh pi@192.168.0.126
        - 登录路由器查看aiy的IP，可能会改变
- VNC
    - 在aiy树莓派上安装 tigervnc
        - sudo apt-get install realvnc-vnc-server
        - ubuntu mate 不行 。vncserver-x11
            - vncserver-x11: command not found
    - 在macOS安装 VNC Viewer.app 
    - 使用
        - aiy 输入vncserver
        
```bash
New 'aiy:1 (pi)' desktop is aiy:1

Starting applications specified in /home/pi/.vnc/xstartup
Log file is /home/pi/.vnc/aiy:1.log
```        

- VNC Viewer
    - 192.168.0.126:1
    - 密码 raspberry