

class Rectangulo():
    area = 0

    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        self.area = altura * anchura

    def setaltura(self, altura):
        self.altura = altura

    def setanchura(self, anchura):
        self.anchura = anchura

    def getaltura(self):
        return self.altura

    def getanchura(self):
        return self.anchura

    def getarea(self):
        return self.area

    def printarea(self):
        print("area=", self.area)

    def tostring(self):
        print(self.__class__.__name__, ", anchura=", self.getanchura(), ", altura=", self.getaltura())
        self.printarea()

    def dibujar(self):
        for i in range(self.altura):
            for j in range(self.anchura):
                print("*", end="")
            print("")


