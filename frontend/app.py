from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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