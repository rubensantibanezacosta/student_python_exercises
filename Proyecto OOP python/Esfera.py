from Circulo import Circulo
import math

class Esfera(Circulo):

    volumen=0

    def __init__(self, radio):
        super().__init__(radio)

        self.volumen = self.area * self.radio

    def printvolumen(self):
        print("volumen=", self.volumen)

    def tostring(self):
        print(self.__class__.__name__, ", radio=", self.getradio())
        self.printvolumen()


