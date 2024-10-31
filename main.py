from clases.caja import caja
from clases.camion import camion
from clases.naranja import naranja

def main():
    
    #metodo para tomar el total de naranjas y dividirlas en las lista de jugo y expo:
    def generarNaranjas(total):
        for i in range(total):
            pNaranja = naranja()
            if pNaranja.getPeso() > 150 and pNaranja.getPeso() < 350:
                lstNaranjasExpo.append(pNaranja)
            else:
                lstNaranjasJugo.append(pNaranja)
    
    #metodo para empaquetar 100 naranjas por caja
    def empaquetarNaranjas(listaNaranjas, listaCaja):
        pCaja = caja()
        for pNaranaja in listaNaranjas:
            if pCaja.getCapacidad() < 100:
                pCaja.cargarCaja(pNaranaja)
            else:
                listaCaja.append(pCaja)
                pCaja = caja()
                pCaja.cargarCaja(pNaranaja)

    #metodo para cargar cajas en el camion
    def cargarCajas(listaCajas, listaCamion):
        pCamion = camion()
        for pCaja in listaCajas:
            if pCamion.getPesoCarga() + int(pCaja.getPesoTotal()) < pCamion.getCapacidadTotal():
                pCamion.cargarCamion(pCaja)
            else:
                listaCamion.append(pCamion)
                pCamion = camion()
                pCamion.cargarCamion(pCaja)

        #si el camion no llega a los 500k lo carga igual en el array de camiones
        if pCamion.getPesoCarga() > 0:
            listaCamion.append(pCamion)

    #metodo para imprimir los camiones y los pesos
    def imprimirCamiones(listaCamion):
        i=1
        for pCamion in listaCamion:
            if pCamion.getPesoCarga() > 400: #si el camion tiene carga mayor al 80%
                print(f"\nCamion {i} (carga total: {round(pCamion.getPesoCarga(),2)} kg)")
                j = 1
                for pCaja in pCamion.getLstCaja():
                    print(f"caja {j}: {round(pCaja.getPesoTotal(),2)} kg", end =",")
                    j+=1
                print()
            else:
                print(f"\nEl camion {i} contiene {round(pCamion.getPesoCarga(),2)} kg, faltando {round(pCamion.getCapacidadTotal()-pCamion.getPesoCarga(),2)} kg para completar la carga")
                print()
            i=i+1

    lstNaranjasExpo = []
    lstNaranjasJugo = []
    lstCajas = []
    lstCamion = []

    crearNaranjas = int(input("ingrese una cantidad de naranjas >"))
    generarNaranjas(crearNaranjas)
    empaquetarNaranjas(lstNaranjasExpo,lstCajas)
    cargarCajas(lstCajas, lstCamion)
    imprimirCamiones(lstCamion)


if __name__ == "__main__":
    main()