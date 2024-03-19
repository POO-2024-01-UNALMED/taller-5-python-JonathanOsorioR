class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []  
        
    def agregarZonas(self, zonaNueva):
        self._zonas.append(zonaNueva)

    def cantidadTotalAnimales(self):
        numero = 0
        for zona in self._zonas:
            numero += zona.cantidadAnimales()
        return numero
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZonas(self):
        return self._zonas
    
    def setZonas(self, zonas):
        self._zonas = zonas