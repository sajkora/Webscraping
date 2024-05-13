import sys
from flask import Flask, render_template, url_for, jsonify, redirect, request
sys.path.append('./')
from backend.Scraping.main import get_random_crypto, scrape_data, download_csv_to_folder

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET'])
def generate():
    row = get_random_crypto()
    return render_template('index.html', row=row)

@app.route('/save-data', methods=['POST'])
def save_data():
    directory = request.form.get('directory')
    download_csv_to_folder(directory)
    return redirect('/')

if __name__ == '__main__':
    scrape_data()
    app.run()
    
