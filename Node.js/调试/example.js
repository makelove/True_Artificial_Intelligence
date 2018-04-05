var http = require('http');
var url = require('url');
//基于Nodejs内建的调试器
debugger;


http.createServer(function (req, res) {
        var path = url.parse(req.url).pathname;
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end(path);
}).listen(1337, "127.0.0.1");
console.log('Server running at http://127.0.0.1:1337/');