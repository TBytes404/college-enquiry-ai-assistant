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
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS queries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        query TEXT NOT NULL,
        answer TEXT NOT NULL
    );
    """
    cursor = connection.cursor()
    try:
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_query(connection, query, answer):
    insert_query = """
    INSERT INTO queries (query, answer)
    VALUES (%s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(insert_query, (query, answer))
    connection.commit()
    return cursor.lastrowid

def main():
    connection = create_connection("localhost", "root", "tuhin2003@#", "chatbot")
    if connection is not None:
        create_table(connection)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()