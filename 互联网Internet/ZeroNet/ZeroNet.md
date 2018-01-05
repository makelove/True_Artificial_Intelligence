## ZeroNet
- 参考
    - [官方中文介绍](https://github.com/HelloZeroNet/ZeroNet/blob/master/README-zh-cn.md)
    - [开放的零网与个人站点尝试](https://www.jianshu.com/p/b7f8d56335ca)
    - [ZeroNet会颠覆现有的Internet网络吗？](https://zhuanlan.zhihu.com/p/24923913)

- 安装
    - https://zeronet.io/
    
- 运行 下载的程序,便会自动打开浏览器
    - 随便玩
- 在Docker里运行
    - docker pull nofish/zeronet
    - 新建文件夹 Zeronet
    - docker run -d -v Zeronet:/root/data -p 15441:15441 -p 43110:43110 nofish/zeronet
        - 可选:打开Tor
            - docker run -d -e "ENABLE_TOR=true" -v Zeronet:/root/data -p 15441:15441 -p 43110:43110 nofish/zeronet
    - 打开浏览器http://127.0.0.1:43110/