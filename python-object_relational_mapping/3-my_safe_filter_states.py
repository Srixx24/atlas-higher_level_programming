#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states(username, password, database, state_name):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        cursor = db.cursor()

        command = "SELECT * FROM states " \
                "WHERE name=%s " \
                "ORDER BY id ASC"
        cursor.execute(command, (state_name,))

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
    state_name = sys.argv[4]

    list_states(username, password, database, state_name)
