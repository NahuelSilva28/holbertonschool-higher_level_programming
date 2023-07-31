#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def get_cities_by_state(username, password, database):
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
            # SQL query with JOIN to get cities and their corresponding states
            query = "SELECT cities.id, cities.name, states.name FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     ORDER BY cities.id ASC"
            cursor.execute(query)
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
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    get_cities_by_state(username, password, database)

