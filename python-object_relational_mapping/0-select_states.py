#!/usr/bin/python3
''' Script that lists all states from database hbtn_0e_0_usa '''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=mysql_username,
                                 passwd=mysql_password,
                                 db=database_name
                                 )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
