from application import app
from flask import render_template, request, current_app, jsonify
import os

from application.model.dao.blog_dao import BlogDAO
from application.model.entity.blog import Blog

@app.route("/criar_blog", methods=['POST'])
def criacao():
    """blog_dao  = BlogDAO()
    nome = request.values.get('nome')
    autor = request.values.get('autor')
    categoria = request.values.get('categoria')
    blog = blog_dao.criar_blog(autor, titulo)"""
    return