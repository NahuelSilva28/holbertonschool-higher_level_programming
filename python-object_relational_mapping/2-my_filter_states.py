#!/usr/bin/python3
"""
This script retrieves and displays all values in the states table of hbtn_0e_0_usa
where the name matches the user-provided argument.
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
            # Use format to create the SQL query with the user input
            query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
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
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    filter_states_by_name(username, password, database, state_name)

