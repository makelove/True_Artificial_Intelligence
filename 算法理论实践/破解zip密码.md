## 破解zip密码

- 参考
    - [使用fcrackzip破解zip保护密码](http://topspeedsnail.com/fcrackzip-crack-zip-password/)
    
- 安装使用
    - sudo apt-get install fcrackzip
    - 创建 带密码zip文件
        - zip --password 12345 crack_this.zip test.txt 
    - 穷举法
        - fcrackzip -b -c 'aA1!' -l 1-10 -u crack_this.zip
    - 使用字典
        - fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u crack_this.zip