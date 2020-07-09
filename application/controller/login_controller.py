from application import app
from flask import render_template, request, current_app
import os


@app.route('/logado', methods = ['POST'])
def logado():
    usuario = current_app.config['usuario_dao']
    email = request.form['login-email']
    senha = request.form['login-password']
    logar_usuario = usuario.logar_usuario(email,senha)
    if  logar_usuario == True:
        return render_template("logado.html")
    else: 
        return render_template('login.html')

@app.route ('/login/cadastro', methods = ['POST'])
def cadastro ():
    usuario = current_app.config['usuario_dao']
    email = request.form['signup-email']
    senha = request.form['signup-password']
    confirmar_senha = request.form['signup-password-confirm']
    cadastrar_usuario = usuario.cadastrar_usuario(email, senha, confirmar_senha)
    return render_template('login.html', cadastrar_usuario = cadastrar_usuario)

@app.route('/login')
def login_user():
    return render_template('login.html')
