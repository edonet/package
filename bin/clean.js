#!/usr/bin/env node

'use strict';


/*
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
    os = require('os'),
    fs = require('fs'),
    path = require('path'),
    stat = require('./stat'),
    config = require('../config.json'),
    homedir = os.homedir();


/*
 ***************************************
 * 移除配置文件
 ***************************************
 */
function remove(dir, files) {
    files.length && files.forEach(async file => {

        // 获取文件路径
        let filePath = path.resolve(dir, file),
            stats = await stat(filePath);

        if (stats) {

            // 删除目标文件
            fs.unlink(filePath, err => {

                // 输出错误信息
                if (err) {
                    return console.error(err);
                }

                console.log(`==> remove: ${filePath}`);
            });
        }
    });
}


/*
 ***************************************
 * 移除配置文件
 ***************************************
 */
remove(homedir, ['.bin']);
remove(homedir, config.settings);
remove('/usr/local/bin', config.bin);
