#Emiliano Tartarini A01372663
#Grupo 02

def calcularMonto(montos):

    if montos >= 1 and montos <= 9:
        valor=(montos*2300)
        return valor
    elif montos >= 10 and montos <= 19:
        valor=(montos * 2300)* .85
        return valor
    elif montos >= 20 and montos <= 49:
        valor=(montos * 2300)* .78
        return valor
    elif montos >= 50 and montos <= 99:
        valor=(montos * 2300)* .65
        return valor
    elif montos <=0:
        print("error")
    else:
        valor=(montos * 2300) * .58
        return valor

def main():
   bulto=int(input("¿cuanto se compro?:"))
   monto=calcularMonto(montos)
   print("El precio final es $",valor)
