## 树莓派3b安装Node.js

- 9.x版本
```bash
pi@raspberrypi:~ $  node -v
v0.10.29
pi@raspberrypi:~ $  sudo su -
root@raspberrypi:~ # apt-get remove nodered -y
root@raspberrypi:~ # apt-get remove nodejs nodejs-legacy -y
root@raspberrypi:~ # apt-get remove npm  -y # if you installed npm
root@raspberrypi:~ # curl -sL https://deb.nodesource.com/setup_9.x | sudo bash -
root@raspberrypi:~# apt-get install nodejs -y
root@raspberrypi:~# node -v
v9.9.0
root@raspberrypi:~# npm -v
3.7.3
```

- 安装到系统
    - sudo npm install -g puppeteer  --ignore-scripts
    - export NODE_PATH='/usr/local/lib/node_modules'
    - chromium-browser --headless --disable-gpu --print-to-pdf https://www.google.com
