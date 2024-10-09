import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("connection successful")
    except Error as e:
        print(f"the error '{e}' occurred")
    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)  # Execute with parameters
        else:
            cursor.execute(query)  # Execute without parameters
        connection.commit()
        print("query executed successfully")
    except Error as e:
        print(f"the error '{e}' occurred")


def execute_read_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        if params:
            cursor.execute(query, params)  # Execute with parameters
        else:
            cursor.execute(query)  # Execute without parameters
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"the error '{e}' occurred")
