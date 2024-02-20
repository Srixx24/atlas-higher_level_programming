#!/usr/bin/python3
"""
Lists all states with a name starting with N.
"""
import MySQLdb
import sys


def list_states(username, password, database):
    try:
        db = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=username,
                            passwd=password,
                            db=database)

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

	except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))

    finally:
        if db:
            db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
