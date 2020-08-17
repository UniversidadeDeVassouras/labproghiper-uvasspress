class Resposta:
    def __init__(self, conteudo_resposta, data_resposta, nome_autor):
        self._conteudo_resposta = conteudo_resposta
        self._data_resposta = data_resposta
        self._nome_autor = nome_autor

    def get_conteudo_resposta(self):
        return self._get_conteudo_resposta

    def get_data_resposta(self):
        return self._data_resposta

    def get_nome_autor(self):
        return self._get_nome_autor

    def set_conteudo_resposta(self, conteudo_resposta):
        self._get_conteudo_resposta = conteudo_resposta

    def set_data_resposta(self, data_resposta):
        self._data_resposta = data_resposta

    def set_nome_autor(self, nome_autor):
        self._get_nome_autor = nome_autor