

class Autor:
    def __init__(self, id, nome_completo, email, senha):
        self._id = id
        self._nome_completo = nome_completo
        self._email = email
        self._senha = senha
        

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id

    def get_nomeCompleto (self):
        return self._nome_completo

    def get_email (self):
        return self._email

    def get_password (self):
        return self._senha
