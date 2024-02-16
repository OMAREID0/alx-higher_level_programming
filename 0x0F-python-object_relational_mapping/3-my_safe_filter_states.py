#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql = """SELECT * FROM states WHERE name
        LIKE %s ORDER BY states.id ASC"""
    state = sys.argv[4]
    cur.execute(sql, state)
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
