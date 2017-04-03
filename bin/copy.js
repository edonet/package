'use strict';


/**
 ***************************************
 * 加载依赖模块
 ***************************************
 */
const
    fs = require('fs');


/**
 ***************************************
 * 定义复制函数
 ***************************************
 */
async function copy(src, dist) {

    // 返回【Promise】对象
    return await new Promise((resolve, reject) => {

        // 创建输入输出流
        let rs = fs.createReadStream(src),
            ws = fs.createWriteStream(dist);


        // 监听完成信息
        ws.on('close', () => resolve([src, dist]));

        // 监听错误信息
        rs.on('error', err => reject(err));
        ws.on('error', err => reject(err));

        // 开始传输数据
        rs.pipe(ws);
    });
}


/**
 ***************************************
 * 输出接口
 ***************************************
 */
module.exports = copy;
