from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_name():
    name = request.args.get('n', '')
    return 'Hello ' + name

@app.route('/form')
def form():
    if name == '':
        return render_template('simple_form.html')
    else:
        return 'Hello ' + name
