from flask import Flask, render_template, url_for
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
import logging

logging.basicConfig(stream=sys.stderr)

import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    print("Calling generate function...")
    random_crypto = main.get_random_crypto()
    return render_template('index.html', random_crypto=random_crypto)

if __name__ == '__main__':
    app.run()


#cd frontend
#virtualenv flask
#cd flask
#flask\Scripts\activate.bat
#cd frontend
#pip install flask
#python -m flask run --debug
#port 5000