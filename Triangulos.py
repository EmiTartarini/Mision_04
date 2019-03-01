#Emiliano Tartarini A01372663
#Grupo 02

def TrianguloLados(L1,L2,L3):
    if L1<=0:
        return "Error"
    if L2<=0:
        return "Error"
    if L3<=0:
        return "ERROR"
    if L1==L2 and L2==L3:
        return "EQUILATERO"
    if L1==L3 and L2!=L1:
        return "ISOCELES"
    if L1!=L2 and L2==L3:
        return "ISOCELES"
    if L1!=L2 and L2!=L3 and L3!=L1:
        return "ESCALENO"


def main():
    L1= int(input("valor de lado:"))
    L2= int(input("segundo valor de lado:"))
    L3= int(input("tercer valor de lao:"))
    print(TrianguloLados(L1,L2,L3))

main()