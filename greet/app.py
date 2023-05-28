from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welocome():
    return 'welcome'

@app.route('/welcome/home')
def welocome_home():
    return 'welcome home'

@app.route('/welcome/back')
def welocome_back():
    return 'welcome back'