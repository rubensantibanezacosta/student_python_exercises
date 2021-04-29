from Rectangulo import Rectangulo


class Cubo(Rectangulo):
    volumen = 0

    def __init__(self, altura, anchura, profundidad):
        super().__init__(altura, anchura)
        self.profundidad = profundidad
        self.volumen = self.area * profundidad

    def setprofundidad(self, profundidad):
        self.profundidad = profundidad

    def getprofundidad(self):
        return self.profundidad

    def printvolumen(self):
        print("volumen=", self.profundidad,)

    def tostring(self):
        print(self.__class__.__name__, ", anchura=", self.getanchura(), ", altura=", self.getaltura(), "profundidad")
        self.printvolumen()

    def dibujar(self):
        for i in range(self.altura+self.profundidad):
            for j in range(self.anchura+self.profundidad):
                if j == 0 or i == 0 or i == self.altura or j == self.anchura or j==self.profundidad or i==self.profundidad or j==self.anchura+self.profundidad or i==self.altura+self.profundidad:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")

