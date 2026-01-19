# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.

from flask import Flask, render_template, request, redirect, url_for, flash
import database_operations

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    connection = database_operations.get_db_connection()
    if connection:
        database_operations.create_table_if_not_exists(connection)
        database_operations.add_user(connection, name, email, password)
        connection.close()
        flash(f"User '{name}' added successfully!", 'success')
    else:
        flash("Database connection failed.", 'error')
    
    return redirect(url_for('index'))

@app.route('/search_user', methods=['POST'])
def search_user():
    name = request.form['name']
    search_results = []
    
    connection = database_operations.get_db_connection()
    if connection:
        search_results = database_operations.get_user_by_name(connection, name)
        connection.close()
        if not search_results:
            flash(f"No user found with name '{name}'.", 'error')
    else:
        flash("Database connection failed.", 'error')
    
    return render_template('index.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
