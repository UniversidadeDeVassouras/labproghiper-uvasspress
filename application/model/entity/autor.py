class Autor:
    def __init__(self, nome, nome_usuario, email, senha):
        self._nome = nome
        self._nome_usuario = nome_usuario
        self._email = email
        self._senha = senha
        

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_nome_usuario(self):
        return self._nome_usuario

    def get_email (self):
        return self._email

    def get_password (self):
        return self._senha
