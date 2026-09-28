## Oh no! What did I tell my coworker on that call again??? shitisaid.com. (or stuffisaid.com for marketability)

### =================== OVERVIEW ===================
### Shitisaid.com is a free-to-use transcripts amalgamator.
### It accepts a wide range of artifacts, converts them to transcripts, and allows
### the user to store, browse, and access them easily and conveniently online.
### The website accepts a variety of text, audio, and video formats, as well as URLs for maximum convenience!




from flask import Flask, render_template, send_from_directory, request
import sys
import os
from pathlib import Path


### ==== DEFINITION ====
class GlobalConfig():
    def __init__(self):
        self.MEDIA_FOLDER = Path(os.getcwd(), "media")
        self.SCHEMA_FOLDER = Path(os.getcwd(), "schema")
        self.DB_FOLDER = Path(os.getcwd(), "db")


### ==== INITIALISATION ====
config = GlobalConfig()
app = Flask(__name__)

app.config["MEDIA_FOLDER"] = config.MEDIA_FOLDER



### ROUTING
@app.route("/", methods=["GET"])
def home():
    return render_template("main.html")


@app.route("/media/<filename>", methods=["GET"])
def media(filename):
    return send_from_directory(
        app.config['MEDIA_FOLDER'],
        filename,
        as_attachment=False,
    )

@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST" and request.form:
        if "email" in request.form:
            if isEmailRegistered(): login()
            else: register()



        print(request.cookies)
        if "email" in request.cookies:
            print(request.cookies.get("email"))



    return render_template("signin.html")


def isEmailRegistered():
    pass

def login():
    pass

def register():
    pass




### =================== REFERENCES ===================
## https://flask.palletsprojects.com/en/stable/quickstart/
## https://stackoverflow.com/questions/69762201/what-is-the-correct-way-to-serve-access-media-files-in-flask


### =================== AI USE DISCLAIMER ===================
## AI was used to generate graphical assets for the website due to it being unfeasible otherwise.
## Assets include: [ logo.svg, 
## 


### =================== GDPR DISCLAIMER ===================
### This service acts as a data processor and data controller. 
### Relevant GDPR-mandated measures will be taken to ensure compliance on release.


### =================== AUTHOR ===================
# Gracjan Blazejowski, 2026.