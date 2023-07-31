#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def filter_cities_by_state(username, password, database, state_name):
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
            # SQL query to get cities of the given state
            query = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities \
                     WHERE state_id = (SELECT id FROM states WHERE name = %s)"
            cursor.execute(query, (state_name,))
            result = cursor.fetchone()[0]

            # Print the cities if there are any, otherwise print nothing
            if result:
                print(result)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
    finally:
        db.close()

# Check if the script is being run directly, not imported as a module
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    filter_cities_by_state(username, password, database, state_name)

