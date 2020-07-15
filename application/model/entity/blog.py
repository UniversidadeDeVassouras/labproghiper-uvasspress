class Blog:
    def __init__(self, id, nome, autor):
        self._nome = nome
        self._id = id
        self._autor = autor
        self._lista_posts = []
        self._lista_seguidores = []

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor
        
    def set_nome(self, nome):
        self._nome = nome  
        
    def get_lista_posts(self):
        return self._listaPosts

    def set_lista_posts(self, listaPosts):
        self._listaPosts = listaPosts

    def get_lista_seguidores(self):
        return self._listaSeguidores

    def set_lista_seguidores(self, listaSeguidores):
        self._listaSeguidores = listaSeguidores