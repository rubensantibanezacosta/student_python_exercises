import math




class Circulo():
    area = 0

    def __init__(self, radio):
        self.radio = radio
        self.area = math.pi * self.radio * self.radio

    def setradio(self, radio):
        self.radio = radio

    def getradio(self):
        return self.radio

    def getarea(self):
        return self.area

    def printarea(self):
        print("area= ", self.area)

    def tostring(self):
        print(self.__class__.__name__, ", radio=", self.getradio())
        self.printarea()

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
