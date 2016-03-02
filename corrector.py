#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入 MySQL 模組
import MySQLdb

# 連接到 MySQL
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="spgame", unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock')
cursor = db.cursor()

# 執行 SQL 語句
cursor.execute("SELECT * FROM `users` WHERE `usr_water` < 0 OR `usr_fire` < 0 OR `usr_earth` < 0 OR `usr_wind` < 0")
result = cursor.fetchall()

# 輸出結果
for record in result:
    print record
