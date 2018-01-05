## 安装python-libtorrent

- 参考
    - [BT下载与用python轻松自建种子搜索引擎](https://www.jianshu.com/p/f1659aba5aed)
    - [磁力链接是如何实现下载的？](http://www.aneasystone.com/archives/2015/05/how-does-magnet-link-work.html)
    - >根据BitTorrent协议，文件发布者会根据要发布的文件生成提供一个.torrent文件，即种子文件，也简称为“种子”。 种子文件本质上是文本文件，包含Tracker信息和文件信息两部分。Tracker信息主要是BT下载中需要用到的Tracker服务器的地址和针对Tracker服务器的设置，文件信息是根据对目标文件的计算生成的，计算结果根据BitTorrent协议内的Bencode规则进行编码。它的主要原理是需要把提供下载的文件虚拟分成大小相等的块，块大小必须为2k的整数次方（由于是虚拟分块，硬盘上并不产生各个块文件），并把每个块的索引信息和Hash验证码写入种子文件中；所以，种子文件就是被下载文件的“索引”。 下载者要下载文件内容，需要先得到相应的种子文件，然后使用BT客户端软件进行下载。 下载时，BT客户端首先解析种子文件得到Tracker地址，然后连接Tracker服务器。Tracker服务器回应下载者的请求，提供下载者其他下载者（包括发布者）的IP。下载者再连接其他下载者，根据种子文件，两者分别告知对方自己已经有的块，然后交换对方所没有的数据。此时不需要其他服务器参与，分散了单个线路上的数据流量，因此减轻了服务器负担。 下载者每得到一个块，需要算出下载块的Hash验证码与种子文件中的对比，如果一样则说明块正确，不一样则需要重新下载这个块。这种规定是为了解决下载内容准确性的问题。 一般的HTTP/FTP下载，发布文件仅在某个或某几个服务器，下载的人太多，服务器的带宽很易不胜负荷，变得很慢。而BitTorrent协议下载的特点是，下载的人越多，提供的带宽也越多，下载速度就越快。同时，拥有完整文件的用户也会越来越多，使文件的“寿命”不断延长。

- 安装
    - 不行pip install python-libtorrent
    - Linux
        - [How to install python-libtorrent in virtualenv](http://dreamingpotato.com/2015/11/21/how-to-install-python-libtorrent-in-virtualenv/)
        - sudo apt-get install python-libtorrent
        - sudo apt-get install python3-libtorrent
            - ln -s  /usr/lib/python3/dist-packages/libtorrent.cpython-35m-x86_64-linux-gnu.so ~/.py3/lib/python3.5/site-packages/libtorrent.so
            - OK
    - macOS
        - [macOS 下试着编译 libtorrent with python3](https://www.fdb713.com/archives/1054)
        - py2:不太行https://superuser.com/questions/549509/how-do-you-install-libtorrent-rasterbar-python-bindings-with-a-brewed-python
            - brew install libtorrent-rasterbar --with-python 
            - mkdir -p /Users/filip/Library/Python/2.7/lib/python/site-packages
             - echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/filip/Library/Python/2.7/lib/python/site-packages/homebrew.pth
         - py2,可以了
            - brew install libtorrent-rasterbar --enable-python-binding --with-python --with-boost-python=mt
            - ln -s /usr/local/lib/python2.7/site-packages/libtorrent.so ~/.py2/lib/python2.7/site-packages/libtorrent.so
            - 搞定
         - py3:不支持
             - 不行brew install libtorrent-rasterbar --with-python3


- 测试
```python
import libtorrent as bt
info = bt.torrent_info('avator.torrent')
info
print("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))
#magnet:?xt=urn:btih:539390d341f8c18400052ed905f77e48d6ebe40e&dn=Avatar ECE (2009) [1080p]
magnet="magnet:?xt=urn:btih:%s"%info.info_hash()
```

- macOS
```bash
brew info libtorrent-rasterbar
libtorrent-rasterbar: stable 1.1.6 (bottled), HEAD
C++ bittorrent library by Rasterbar Software
https://www.libtorrent.org/
/usr/local/Cellar/libtorrent-rasterbar/1.1.6 (232 files, 24.6MB) *
  Built from source on 2018-01-04 at 11:10:07 with: --with-python
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/libtorrent-rasterbar.rb
==> Dependencies
Build: pkg-config ✔
Required: openssl ✔, boost ✔
Optional: python ✔
==> Options
--with-python
	Build with python support
--HEAD
	Install HEAD version
```