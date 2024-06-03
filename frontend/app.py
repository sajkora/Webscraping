import sys
from flask import Flask, render_template, session, url_for, jsonify, redirect, request, flash
import csv
import secrets
sys.path.append('./')
from backend.Scraping.main import get_random_crypto, scrape_data, download_csv_to_folder, read_users, write_user
import os
import pandas as pd

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 


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

@app.route('/all-crypto')
def all_crypto():
    if not session.get('username'):
        return redirect(url_for('login'))

    csv_file_path = 'Crypto Data.csv'
    if not os.path.exists(csv_file_path):
        flash("No data available. Please run the scraper first.", category='error')
        return redirect(url_for('home'))
    
    df = pd.read_csv(csv_file_path)
    all_cryptos = df.to_dict(orient='records')
    return render_template('all_crypto.html', all_cryptos=all_cryptos)

@app.route('/add-to-favorites', methods=['POST'])
def add_to_favorites():
    if not session.get('username'):
        return jsonify({'success': False, 'message': 'Not logged in'})

    crypto_name = request.json.get('name')
    favorites_file = f'{session.get("username")}_favorites.csv'

    if not os.path.exists(favorites_file):
        with open(favorites_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name'])

    with open(favorites_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([crypto_name])

    return jsonify({'success': True})

@app.route('/profile')
def profile():
    if not session.get('username'):
        return redirect(url_for('login'))

    favorites_file = f'{session.get("username")}_favorites.csv'
    favorites = []

    if os.path.exists(favorites_file):
        df = pd.read_csv(favorites_file)
        favorites = df['Name'].tolist()

    return render_template('profile.html', favorites=favorites)

@app.route('/remove-from-favorites', methods=['POST'])
def remove_from_favorites():
    if not session.get('username'):
        return jsonify({'success': False, 'message': 'Not logged in'})

    crypto_name = request.json.get('name')
    favorites_file = f'{session.get("username")}_favorites.csv'

    if os.path.exists(favorites_file):
        df = pd.read_csv(favorites_file)
        df = df[df['Name'] != crypto_name]  
        df.to_csv(favorites_file, index=False)
        return jsonify({'success': True})

    return jsonify({'success': False, 'message': 'Favorites file does not exist'})


if __name__ == '__main__':
    scrape_data()
    app.run(debug=True)
    #!(usunac debug true)!