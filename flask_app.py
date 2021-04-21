# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def msg():
    return render_template('index.html')

@app.route('/save')
def read():
    msg = request.args.get('msg', 'userName', '')
    if msg != '':
        f = open("file.txt", "a")
        f.write('\033[1m' + userName + '\033[0m' + '<br>' + msg + '<br>')
        f.close()
    f = open("file.txt", "r")
    return f.read()
