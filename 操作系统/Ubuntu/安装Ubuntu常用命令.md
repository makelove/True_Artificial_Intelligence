# 安装Ubuntu后常做步骤

- 总是要：下载最新版Ubuntu
    - https://www.ubuntu.com/download/desktop
    - ubuntu-16.04.3-desktop-amd64.iso

## 常用软件
- sudo apt update
- 删除libreoffice
    - sudo apt-get remove --purge libreoffice*
    - sudo apt-get remove libreoffice-common  
    - sudo apt-get purge libreoffice?
- sudo apt-get remove unity-webapps-common  
- 可选，删除不常用的软件
    - sudo apt-get remove thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines gnome-sudoku cheese
    
- ssh远程登录
    - sudo apt install openssh-server
    - ssh-keygen
    - cd .ssh
    - cp id_rsa.pub authorized_keys
    - 把自己电脑的公钥复制过来nano authorized_keys
    - ssh 登录免密码
- 更好的终端 
    - sudo apt install terminator    
- sudo apt-get install vim

- 安装 open-vm-tools代替 VMware Tools
    - 参考：https://zhuanlan.zhihu.com/p/22488904
    - 如果要实现文件夹共享，需要安装 open-vm-tools-dkms ，桌面环境还需要安装 open-vm-tools-desktop 以支持双向拖放文件
    - sudo apt install open-vm-tools open-vm-tools-desktop open-vm-tools-dkms

## Python开发环境