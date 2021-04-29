from Circulo import Circulo
import math

class Cilindro(Circulo):

    volumen = 0

    def __init__(self, radio, profundidad):
        super().__init__(radio)
        self.profundidad = profundidad

        self.volumen = self.area * profundidad

    def setradio(self, radio):
        self.radio = radio

    def setprofundidad(self, profundidad):
        self.profundidad=profundidad

    def getradio(self):
        return self.radio

    def getprofundidad(self):
        return  self.profundidad



    def printvolumen(self):
        print("volumen=", self.volumen)


    def tostring(self):
        print(self.__class__.__name__, ", radio=", self.getradio())
        self.printvolumen()

    def dibujar(self):
        for i in range(self.radio*2):
            for j in range(i):
                print("*", end="")
            print("")

        discount = self.radio*2
        for i in range(self.radio*2):
            for j in range(discount):
                print("*", end="")
            print("")
            discount = discount - 1

            for j in range(self.radio*2):
                for z in range(self.anchura):
                    print("*", end="")
                print("")

