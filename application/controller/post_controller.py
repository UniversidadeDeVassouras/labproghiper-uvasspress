from flask import render_template, request
from application import app
import os
from application.model.entity.post import Post
from application.model.dao.post_DAO import PostDAO
from application.model.entity.administrador import Administrador
from application.model.dao.administradorDAO import administradorDAO
from application.model.entity.comentario import Comentario



@app.route("/posts/<autor_id>/<post_id>")
def exibir_posts():
    exibicao = administradorDAO().procurar_id_autor(autor_id)
    administrador_dao = administradorDAO()
    exibir_posts = post_DAO().retornar_todas_postagens()
    return render_template('post.html', exibicao = exibicao, exibir_posts = exibir_posts)


@app.route("/<post_id>/curtir", methods=['POST'])
def curtir():
    post_dao = post_DAO()
    post = administradorDAO().identificar_postagens_autor(int(post_id))
    post_dao.adicionar_curtida(post)
    return render_template('curtida.html', post = post)