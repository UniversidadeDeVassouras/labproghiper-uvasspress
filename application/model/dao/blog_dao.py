from application import todas_postagens
from application.model.entity.blog import Blog

class BlogDAO():
    def __init__(self):
        pass

    def criar_blog(self, nome):
        self._blog = Blog(nome)
        return "Blog criado com sucesso!"

    def adicionar_post(self, blog, post):
        blog.get_lista_posts().append(post) 
        return

    def alterar_status_post(self, post):  #InativarPost
        if post.get_status() == True:
            post.set_status(False) #Inativo
        else:
            post.set_status(True)  #Ativo
            
    """def apagar_post(self, blog, post):
        post.get_id() -= ponteiro #Pega a posição do post na lista
        blog.get_lista_posts().pop(ponteiro) #Apaga o post
        return
"""
    def procurar_postagem(self, id):
        for i in range(0, len(self._todas_postagens)):
            if self._todas_postagens[i].get_id() == int(id):
                return self._todas_postagens[i]
        return None