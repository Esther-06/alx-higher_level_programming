#!/usr/bin/python3
"""
return matching states
parameters given to script: username, password, database, state to match
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":)
     # connect to database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # create cursor to exec queries using SQL; match arg given
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
    cursor.close()
    db.close()
