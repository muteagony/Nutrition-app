import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        user=user, password=password, host=host, port=port, database=database,
    )

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL query
    cursor.execute("SELECT * FROM vitamin_schema;")
    record = cursor.fetchall()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

