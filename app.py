# Audo added TEXT-123
import os
import mysql.connector
from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from users_db import get_db_connection, add_user, get_user_by_name, create_users_table

app = Flask(__name__)
# Secret key is needed for flash messages
app.secret_key = os.getenv('SECRET_KEY', 'super_secret_key_for_demo')
csrf = CSRFProtect(app)

def init_db():
    """Initializes the database table if it doesn't exist."""
    print("Initializing database...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        create_users_table(cursor)
        conn.close()
        print("Database initialized.")
    except Exception as e:
        print(f"Warning: Database initialization failed: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    search_result = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            if action == 'add':
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('password')
                
                try:
                    hashed_password = generate_password_hash(password)
                    add_user(cursor, username, email, hashed_password)
                    conn.commit()
                    flash(f'User {username} added successfully!', 'success')
                except mysql.connector.Error as err:
                    if err.errno == 1062:
                        flash(f'Error: User with email {email} already exists.', 'error')
                    else:
                        app.logger.error(f"Database error: {err}")
                        flash('An error occurred during registration.', 'error')
                        
            elif action == 'search':
                search_name = request.form.get('search_username')
                user = get_user_by_name(cursor, search_name)
                if user:
                    search_result = {'name': user[0], 'email': user[1]}
                else:
                    flash(f'User {search_name} not found.', 'info')
            
            cursor.close()
            conn.close()
            
        except Exception as e:
            flash(f"Connection error: {e}", 'error')

    return render_template('index.html', search_result=search_result)

if __name__ == '__main__':
    # Initialize DB on start (optional, but good for demo)
    if os.getenv('DB_HOST'):
        init_db()
    
    # Security check for Secret Key
    if app.secret_key == 'super_secret_key_for_demo':
        print("WARNING: You are using the default secret key. This is insecure for production.")
        print("Set the SECRET_KEY environment variable.")
    
    # Use environment variable for debug mode, default to False for safety
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=8080, debug=debug_mode)
