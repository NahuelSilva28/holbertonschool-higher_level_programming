#!/usr/bin/python3
"""
This script retrieves and lists all states from the database hbtn_0e_0_usa.
It requires three arguments: mysql username, mysql password, and database name.
It utilizes the MySQLdb module for database connectivity.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import sys
import MySQLdb

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
        cursor.execute("SELECT * FROM states ORDER BY id")
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

# Check if the script is being run directly, not imported as a module
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    get_states(username, password, database)

