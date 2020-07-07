class Comentario:
    def __init__(self, id, conteudo, data_hora_criacao, nome_comentarista, status):
        self._id = id
        self._conteudo = conteudo
        self._data_hora_criacao = data_hora_criacao
        self._nome_comentarista = nome_comentarista
        self._status = status