## mac上将socks5代理转为http代理
- http://blog.fatedier.com/2015/09/20/trans-socks5-proxy-to-http-proxy-on-mac/

在 mac 上使用 ss 的时候创建的是 socks5 代理，浏览器可以正常设置使用，不过在 shell 中一些程序无法使用 socks5 代理，而需要使用 http 代理，通过设置 http_proxy 环境变量，就可以让 shell 通过 http 代理来访问网络。polipo 这款工具就可以帮助我们将 socks5 代理转换为 http 代理。

- 安装
我们使用 homebrew 来安装 polipo。

brew install polipo

- 创建 http 代理
假设我们 ss 的 socks5 代理端口为 1080。

- polipo socksParentProxy=localhost:1080

执行这条命令后一个 http 代理就已经创建好了，默认监听的端口为 8123。

我们设置 http 代理端口为 8123 后就可以使用 ss 访问网络。

使用 http 代理
例如我们使用 wget 获取 google 的首页数据。

- http_proxy=http://127.0.0.1:8123 wget http://www.google.com


- iPhone-Android手机使用macOS已经建立好的代理服务
    - polipo socksParentProxy=localhost:1080 proxyAddress=0.0.0.0