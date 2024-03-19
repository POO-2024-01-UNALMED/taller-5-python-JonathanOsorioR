class Zona:

    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def cantidadAnimales(self):

        return len(self._animales)
    
    def agregarAnimales(self, animal):

        self._animales.append(animal)

    #getters y setters
    
    def getNombre(self):

        return self._nombre
    
    def setNombre(self, nombre):

        self._nombre = nombre

    def getZoo(self):

        return self._zoo
    
    def setZoo(self, _zoo):

        self._nombre = _zoo

