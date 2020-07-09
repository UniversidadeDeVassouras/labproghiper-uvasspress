from application import app
from flask import render_template, request
from application.model.dao.usuarioDAO import UsuarioDAO
import os


@app.route ('/login/cadastro', methods = ['POST'])
def cadastro ():
    email = request.form['signup-email']
    senha = request.form['signup-password']
    confirmar_senha = request.form['signup-password-confirm']
    cadastrar_usuario = UsuarioDAO.cadastrar_usuario(email, senha, confirmar_senha)
    return render_template('login.html', cadastrar_usuario = cadastrar_usuario)

@app.route('/login')
def login_user():
    return render_template('login.html')