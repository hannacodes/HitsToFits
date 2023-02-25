from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import sys
import os
 
# setting path
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)
sys.path.append('../backend')

from backend import hits

app = Flask(__name__)

nav = "<a href='/'>home</a> <a href='/about/'>about</a>"

song_url = ""
ALLOWED_EXTENSIONS=[".png", ".jpg"]
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
        song_url = form_data["song"]
        features = hits.getAllData(song_url)
        mode = hits.getMode(features)
        return redirect("/closet")
        
@app.route('/closet')
def closet(): 
    return render_template("closet.html")
'''
def allowedFile(filename): 
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
'''

@app.route('/upload', methods=["GET", "POST"])
def upload(): 
    if request.method == 'POST': 
        if request.form.get("existing") == "ViewExisting":
            return redirect("/existing")
        else: 
            print(request.files)
            photolst = request.files.getlist("file")
            for file in photolst: 
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "you uploaded: " + str(photolst)
    if request.method == 'GET': 
        return f"the url is invalid"

@app.route("/precloset")
def precloset():
    return render_template("precloset.html")