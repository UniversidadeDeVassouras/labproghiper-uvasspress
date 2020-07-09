class Autor:
    def __init__(self, id, nome_completo, login, senha, email):
        self._id = id
        self._nome_completo = nome_completo
        self._login = login
        self._senha = senha
        self._email = email


    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id

    def get_nomeCompleto (self):
        return self._nome_completo
    
    def get_login (self):
        return self._login

    def get_password (self):
        return self._senha

    def get_email (self):
        return self._email