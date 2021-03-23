# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/form')
def form():
    if request.args.get('name', '') == '':
        return render_template('simple_form.html')

