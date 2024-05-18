from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import os
import json

app = Flask(__name__)
app.secret_key = 's4nh4s3cr3T@'

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('books'))
    return render_template('login.html')

@app.route('/validar', methods=['POST'])
def validar():
    username = request.form.get('username')
    password = request.form.get('password')

    salt = "secday"
    password_hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

    conn = sqlite3.connect('auth.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=\""+username+"\" AND password=\""+password_hashed+"\"")
    #c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password_hashed,))
    result = c.fetchone()

    conn.close()

    if result is None:
        error_message = "Usuário ou senha incorretos."
        return render_template('login.html', error_message=error_message)
    else:
        session['username'] = username
        return redirect(url_for('books'))

@app.route('/books')
def books():
    if 'username' in session:
        with open('books.json', 'r') as f:
            books = json.load(f)
        return render_template('index.html', books=books)
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=False)

