## 安装python-libtorrent
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