'use strict';

/*
 ***************************************
 * 加载依赖模块
 ***************************************
 */

const
    path = require('path'),
    copy = require('./copy'),
    cwd = process.cwd();


/*
 ***************************************
 * 执行生成【hosts】配置
 ***************************************
 */
copy(path.resolve(cwd, 'settings/hosts'), '/etc/hosts')
    .then(res => console.log(`==> ${res[0]} : ${res[1]}`))
    .catch(err => console.error(err));

