#!/usr/bin/python3
"""Using MySQL"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name\
            FROM cities c INNER JOIN states s\
            ON c.state_id = s.id\
            WHERE s.name = %s\
            ORDER BY c.id ASC", (sys.argv[4], ))
    query = cur.fetchall()
    cities = []
    for row in query:
        cities.append(row[0])
    print(", ".join(cities))
    cur.close()
    db.close()
