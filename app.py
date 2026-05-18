from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os
from datetime import datetime
from difflib import SequenceMatcher

app = Flask(__name__)
app.secret_key = "codealpha"

# Create Database Table
def init_db():

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            registered_at TEXT
        )
    ''')

    conn.commit()
    conn.close()

def is_similar(email1, email2):

    username1 = email1.split('@')[0]
    username2 = email2.split('@')[0]

    similarity = SequenceMatcher(
        None, username1, username2
    ).ratio()

    return similarity >= 0.75

@app.route('/',)
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM users')
    
    all_users = cursor.fetchall()

    conn.close()

    return render_template('users.html', users = all_users)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users where id = ?', (id,))
    conn.commit()
    conn.close()
    flash("User Deleted successfully", "success")
    return redirect('/users')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    name = request.form['username']
    email = request.form['email']

    # Connect Database
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    # Check Duplicate Email
    cursor.execute(
        'SELECT * FROM users where email = ?',
        (email,)
    )

    existing_user = cursor.fetchone()

    #If email already exists
    if existing_user:
        conn.close()

        flash('Duplicate user found!!', 'error')

        return redirect("/")
    
    cursor.execute("SELECT email from users")
    all_emails = cursor.fetchall()

    #False Positive Detection
    for existing_email in all_emails:
        db_email = existing_email[0]

        if is_similar(email, db_email):
            conn.close()

            flash(f"False Positive Detected!! Similar email exists: {db_email}", "error")

            return redirect('/')

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Insert Data
    cursor.execute(
        "INSERT INTO users (name, email, registered_at) VALUES (?, ?, ?)",
        (name, email, current_time)
    )

    conn.commit()
    conn.close()

    flash("User Registered Successfully!!", "success")

    return redirect('/')

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)