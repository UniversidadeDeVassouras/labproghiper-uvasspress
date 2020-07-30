from application.model.entity.post import Post
from application.model.entity.comentario import Comentario

class PostDAO:
    def __init__(self):
        pass
    
    def retornar_todas_postagens(self):
        return self.todas_as_postagens

    def adicionar_curtida(self, post):
        curtida = post.get_qtd_curtidas()
        curtida += 1
        post.set_qtd_curtidas(curtida)

    def get_comentario_pendente_by_id(self, id, post):
        pendentes_lista = list(filter(lambda categoria : get_comentario_pendente_by_id() == id, post.get_comentarios_pendentes()))
        if len(pendentes_lista) == 0:
            return None
        return pendentes_lista[0]
