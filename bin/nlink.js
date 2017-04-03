#!/usr/bin/env node

'use strict';


/**
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
    fs = require('fs'),
    path = require('path'),
    stat = require('./stat'),
    thunkify = require('./thunkify'),
    bindir = '/usr/local/bin',
    args = process.argv.slice(2),
    cmd = args.shift(),
    cwd = process.cwd();


/**
 ***************************************
 * 调用处理命令
 ***************************************
 */
switch (cmd) {
    case '-d': unlink(args); break;
    default: mklink(); break;
}


/**
 ***************************************
 * 取消链接文件
 ***************************************
 */
async function unlink(args) {

    if (args.length === 0) {

        try {

            // 获取包文件【bin】列表
            args = Object.keys(require(path.resolve(cwd, 'package.json')).bin);

        } catch (e) {
            args = [];
        }
    }

    // 删除定义的【bin】文件
    args.forEach(async name => {
        try {

            let dist = path.resolve(bindir, name);

            // 移除现在的文件
            await stat(dist) && await thunkify(fs.unlink)(dist);
            return console.log(`==> unlink: ${name}`);

        } catch (err) {
            return console.error(err);
        }
    });
}



/**
 ***************************************
 * 添加链接文件
 ***************************************
 */
async function mklink() {
    let bin = null,
        keys = [];

    try {

        // 获取包文件【bin】列表
        bin = require(path.resolve(cwd, 'package.json')).bin;
        keys = Object.keys(bin);

    } catch (e) {
        return false;
    }


    // 添加【bin】链接
    keys.forEach(async name => {

        // 获取源文件地址
        let src = path.resolve(cwd, bin[name]),
            dist = path.resolve(bindir, name);

        try {

            // 移除现在的文件
            await stat(dist) && await thunkify(fs.unlink)(dist);

            // 生成链接
            await thunkify(fs.symlink)(src, dist);
            return console.log(`==> link [${name}]: ${src}`);

        } catch (err) {
            return console.error(err);
        }
    });

}

