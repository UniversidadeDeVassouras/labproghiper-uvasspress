from application import app
from flask import render_template, request
import os


@app.route("/feed")
def feed():
    return render_template("feed.html")

