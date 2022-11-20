from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/webhook')
def webhook():
    return 'webhook App with Python Flask!'

app.run()
