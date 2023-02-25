from flask import Flask, render_template, request
import sys
import os
 
# setting path
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)
sys.path.append('../backend')

from backend import hits

app = Flask(__name__)

nav = "<a href='/'>home</a> <a href='/about/'>about</a>"

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/song', methods = ['POST', 'GET'])
def song():
    print(request.method )
    if request.method == 'GET': 
        return f"the url is invalid"
    if request.method == 'POST':
        form_data = request.form
        features = hits.getAllData(form_data["song"])
        mode = hits.getMode(features)
        return "<h1> Mode: "+str(mode)+"</h1>"
    
@app.route('/closet')
def closet(): 
    return render_template("closet.html")

@app.route('/upload', methods=["GET", "POST"])
def upload(): 
    if request.method == 'POST': 
        if request.form.get("existing") == "ViewExisting":
            return "existing"
        else: 
            print(request.form)
            photolst = request.form.getlist("photos")
            return "you uploaded: " + str(photolst)
    if request.method == 'GET': 
        return f"the url is invalid"