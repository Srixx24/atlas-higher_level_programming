#!/usr/bin/python3
"""
Lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        cursor = db.cursor()

        command = "SELECT cities.id, cities.name, states.name " \
                "FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC"
                "LIMIT 2"
        cursor.execute(command, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            city = row[1]
            state = row[2]
            print("{}, {}".format(city, state))

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

    list_cities_by_state(username, password, database, state_name)
