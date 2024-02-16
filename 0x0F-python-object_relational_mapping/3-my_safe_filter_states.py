#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql = """SELECT * FROM states WHERE name
        LIKE BINARY %s ORDER BY states.id ASC"""
    cur.execute(sql, (sys.argv[4]))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
