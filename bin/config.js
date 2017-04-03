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
    homedir = os.homedir(),
    settings = path.resolve(cwd, 'settings');


/*
 ***************************************
 * 执行生成【home】配置
 ***************************************
 */
symlink(
    settings,
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
