#!/usr/bin/python3
"""
This script retrieves and lists all states from the database hbtn_0e_0_usa
where the name matches the user-provided argument.
It requires four arguments: mysql username, mysql password, database name, and state name to search.
It utilizes the MySQLdb module for database connectivity.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import sys
import MySQLdb


def filter_states_by_name(username, password, database, state_name):
    try:
        # Connect to the database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        with db.cursor() as cursor:
            query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
            cursor.execute(query, (state_name,))
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
    finally:
        db.close()

# Check if the script is being run directly, not imported as a module
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    filter_states_by_name(username, password, database, state_name)

