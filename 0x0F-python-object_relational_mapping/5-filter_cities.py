#!/usr/bin/python3
"""script that takes in the name of a state as an argument
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    (_, SQL_USR, SQL_PASSWD, DB_NAME, state_name) = sys.argv

    db = MySQLdb.connect(
      host="localhost", user=SQL_USR, password=SQL_PASSWD,
      database=DB_NAME, port=3306)

    cur = db.cursor()
    cur.execute("""
      SELECT c.name FROM cities c
      INNER JOIN states s
      WHERE c.state_id = s.id AND s.name=(%s)
      ORDER BY c.id
      """, (state_name,))
    results = cur.fetchall()

    for i, res in enumerate(results):
        print(f"{res[0]}{', ' if i + 1 != len(results) else ''}", end='')
    print("")

    cur.close()
    db.close()
