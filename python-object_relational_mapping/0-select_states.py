#!/usr/bin/env python3
"""0. Get all states
mandatory
Write a script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

def get_states(username, password, database):
    try:
        # Connect to the database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        cursor.execute("SELECT MIN(id), name FROM states GROUP BY name ORDER BY MIN(id) ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    get_states(username, password, database)
