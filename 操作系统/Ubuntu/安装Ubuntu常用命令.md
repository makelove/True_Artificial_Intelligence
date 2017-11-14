# 安装Ubuntu后常做步骤

- 总是要：下载最新版Ubuntu
    - https://www.ubuntu.com/download/desktop

## 常用软件
- sudo apt update
- 删除libreoffice
    - sudo apt-get remove --purge libreoffice*
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



## Python开发环境