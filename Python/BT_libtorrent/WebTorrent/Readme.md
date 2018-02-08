# WebTorrent
- 参考
    - [Get Started with WebTorrent](https://webtorrent.io/intro)

- 测试
    - 打开 https://instant.io/ ，上传一个视频文件，要小，复制[Magnet URI]
    - 在test2.html中修改id="torrentLink" 为[Magnet URI]
```html
<a id="torrentLink" href="magnet:?xt=urn:btih:b99afed0e59957be8626a18fd3cebc84e06d4604&dn=banana.mp4&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com">banana.torrent</a>
``` 
- 修改torrentId    
```javascript
var torrentId = 'magnet:?xt=urn:btih:b99afed0e59957be8626a18fd3cebc84e06d4604&dn=banana.mp4&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com'
```    
- 把html文件放到HTTP服务器，打开网址，http://localhost:63342/WebTorrent/test2.html?_ijt=nciqmlopnkk2k5rm6artil5515
    - 就会自动播放视频文件