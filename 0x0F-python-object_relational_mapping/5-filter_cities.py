#!/usr/bin/python3
"""Module that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    connection = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3], port=3306)

    # create a cursor
    cursor = connection.cursor()

    # Execute a query
    query = """SELECT c.name FROM cities c
                JOIN states s on s.id = c.state_id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id;"""
    cursor.execute(query, (argv[4], ))

    cities = []
    # loop for each row in the result set
    for row in cursor.fetchall():
        cities.append(row[0])

    # print cities
    print(", ".join(cities))
    # Close up process
    cursor.close()
    connection.close()
