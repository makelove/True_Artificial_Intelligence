## 使用ssl加密传输数据

- 小心
    - 在MacOS测试这些代码，会把证书加入到【钥匙串】中，导致【联系不上iCloud】，一些依赖【钥匙串】的软件会保存，例如Chrome

- 参考
    - [Python中使用ssl加密](https://blog.csdn.net/robin912/article/details/44497355)
    
- 使用openssl产生证书
    - openssl req -new -x509 -days 365 -nodes -out mycertfile.pem -keyout mykeyfile.pem