#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入模組
import MySQLdb,threading,sys
from termcolor import colored
from time import gmtime, strftime
from ConfigParser import SafeConfigParser

try:

    time = strftime("%H:%M", gmtime())
    # 連接到 MySQL
    def checker():
        # 執行 SQL 語句
        db = MySQLdb.connect(host, user, password, database, unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock')
        cursor = db.cursor()
        cursor.execute("SELECT `usr_id`, `usr_name`, usr_water, usr_fire, usr_earth, usr_wind FROM `users` WHERE usr_water < 0 OR usr_fire < 0 OR usr_earth < 0 OR usr_wind < 0")
        result = cursor.fetchall()
        if cursor.rowcount == 0 :
            print colored('[LOG] All player card data is normal now. ' + time, 'blue')


        # 輸出結果
        for record in result:
            if record[2] < 0 :
                cursor.execute("UPDATE users SET usr_water = '0' WHERE usr_id = " + str(record[0]))
                db.commit()
                print colored( "[LOG] ID:" + str(record[0]) + ". " + "Name:" + str(record[1]) + ". water white card abnormal, but this fixed. " + time, "red" )
            elif record[3] < 0 :
                cursor.execute("UPDATE users SET usr_fire = '0' WHERE usr_id = " + str(record[0]))
                db.commit()
                print colored( "[LOG] ID:" + str(record[0]) + ". " + "Name:" + str(record[1]) + ". fire white card abnormal, but this fixed. " + time, "red" )
            elif record[4] < 0 :
                cursor.execute("UPDATE users SET usr_earth = '0' WHERE usr_id = " + str(record[0]))
                db.commit()
                print colored( "[LOG] ID:" + str(record[0]) + ". " + "Name:" + str(record[1]) + ". earth white card abnormal, but this fixed."  + time, "red" )
            elif record[5] < 0 :
                cursor.execute("UPDATE users SET usr_wind = '0' WHERE usr_id = " + str(record[0]))
                db.commit()
                print colored( "[LOG] ID:" + str(record[0]) + ". " + "Name:" + str(record[1]) + ". wind white card abnormal, but this fixed."  + time, "red" )
        global t        #Notice: use global variable!
        t = threading.Timer(float(looptime), checker)
        t.start()

    if __name__ == '__main__':
        parser = SafeConfigParser()
        parser.read('config.ini')
        global host, user, password, db, looptime
        host = parser.get('DB', 'ip')
        user = parser.get('DB', 'user')
        password = parser.get('DB', 'pw')
        database = parser.get('DB', 'db')
        looptime = parser.get('CHECKER', 'looptime')
        t = threading.Timer(float(looptime), checker)
        t.start()
except:
    print "Unexpected error:", sys.exc_info()
    raw_input('press enter key to exit')
