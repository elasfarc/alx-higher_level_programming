#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
  table of hbtn_0e_0_usa where name matches the argument.
  sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":

    (_, SQL_USR, SQL_PASSWD, DB_NAME, search) = sys.argv

    db = MySQLdb.connect(
      host="localhost", user=SQL_USR, password=SQL_PASSWD,
      database=DB_NAME, port=3306)

    cur = db.cursor()
    cur.execute("""
      SELECT * from states
      WHERE name like '{}'
      ORDER BY id
      """.format(search))
    results = cur.fetchall()
    for res in results:
        print(res)

    cur.close()
    db.close()
