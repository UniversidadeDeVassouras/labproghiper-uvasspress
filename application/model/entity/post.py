class Post:
    def __init__(self, id, titulo, conteudo, descricao, imagem_destaque, data_hora_criacao, data_hora_edicao, status, autor, id_autor):
        self._id = id
        self._titulo = titulo
        self._conteudo = conteudo
        self._descricao = descricao
        self._imagem_destaque = imagem_destaque
        self._data_hora_criacao = data_hora_criacao
        self._data_hora_edicao = data_hora_edicao
        self._status = status
        self._qtd_curtida = 0
        self._autor = autor
        self._id_autor = id_autor
        self._comentarios_pendentes = []
        self._comentarios_autorizados = []

    def get_qtd_curtidas(self):
        return self._qtd_curtida

    def set_qtd_curtidas(self, curtida):
        self._qtd_curtida = curtida

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_titulo(self):
        return self._titulo

    def set_conteudo(self,conteudo):
        self._conteudo = conteudo

    def get_conteudo(self):
        return self._conteudo

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_descricao(self):
        return self._descricao

    def set_imagem_d(self, imagem_destaque):
        self._imagem_destaque= imagem_destaque

    def get_imagem_d(self):
        return self._imagem_destaque

    def set_data_hora_criacao(self,dh):
        self._data_hora_criacao = dh

    def get_data_hora_criacao(self):
        return self._data_hora_criacao

    def get_autor(self):
        return self._autor

    def get_id_autor(self):
        return self._id_autor

    def get_comentarios_pendentes(self):
        return self._comentarios_pendentes

    def get_comentarios_autorizados(self):
        return self._comentarios_autorizados

    def add_comentarios_pendentes(self, comentario):
        self._comentarios_pendentes.append(comentario)

    def add_comentarios_autorizados(self, comentario):
        self._comentarios_autorizados.append(comentario)