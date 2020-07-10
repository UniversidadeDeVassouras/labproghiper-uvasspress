class Blog:
    def __init__(self, id, titulo, autor, categoria):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._lista_posts = []
        self._lista_seguidores = []

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_titulo(self):
        return self._titulo
        
    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor
    
    def get_categoria(self):
        return self._categoria
    
    def set_categoria(self, categoria):
        self._categoria = categoria    
        
    def get_lista_posts(self):
        return self._listaPosts

    def set_lista_posts(self, listaPosts):
        self._listaPosts = listaPosts

    def get_lista_seguidores(self):
        return self._listaSeguidores

    def set_lista_seguidores(self, listaSeguidores):
        self._listaSeguidores = listaSeguidores