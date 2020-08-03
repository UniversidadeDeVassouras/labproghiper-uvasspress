class Autor:
    def __init__(self, id, nome_completo, login, senha, email):
        self._id = id
        self._nome_completo = nome_completo
        self._login = login
        self._senha = senha
        self._email = email
        self._status = "ativo"
        
    def get_email(self):
        return self._email
    
    def set_senha(self, senha):
        self._senha = senha
    
    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
