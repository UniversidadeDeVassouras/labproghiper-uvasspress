from application import app
from flask import render_template, request
import os

@app.route('/recuperacaosenha')
def recuperacaoSenha():
   return render_template('recuperacaoSenha.html')
