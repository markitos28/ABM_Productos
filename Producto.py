class Producto():
    _marca=''
    _modelo=''
    _peso=0
    _cantidad=0
    def __init__(self, marca, modelo, peso, cantidad):
        self._marca= marca
        self._modelo= modelo
        self._peso= peso
        self._cantidad = cantidad
    # Metodos GET
    @property
    def Marca(self):
        return self._marca
    @property
    def Modelo(self):
        return self._modelo
    @property
    def Peso(self):
        return self._peso
    @property
    def Cantidad(self):
        return self._cantidad

    #Metodos SET
    ''' Marca y Modelo no deben ser modificados'''
    @Peso.setter
    def Peso(self, peso):
        self._peso= peso

    @Cantidad.setter
    def Cantidad(self, cantidad):
        self._cantidad= cantidad

    