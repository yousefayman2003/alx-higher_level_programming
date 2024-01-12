#!/usr/bin/python3
"""Module that deals with SQL injection"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3], port=3306)

    # create a cursor
    cursor = connection.cursor()

    # Execute a parameterized query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id;"
    cursor.execute(query, (argv[4],))

    # loop for each row in the result set
    for row in cursor.fetchall():
        print(row)

    # Close up process
    cursor.close()
    connection.close()
