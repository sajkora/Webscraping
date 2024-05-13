import sys
from flask import Flask, render_template, url_for, jsonify
sys.path.append('./')
from backend.Scraping.main import get_random_crypto, scrape_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET'])
def generate():
    row = get_random_crypto()
    return render_template('index.html', row=row)


if __name__ == '__main__':
    scrape_data()
    app.run()
    
