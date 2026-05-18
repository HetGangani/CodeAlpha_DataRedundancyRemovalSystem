from flask import Flask, render_template, request, redirect, flash
import sqlite3

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
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

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

    # Insert Data
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    flash("User Registered Successfully!!", "success")

    return redirect('/')

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)