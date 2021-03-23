# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/read')
def read():
    msg = request.args.get('msg', '')
    if msg != '':
        f = open("file.txt", "w" + '<br>')
        f.write(msg)
        f.close()
    f = open("file.txt", "r")
    return f.read()

@app.route('/')
def msg():
    return render_template('msg.html')
