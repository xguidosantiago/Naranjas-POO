class caja:

    def __init__(self):
        self.Capacidad = 0
        self.pesoTotal = 0
        self.lstNaranjas = []

    def cargarCaja(self,naranja):
        self.lstNaranjas.append(naranja)
        self.pesoTotal += naranja.getPeso()/1000
        self.Capacidad +=1

    def getCapacidad(self):
        return self.Capacidad
    def getPesoTotal(self):
        return self.pesoTotal
    def getLstNaranjas(self):
        return self.lstNaranjas