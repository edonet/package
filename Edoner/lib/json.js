'use strict';

const
    fs = require('fs');


module.exports = (dir, data) => {
    return data ?
        fs.writeFileSync(dir, JSON.stringify(data, null, 4)) :
        JSON.parse(fs.readFileSync(dir));
};
