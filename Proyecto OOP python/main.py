
from Rectangulo import Rectangulo
from Circulo import Circulo
from Cubo import Cubo
from Cilindro import Cilindro
from Esfera import Esfera


lista=[]


def menuPrincipal():
   seleccion=input("Selecciona una de las opciones:\n"\
          "1. Crear un objeto:\n" \
          "2. Leer Listado\n" \
          "3. Eliminar objeto\n"\
          "4. Salir\n")
   return seleccion

def CrearObjeto():
    #submenu crear objeto

    objetoACrear=input("Selecciona el tipo de objeto que quieres crear: \n"
          " 1. Circulo\n 2.Rectangulo\n 3.Cilindro\n 4.Cubo\n 5.Esfera\n")
    return objetoACrear

def leerListado():
    for i in range (len(lista)):
        print(i)
        lista[i].tostring()
        lista[i].dibujar()

def borrarFigura():
    leerListado()
    num=input(int("Selecciona el numero de la figura que quieres eliminar\n"))
    list.pop(list[num])
    print("Figura numero",num, "borrada\n")


print("Bienvenido a la aplicacion FORMAS\n"
          "======================================")

on=0
while on==0:

    seleccion = menuPrincipal()
    if seleccion == '1':
        subseleccion = CrearObjeto()

        if subseleccion == '1':
            print("Has seleccionado Circulo")
            radio = int(input("Introduce el radio"))
            C = Circulo.Circulo(radio)
            lista.append(C)
            print("Circulo Creado\n")

        elif subseleccion == '2':
            print("Has seleccionado Rectangulo\n")
            altura = int(input("Introduce la altura"))
            anchura = int(input("Introduce la anchura"))
            R = Rectangulo(altura, anchura)
            lista.append(R)
            print("Rectangulo Creado\n")

        elif subseleccion == '3':
            print("Has seleccionado \n")
            radio = int(input("Introduce el radio\n"))
            altura = int(input("Introduce la altura\n"))
            Ci = Cilindro(radio, altura)
            lista.append(Ci)
            print("Cilindro Creado\n")

        elif subseleccion == '4':
            print("Has seleccionado Cubo\n")
            altura = int(input("Introduce la altura\n"))
            anchura = int(input("Introduce la anchura\n"))
            profundidad = int(input("Introduce la profundidad\n"))
            Cu = Cubo(altura, anchura, profundidad)
            lista.append(Cu)
            print("Cubo Creado\n")

        elif subseleccion == '5':
            print("Has seleccionado Esfera\n")
            radio = int(input("Introduce el radio\n"))
            E = Esfera(radio)
            lista.append(E)
            print("Esfera Creada\n")

        else:
            print("La figura seleccionada no existe\n")
            subseleccion = CrearObjeto()

    elif seleccion == '2':
        if len(lista)>0:
            leerListado()
        else:
            print("No se ha creado ningun objeto\n")

    elif seleccion == '3':
        borrarFigura()


    elif seleccion == '4':
        on = -1



    else:
        print("Esa opcion no existe")



