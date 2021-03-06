# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def msg():
    return render_template('index.html')

@app.route('/save')
def read():
    userName = request.args.get('userName', '')
    msg = request.args.get('msg', '')
    if msg != '':
        f = open("file.txt", "a")
        f.write('🌊' + userName + '🌊' + '<br>')
        f.write(msg + '<br>')
        f.close()
    f = open("file.txt", "r")
    return f.read()
