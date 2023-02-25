from flask import Flask

app = Flask(__name__)

nav = "<a href='/'>home</a> <a href='/about/'>about</a>"

@app.route('/')
def hello():
    return nav + '<h1>TEST TEST</h1>'


@app.route('/about/')
def about():
    return nav+'<h3>This is a Flask web application.</h3>'

@app.route('/test/')
def test():
    return nav+'<h3>another page!</h3>'