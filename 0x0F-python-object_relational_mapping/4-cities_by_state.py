#!/usr/bin/python3
"""Module that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3], port=3306)

    # create a cursor
    cursor = connection.cursor()

    # Execute a query
    query = """SELECT c.id, c.name, s.name FROM cities c
                JOIN states s on s.id = c.state_id
                ORDER BY c.id;"""
    cursor.execute(query)

    # loop for each row in the result set
    for row in cursor.fetchall():
        print(row)

    # Close up process
    cursor.close()
    connection.close()
