#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(username, password, database):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        cursor = db.cursor()

        command = "SELECT * FROM cities ORDER BY id ASC"
        cursor.execute(command)

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

    list_cities(username, password, database)
