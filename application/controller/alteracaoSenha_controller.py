from application import app
from flask import render_template, request
import os

@app.route('/alteracaosenha')
def alteracaoSenha():
   return render_template('alteracaoSenha.html')