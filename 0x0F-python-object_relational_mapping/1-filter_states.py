#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa
  with a name starting with N
  sorted in ascending order by states.id
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    (_, SQL_USR, SQL_PASSWD, DB_NAME) = argv

    db = MySQLdb.connect(
      host="localhost", user=SQL_USR, password=SQL_PASSWD,
      database=DB_NAME, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * from  states WHERE name LIKE 'N%' ORDER BY id")
    results = cur.fetchall()

    for res in results:
        print(res)

    cur.close()
    db.close()
