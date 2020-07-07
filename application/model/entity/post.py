class Post:
    def __init__(self, id, titulo, conteudo, descricao, imagem_destaque, data_hora_criacao, data_hora_edicao, status):
        self._id = id
        self._titulo = titulo
        self._conteudo = conteudo
        self._descricao = descricao
        self._imagem_destaque = imagem_destaque
        self._data_hora_criacao = data_hora_criacao
        self._data_hora_edicao = data_hora_edicao
        self._status = status
