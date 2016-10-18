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
http
    .createServer((req, res) => {

        let url = req.url;

        switch (url) {

            // 退出服务
            case '/exit':
                process.nextTick(() => process.exit(1));
                break;

            default: break;
        }

        // 返回数据
        res.writeHead(200, {'Content-Type': 'text/html'});
        return res.end(`Info: ${url}`);

    })
    .listen(config.port, err => {

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

