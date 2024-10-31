class camion:

    def __init__(self):
        self.CapacidadTotal = 500
        self.lstCaja = []
        self.pesoCarga = 0

    def cargarCamion(self, caja):
        self.lstCaja.append(caja)
        self.pesoCarga += caja.getPesoTotal()
        
    def getCapacidadTotal(self):
        return self.CapacidadTotal
    def getLstCaja(self):
        return self.lstCaja
    def getPesoCarga(self):
        return self.pesoCarga