#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
            WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
