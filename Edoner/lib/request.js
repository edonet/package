'use strict';

const
    http = require('http');


module.exports = (options, callback) => {

    // 发送请求
    let request = http.request(options, res => {

            // 输出返回头
            console.log('STATUS: ' + res.statusCode);
            console.log('HEADERS: ' + JSON.stringify(res.headers));

            // 输出返回体
            res.setEncoding('utf8');
            res.on('data', chunk => {
                console.log('BODY: ' + chunk);
            });

            // 结束返回体
            res.on('finish', () => {
                callback && callback();
            });
        });


    // 监听错误信息
    request.on('error', e => {
        callback && callback(e);
        console.log('problem with request: ' + e.message);
    });

    // 结束请求
    request.end();
};
