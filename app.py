from flask import Flask, render_template

app = Flask(__name__)

@app.route('/developer/<name>')
def demo(name):
    return render_template('developer.html',name=name)
