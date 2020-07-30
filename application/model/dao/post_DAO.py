from application.model.entity.post import Post

class PostDAO:
    def __init__(self):
        pass
    
    def retornar_todas_postagens(self):
        return self.todas_as_postagens

    def adicionar_curtida(self, post):
        curtida = post.get_qtd_curtidas()
        curtida += 1
        post.set_qtd_curtidas(curtida)

