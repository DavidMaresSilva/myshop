from flask import render_template, session, request, redirect, url_for

from shop import app, db

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')