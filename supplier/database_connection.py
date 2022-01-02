import psycopg2
from config import *


def connect_to_db():
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
    return record


def db_start():
    connection = psycopg2.connect(
        user=user, password=password, host=host, port=port, database=database,
    )
    cursor = connection.cursor()
    return cursor, connection


def db_query(query):
    try:
        cursor, connection = db_start()
        cursor.execute(query)
        record = cursor.fetchall()
        # print(record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        db_finish(connection, cursor)

    return record


def db_finish(connection, cursor):
    if connection:
        cursor.close()
        connection.close()


foo = db_query("SELECT * FROM ingredient_schema LIMIT 3")

for ingr in foo:
    print(ingr[1])

# print(db_query("SELECT * FROM ingredient_schema LIMIT 3"))
