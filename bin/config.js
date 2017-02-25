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
    settings = require('../package.json').settings || [],
    cwd = process.cwd(),
    dir = os.homedir();


/*
 ***************************************
 * 执行生成软链接命令
 ***************************************
 */
settings.length && settings.forEach(name => {

    // 获取输入、输出路径
    let src = path.resolve(cwd, 'Settings/', name),
        dist = path.resolve(dir, name);

    // 输出关联目录
    console.log(`==> ${src} : ${dist}`);

    // 生成软链接
    fs.symlink(src, dist, err => err && console.error(err));
});
