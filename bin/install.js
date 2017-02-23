#!/usr/bin/env node

'use strict';


/*
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
	fs = require('fs'),
	path = require('path'),
	packages = require('../package.json').packages || [],
	cwd = process.cwd(),
	dir = process.argv.slice(2)[0];


/*
 ***************************************
 * 执行生成软链接命令
 ***************************************
 */
packages.length && packages.forEach(name => {

	// 获取输入、输出路径
	let src = path.resolve(cwd, name),
		dist = path.resolve(dir, name);

	// 输出关联目录
	console.log(`--> ${src} : ${dist}`);

	// 生成软链接
	fs.symlink(src, dist, err => err && console.error(err));
});
