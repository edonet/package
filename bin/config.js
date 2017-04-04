#!/usr/bin/env node

'use strict';


/*
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
    os = require('os'),
    path = require('path'),
    symlink = require('./symlink'),
    config = require('../config.json'),
    cwd = process.cwd(),
    homedir = os.homedir();


/*
 ***************************************
 * 执行生成【home】配置
 ***************************************
 */
symlink(
    path.resolve(cwd, 'settings'),
    homedir,
    config.settings || []
);

/*
 ***************************************
 * 执行生成【bin】目录
 ***************************************
 */
symlink(
    path.resolve(cwd, 'node_modules'),
    homedir,
    ['.bin']
);

/*
 ***************************************
 * 执行生成【mpv】配置目录
 ***************************************
 */
symlink(
    cwd,
    path.resolve(homedir, '.config'),
    ['mpv']
);
