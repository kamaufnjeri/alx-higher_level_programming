#!/usr/bin/python3
"""Using MySQLdb to read from database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    query = cur.fetchall()
    for i in query:
        print(i)
    cur.close()
    db.close()
