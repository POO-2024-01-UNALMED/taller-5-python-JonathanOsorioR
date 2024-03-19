from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        
    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = cls(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):  
        self._colorPiel = colorPiel

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getRanas(cls):
        return cls.ranas
    
    @classmethod
    def setRanas(cls, ranas):
        cls.ranas = ranas
    
    @classmethod
    def getSalamandras(cls):
        return cls.salamandras
    
    @classmethod
    def setSalamandras(cls, salamandras):
        cls.salamandras = salamandras
        
