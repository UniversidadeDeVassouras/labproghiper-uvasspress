from application import app
from flask import render_template, request
import os

@app.route('/')
def index():
   return render_template('index.html')
