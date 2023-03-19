#!/usr/bin/python3
"""
return states starting with 'N'
parameters given to script: sername, passwaord, database
"""

import MySQLdb
from sys import argv

if__name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    #connect to database
    db= MySQLdb.connect(host="localhost",
                        port=3306,
                        user=username,
                        passwd=password,
                        db=db_name)

    #create cursor to exec queries using SQL; filter names starting with 'N'
    cursor = db.cursor()
    cursor.execute("SELECT *FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
