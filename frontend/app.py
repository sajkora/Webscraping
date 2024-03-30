from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

app.debug = True

#cd frontend
#virtualenv flask
#cd flask
#flask\Scripts\activate.bat
#cd frontend
#pip install flask
#xampp 
#python -m flask run
#port 5000