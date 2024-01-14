#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
  sorted in ascending order by cities.id
"""
import MySQLdb
import sys

if __name__ == "__main__":

    (_, SQL_USR, SQL_PASSWD, DB_NAME) = sys.argv

    db = MySQLdb.connect(
      host="localhost", user=SQL_USR, password=SQL_PASSWD,
      database=DB_NAME, port=3306)

    cur = db.cursor()
    cur.execute("""
      SELECT c.id, c.name, s.name FROM cities c
      INNER JOIN states s
      WHERE c.state_id = s.id
      ORDER BY s.id
      """)
    results = cur.fetchall()
    for res in results:
        print(res)

    cur.close()
    db.close()
