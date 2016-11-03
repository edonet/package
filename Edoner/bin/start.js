#!/usr/bin/env node

'use strict';

const
    http = require('http'),
    path = require('path'),
    json = require('../lib/json'),
    dir = path.join(__dirname, '.config'),
    config = json(dir);



if (config.state !== 'pending') {
    process.exit(0);
}

// 更新状态【runing】
config.state = 'running';
json(dir, config);


// 创建服务
let onlineSocket = [],
    server = http.createServer((req, res) => {

        // 返回数据
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(`Info: ${req.url}`);

        let args = req.url.split('?');

        switch (args[0]) {

            // 保存文件
            case '/save':
                invokeSaveFile(args[1]);
                break;

            // 退出服务
            case '/exit':
                process.nextTick(() => process.exit(1));
                break;

            default: break;
        }

    }),
    io = require('socket.io')(server);


// 监听【socket】链接事件
io.on('connection', socket => {

    // 添加到链接列表
    onlineSocket.push(socket);

    // 链接成功
    socket.emit('success', 'Connection success!');

    // 断开链接
    socket.on('disconnect', () => {
        onlineSocket = onlineSocket.filter(v => v !== socket);
    });
});

// 监听端口
server.listen(config.port, err => {

    if (err) {
        return console.log(err);
    }

    console.log('');
    console.log('> -------------------------------------------------');
    console.log('> Sublime Text Server listening on: http://localhost: %s', config.port);
    console.log('> open your brower and enjoy it.');
    console.log('> -------------------------------------------------');
    console.log('');
});


// 保存文件
function invokeSaveFile(filename) {
    onlineSocket.forEach(socket => {
        socket.emit('save', filename);
    });
}
