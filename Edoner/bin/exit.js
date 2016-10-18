#!/usr/bin/env node

'use strict';

const
    path = require('path'),
    json = require('../lib/json'),
    request = require('../lib/request'),
    dir = path.join(__dirname, '.config'),
    config = json(dir);


if (config.state === 'running') {

    // 修复状态
    config.state = 'pending';
    json(dir, config);

    // 发送请求
    request({
        hostname: 'localhost',
        port: config.port,
        path: '/exit',
        method: 'GET'
    });
}
