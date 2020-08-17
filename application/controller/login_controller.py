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
        mensagem_erro = "Email ou senha incorretos"
        return render_template('login-1.html',mensagem_erro = mensagem_erro)

@app.route ('/login/cadastro', methods = ['POST'])
def cadastro ():
    usuario = current_app.config['usuario_dao']
    email = request.form['signup-email']
    senha = request.form['signup-password']
    confirmar_senha = request.form['signup-password-confirm']
    nome = request.form['signup-nome']
    nome_usuario = request.form['signup-user-name']
    usuario.cadastrar_usuario(nome, nome_usuario, email, senha, confirmar_senha, administrador = True)
    return render_template('criar_blog.html')

@app.route('/login/cadastro-blog', methods = ['POST'])
def cadastro_blog():
    usuario = current_app.config['usuario_dao']
    blog = current_app.config['blog_dao']
    nome = request.form['blog-name']
    cadastrar_blog = blog.criar_blog(nome)
    return render_template('dashboard.html')

@app.route('/login')
def login_user():
    usuario = current_app.config ['usuario_dao']
    check_user = usuario.exibir()

    if not check_user:
        return render_template('cadastro.html')
    else:
        return render_template('login-1.html', check_user = check_user)

@app.route('/logado/cadastro-autores', methods = ['POST'])
def cadastro_autores():
    usuario = current_app.config['usuario_dao'] 
    email = request.form['signup-email']
    senha = request.form['signup-password']
    confirmar_senha = request.form['signup-password-confirm']
    nome = request.form['signup-nome']
    nome_usuario = request.form['signup-user-name']
    usuario.cadastrar_usuario(nome, nome_usuario, email, senha, confirmar_senha, administrador = False)
    return render_template('dashboard.html')
