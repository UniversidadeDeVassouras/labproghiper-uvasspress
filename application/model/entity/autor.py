class Autor:
    def __init__(self, id, nome_completo, login, senha, email):
        self._id = id
        self._nome_completo = nome_completo
        self._login = login
        self._senha = senha
        self._email = email

    def get_email(self):
        return self._email
