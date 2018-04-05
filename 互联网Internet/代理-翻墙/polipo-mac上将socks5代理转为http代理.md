## mac上将socks5代理转为http代理
- http://blog.fatedier.com/2015/09/20/trans-socks5-proxy-to-http-proxy-on-mac/

- polipo已经停止了维护，Proxychains也是一款优秀的代理软件，Proxychains#78,但是由于Mac的sip保护，导致了Proxychains无法正常工作(OS X 10.11版本以上都GG)

- 另外由于shadowsocks的代理类型是socks5，所以直接的export http_proxy=http://proxyAddress:port并不能起作用。



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

- 在.bash_profile里设置-别名 
    - alias hp="http_proxy=http://localhost:8123"

```bash
#proxy
export http_proxy="http://127.0.0.1:8123/"
export https_proxy="http://127.0.0.1:8123/"
export ftp_proxy="http://127.0.0.1:8123/"
export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
export HTTP_PROXY="http://127.0.0.1:8123/"
export HTTPS_PROXY="http://127.0.0.1:8123/"
export FTP_PROXY="http://127.0.0.1:8123/"
export NO_PROXY="localhost,127.0.0.1,localaddress,.localdomain.com"
polipo socksParentProxy=127.0.0.1:1080
```

- iPhone-Android手机使用macOS已经建立好的代理服务
    - polipo socksParentProxy=localhost:1080 proxyAddress=0.0.0.0
    
```bash
(.py3) pro:~ play$ curl ip.gs
Current IP / 当前 IP: 115.171.61.110
ISP / 运营商:  ChinaTelecom
City / 城市: Beijing Beijing
Country / 国家: China
IP.GS is now IP.SB, please visit https://ip.sb/ for more information. / IP.GS 已更改为 IP.SB ，请访问 https://ip.sb/ 获取更详细 IP 信息！
Please join Telegram group https://t.me/sbfans if you have any issues. / 如有问题，请加入 Telegram 群 https://t.me/sbfans

  /\_/\
=( °w° )=
  )   (  //
 (__ __)//


(.py3) pro:~ play$ http_proxy=http://localhost:8123 curl ip.gs
Current IP / 当前 IP: 54.145.10.6
ISP / 运营商:  amazon.com
City / 城市: Ashburn Virginia
Country / 国家: United States
IP.GS is now IP.SB, please visit https://ip.sb/ for more information. / IP.GS 已更改为 IP.SB ，请访问 https://ip.sb/ 获取更详细 IP 信息！
Please join Telegram group https://t.me/sbfans if you have any issues. / 如有问题，请加入 Telegram 群 https://t.me/sbfans

  /\_/\
=( °w° )=
  )   (  //
 (__ __)//


(.py3) pro:~ play$ curl ip.cn
当前 IP：115.171.61.110 来自：北京市 电信

(.py3) pro:~ play$ http_proxy=http://localhost:8123 curl ip.cn
当前 IP：54.145.10.6 来自：美国 Amazon

```    

- 很多选项，任你配置
```bash
(.py3) pro:~ play$ polipo --help
polipo [ -h ] [ -v ] [ -x ] [ -c filename ] [ -- ] [ var=val... ]
  -h: display this message.
  -v: display the list of configuration variables.
  -x: perform expiry on the disk cache.
  -c: specify the configuration file to use.
  
  
(.py3) pro:~ play$ polipo -v
Disabling disk cache: No such file or directory
configFile (none) Configuration file.
CHUNK_SIZE 8192 Unit of chunk memory allocation.
allowUnalignedRangeRequests boolean false Allow unaligned range requests (unreliable).
allowedClients list (not set) Networks from which clients are allowed to connect.
allowedPorts intlist 80-100, 1024-65535 Ports to which connections are allowed.
alwaysAddNoTransform boolean false If true, add a no-transform directive to all requests.
authCredentials atom (hidden) username:password.
authRealm atom (none) Authentication realm.
bigBufferSize integer 32768 Size of big buffers (max size of headers).
cacheIsShared boolean true If false, ignore s-maxage and private.
censorReferer tristate false Censor referer headers.
censoredHeaders list (empty list) Headers to censor.
chunkCriticalMark integer 24772608 Critical mark for chunk memory (0 = auto).
chunkHighMark integer 25165824 High mark for chunk memory.
chunkLowMark integer 18874368 Low mark for chunk memory (0 = auto).
clientTimeout time 2m Client-side timeout.
daemonise boolean false Run as a daemon
disableConfiguration boolean false Disable reconfiguring Polipo at runtime.
disableIndexing boolean true Disable indexing of the local cache.
disableLocalInterface boolean false Disable the local configuration pages.
disableProxy boolean false Whether to be a web server only.
disableServersList boolean true Disable the list of known servers.
disableVia boolean true Don't use Via headers.
diskCacheDirectoryPermissions integer 0700 Access rights for new directories.
diskCacheFilePermissions integer 0600 Access rights for new cache files.
diskCacheRoot atom (none) Root of the disk cache.
diskCacheTruncateSize integer 1048576 Size to which on-disk objects are truncated.
diskCacheTruncateTime time 4d12h Time after which on-disk objects are truncated.
diskCacheUnlinkTime time 32d Time after which on-disk objects are removed.
diskCacheWriteoutOnClose integer 65536 Number of bytes to write out eagerly.
displayName atom Polipo Server name displayed on error pages.
dnsGethostbynameTtl time 20m TTL for gethostbyname addresses.
dnsMaxTimeout time 1m Max timeout for DNS queries.
dnsNameServer atom 192.168.0.1 The name server to use.
dnsNegativeTtl time 2m TTL for negative DNS replies with no TTL.
dnsQueryIPv6 4-state happily Query for IPv6 addresses.
dnsUseGethostbyname 4-state reluctantly Use the system resolver.
dontCacheCookies boolean false Work around cachable cookies.
dontCacheRedirects boolean false If true, don't cache redirects.
dontTrustVaryETag tristate maybe Whether to trust the ETag when there's Vary.
expectContinue tristate maybe Send Expect-Continue to servers.
forbiddenFile atom (none) File specifying forbidden URLs.
forbiddenRedirectCode integer 302 Redirect code, 301 or 302.
forbiddenTunnelsFile atom (none) File specifying forbidden tunnels.
forbiddenUrl atom (none) URL to which forbidden requests should be redirected.
idleTime time 20s Time to remain idle before writing out.
laxHttpParser boolean true Ignore unknown HTTP headers.
localDocumentRoot atom /usr/local/Cellar/polipo/1.1.1/share/polipo/www/ Root of the local tree.
logFacility atom user Syslog facility to use.
logFile atom (none) Log file (stderr if empty and logSyslog is unset, /var/log/polipo if empty and daemonise is true).
logFilePermissions integer 0640 Access rights of the logFile.
logLevel integer 0x7 Logging level (max = 0xFF).
logSyslog boolean false Log to syslog.
maxAge time 14d1h Max age for objects without Expires header.
maxAgeFraction float 0.100000 Fresh fraction of modification time.
maxConnectionAge time 21m Maximum age of a server-side connection.
maxConnectionRequests integer 400 Maximum number of requests on a server-side connection.
maxDiskCacheEntrySize integer -1 Maximum size of objects cached on disk.
maxDiskEntries integer 32 File descriptors used by the on-disk cache.
maxExpiresAge time 30d1h Max age for objects with Expires header.
maxNoModifiedAge time 23m Max age for objects without Last-modified.
maxObjectsWhenIdle integer 32 Number of objects to write at a time when idle.
maxPipelineTrain integer 10 Maximum number of requests pipelined at a time.
maxSideBuffering integer 1500 Maximum buffering for PUT and POST requests.
maxWriteoutWhenIdle integer 65536 Amount of data to write at a time when idle.
mindlesslyCacheVary boolean false If true, mindlessly cache negotiated objects.
objectHashTableSize integer 32768 Size of the object hash table (0 = auto).
objectHighMark integer 2048 High object count mark.
parentAuthCredentials atom (hidden) username:password.
parentProxy atom (none) Parent proxy (host:port).
pidFile atom (none) File with pid of running daemon.
pipelineAdditionalRequests tristate maybe Pipeline requests on an active connection.
pmmFirstSize integer 0 The size of the first PMM chunk.
pmmSize integer 0 The size of a PMM chunk.
preciseExpiry boolean false Whether to consider all files for purging.
proxyAddress atom 127.0.0.1 The IP address on which the proxy listens.
proxyName atom pro.lan The name by which the proxy is known.
proxyOffline boolean false Avoid contacting remote servers.
proxyPort integer 8123 The TCP port on which the proxy listens.
publicObjectLowMark integer 1024 Low object count mark (0 = auto).
redirector atom (none) Squid-style redirector.
redirectorRedirectCode integer 302 Redirect code to use with redirector.
relaxTransparency tristate false Avoid contacting remote servers.
replyUnpipelineSize integer 1048576 Size for a pipeline break.
replyUnpipelineTime time 20s Estimated time for a pipeline break.
scrubLogs boolean false If true, don't include URLs in logs.
serverExpireTime time 1d Time during which server data is valid.
serverIdleTimeout time 45s Server-side idle timeout.
serverMaxSlots integer 8 Maximum number of connections per broken server.
serverSlots integer 2 Maximum number of connections per server.
serverSlots1 integer 4 Maximum number of connections per HTTP/1.0 server.
serverTimeout time 1m30s Server-side timeout.
smallRequestTime time 10s Estimated time for a small request.
socksParentProxy atom (none) SOCKS parent proxy (host:port)
socksProxyType atom socks5 One of socks4a or socks5
socksUserName atom (empty) SOCKS4a user name
tunnelAllowedPorts intlist 22, 80, 109-110, 143, 443, 873, 993, 995, 2401, 5222-5223, 9418 Ports to which tunnelled connections are allowed.
uncachableFile atom (none) File specifying uncachable URLs.
```