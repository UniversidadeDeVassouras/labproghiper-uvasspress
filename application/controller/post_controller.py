from flask import render_template, request
from application import app
import os
from application.model.entity.post import Post
from application.model.dao.post_DAO import PostDAO
from application.model.entity.administrador import Administrador
from application.model.dao.administradorDAO import administradorDAO
from application.model.entity.comentario import Comentario
from datetime import datetime
from flask_mail import Mail, Message

app.config['MAIL_SERVER']='exemplo.gmail.com' #email que vai enviar
app.config['MAIL_PORT'] = 465 #porta do email se for gmail o padrão é 465, ainda mais por não estarmos utilizando TSL
app.config['MAIL_USERNAME'] = 'Id_do@gmail.com' #Nome da conta de Email 
app.config['MAIL_PASSWORD'] = '*****' #Senha
app.config['MAIL_USE_TLS'] = False #Basicamente é um protocolo de segurança
app.config['MAIL_USE_SSL'] = True #Outro protocolo de segurança

mail = Mail(app)


@app.route("/posts/<autor_id>/<post_id>")
def exibir_posts():
    exibicao = administradorDAO().procurar_id_autor(autor_id)
    administrador_dao = administradorDAO()
    exibir_posts = postDAO().retornar_todas_postagens()
    return render_template('post.html', exibicao = exibicao, exibir_posts = exibir_posts)


@app.route("/<post_id>/curtir", methods=['POST'])
def curtir():
    post_dao = postDAO()
    post = administradorDAO().identificar_postagens_autor(int(post_id))
    post_dao.adicionar_curtida(post)
    return render_template('curtida.html', post = post)

@app.route("/<post_id>/comentario", methods=['POST'])
def comentar():
    post_dao = postDAO()
    post = post_dao.retornar_todas_postagens(int(post_id))
    conteudo = request.values.get('conteudo')
    nome_comentarista = request.values.get('nome')
    data_comentario = datetime.today()
    comentario = Comentario(conteudo, data_comentario, nome_comentarista)
    comentario.set_id(1 + len(post.get_comentarios_pendentes()))
    post.add_comentario_pendente(comentario)
    lista_pendentes = post.get_comentario_pendentes()
    return render_template('comentario.html', post = post, lista_pendentes = lista_pendentes)


    
@app.route("/<post_id>/responder", methods=['POST'])
def responder():
    msg = Message('Olá', sender = 'sua_id@gmail.com', recipients = ['email_da_pessoa@gmail.com'])
    msg.body = "Seu comentário foi respondido pelo autor..."
    mail.send(msg)
    return "E-mail Enviado!"