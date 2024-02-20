#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states(username, password, database):

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                port=3306,
                passwd=password,
                db=database
                )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
