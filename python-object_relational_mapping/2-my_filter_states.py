#!/usr/bin/python3
""" Script that displays all values where name matches given argument """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=mysql_username,
                                 passwd=mysql_password,
                                 db=database_name
                                 )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(state_name)
        )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
