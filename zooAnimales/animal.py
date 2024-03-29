import zooAnimales

class Animal:
    _totalAnimales = 0
    _zona = None  

    def __init__(self, nombre, edad, habitat, genero, zona=None):  
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona  
        Animal._totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos : {zooAnimales.mamifero.Mamifero.cantidadMamiferos()}\nAves : {zooAnimales.ave.Ave.cantidadAves()}\nReptiles : {zooAnimales.reptil.Reptil.cantidadReptiles()}\nPeces : {zooAnimales.pez.Pez.cantidadPeces()}\nAnfibios : {zooAnimales.anfibio.Anfibio.cantidadAnfibios()}"

    def toString(self):
        mensaje = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        if self._zona is not None:
            mensaje += f", la zona en la que me ubico es {self._zona.getNombre()}, en el zoo {self._zona.getZoo().getNombre()}"
        return mensaje


    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    @classmethod
    def getZona(cls):
        return cls._zona
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat): 
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
