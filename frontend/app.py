import sys
from flask import Flask, render_template, session, url_for, jsonify, redirect, request, flash
import csv
import secrets
sys.path.append('./')
from backend.Scraping.main import get_random_crypto, scrape_data, download_csv_to_folder, read_users, write_user

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/home')
def home():
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    if not session.get('username'):
        return redirect(url_for('login'))
    row = get_random_crypto()
    return render_template('index.html', row=row)

@app.route('/save-data', methods=['POST'])
def save_data():
    directory = request.form.get('directory')
    download_csv_to_folder(directory)
    return redirect('/home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = {"username": username, "password": password}
        write_user(user)
        return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        if (username, password) in [(u['username'], u['password']) for u in users]:
            session['username'] = username
            flash('Login successful!', category='success')
            return redirect('/home')
        else:
            flash('Invalid username or password. Please try again.', category='error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout successful!', category='success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    scrape_data()
    app.run()
    
