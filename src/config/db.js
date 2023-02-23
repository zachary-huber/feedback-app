const mysql = require('mysql');
const db = mysql.createConnection({
    host: 'database-1.cjozimxhtixf.us-east-1.rds.amazonaws.com',
    user: 'admin',
    password: 'database',
    database: 'database-1'
});

module.exports = db;