'use strict';


/**
 *******************************
 * 加载依赖
 *******************************
 */
const
    fs = require('fs'),
    path = require('path'),
    stat = require('./stat');

/**
 *******************************
 * 定义软链接方法
 *******************************
 */
function symlink(src, dist, files) {

    // 遍历需要链接的文件
    files.length && files.forEach(async function(file) {

        // 获取输入、输出路径
        let srcFile = path.resolve(src, file),
            distFile = path.resolve(dist, file),
            stats = await stat(distFile);

        // 输出关联目录
        console.log(`==> ${srcFile} : ${distFile}`);

        // 不存在目标文件时，直接创建链接
        if (!stats) {
            return fs.symlink(srcFile, distFile, err => err && console.error(err));
        }

        // 删除目标文件
        fs.unlink(distFile, err => {

            // 输出错误信息
            if (err) {
                return console.error(err);
            }

            // 生成软链接
            fs.symlink(srcFile, distFile, err => err && console.error(err));
        });
    });
}


/**
 *******************************
 * 抛出接口
 *******************************
 */
module.exports = symlink;
