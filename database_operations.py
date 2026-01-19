# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.

import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """
    Establishes a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'USERS')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

def create_table_if_not_exists(connection):
    """
    Creates users_table if it does not exist.
    """
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'users_table' checked/created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_user(connection, name, email, password):
    """
    Adds a new user to the users_table.
    """
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO users_table (name, email, password)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, password))
        connection.commit()
        print(f"User '{name}' added successfully.")
    except Error as e:
        print(f"Error adding user: {e}")

def get_user_by_name(connection, name):
    """
    Retrieves user details by name.
    """
    try:
        cursor = connection.cursor(dictionary=True)
        search_query = "SELECT * FROM users_table WHERE name = %s"
        cursor.execute(search_query, (name,))
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error searching user: {e}")
        return []
