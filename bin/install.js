#!/usr/bin/env node

'use strict';


/*
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
	symlink = require('./symlink');


/*
 ***************************************
 * 执行生成软链接命令
 ***************************************
 */
symlink(
	process.cwd(),
	process.argv.slice(2)[0],
	require('../config.json').packages || []
);
