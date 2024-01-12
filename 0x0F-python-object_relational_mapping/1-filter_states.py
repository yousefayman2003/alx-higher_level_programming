#!/usr/bin/python3
"""Module that lists all states with a name
    starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3], port=3306)

    # create a cursor
    cursor = connection.cursor()
    # execute a query
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                    ORDER BY id;""")

    # loop for each row in the result set
    for row in cursor.fetchall():
        print(row)

    # Close up process
    cursor.close()
    connection.close()
