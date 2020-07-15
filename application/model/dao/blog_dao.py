from application.model.entity.blog import Blog

class BlogDAO():
    def __init__(self):
        pass

    def criar_blog(self, nome, autor):
        return Blog(nome, autor)

    def adicionar_post(self, blog, post):
        blog.get_lista_posts().append(post) 
        return

    def alterar_status_post(self, post):  #InativarPost
        if post.get_status() == True:
            post.set_status(False) #Inativo
        else:
            post.set_status(True)  #Ativo
            
    def apagar_post(self, blog, post):
        post.get_id() -= ponteiro #Pega a posição do post na lista
        blog.get_lista_posts().pop(ponteiro) #Apaga o post
        return