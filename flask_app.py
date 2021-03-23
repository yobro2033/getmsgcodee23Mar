# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def msg():
    msg = request.args.get('msg', '')
    f = open("file.txt", "w")
    f.write(msg)
    f.close()
    return render_template('msg.html')
return app.render_template(generate(), mimetype='text/plain')

@app.route('/read')
def red():
    f = open('file.txt', 'r')
    return f.read


        
