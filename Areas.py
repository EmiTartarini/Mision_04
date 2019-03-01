#Emiliano Tartarini A01372663
#grupo 02

def calcularP(h1,B1,h2,B2):
    perimetroUno= (h1*2)+(B1*2)
    perimetroDos= (h2*2)+(B2*2)
    return perimetroUno, perimetroDos

def calcularA1(h1,B1):
    A1= h1*B1
    return A1

def calcularA2(h2,B2):
    A2= h2*B2
    return A2


def MayorIgual(A1,A2):
    if A1>A2:
        return "A1 es mayor"
    if A2>A1:
        return "A2 es mayor"
    if A1==A2:
        return "son iguales"

def main():
    h1= int(input("primer valor de la altura:"))
    B1= int(input("primer valor de la base:"))
    h2= int(input("segundo valor de altura:"))
    B2= int(input("segundo valor de base:"))
    calcularP(h1,B1,h2,B2)
    A1= calcularA1(h1,B1)
    A2= calcularA2(h2,B2)
    print(MayorIgual(A1,A2))

main()