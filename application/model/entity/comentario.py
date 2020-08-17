class Comentario:
    def __init__(self, conteudo, data_hora_criacao, nome_comentarista, status = False):
        self._conteudo = conteudo
        self._data_hora_criacao = data_hora_criacao
        self._nome_comentarista = nome_comentarista
        self._status = status

    def get_conteudo(self):
        return self._conteudo

    def set_id(self, id):
        self._id = id

    def get_data_hora_criacao(self):
        return self._data_hora_criacao

    def get_nome_comentarista(self):
        return self._nome_comentarista

    def get_status(self):
        return self._status
    
    def switch_status(self):
        self._status != self._status