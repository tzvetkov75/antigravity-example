# Audo added TEXT-123
import os
import mysql.connector
from users_db import create_users_table, add_user, get_db_connection

def example_users_usage():
    """
    Demonstrates functionality to add users_table and a specific user.
    """
    print("Connecting to database...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        print("Creating users_table if needed...")
        create_users_table(cursor)
        
        print("Adding user PETER PERTERSON...")
        try:
            # In a real app, use werkzeug.security.generate_password_hash
            # For this demo/script, we will simulate it or rely on app.py for proper flow
            # But let's be consistent if we run this manually:
            from werkzeug.security import generate_password_hash
            hashed_pw = generate_password_hash("test_password")
            add_user(cursor, "PETER PERTERSON", "peter@test.com", hashed_pw)
            conn.commit()
            print("User added successfully.")
        except mysql.connector.Error as err:
            if err.errno == 1062: # Duplicate entry
                print("User already exists.")
            else:
                print(f"Error adding user: {err}")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main entry point of the application.
    """
    print("Starting application...")
    # Showcase Cloud SQL User Integration
    # Ensure environment variables are set before running this in a real environment
    if os.getenv('DB_HOST'):
        example_users_usage()
    else:
        print("Skipping DB operations: DB_HOST not set.")

if __name__ == "__main__":
    main()
