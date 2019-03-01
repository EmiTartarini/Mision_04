#Emiliano Tartarini A01372663
#Grupo 02

def recibirTiempo(h,min,seg):
   if h>24or h<0:
      return "ERROR"
   if h<12:
      return (h,":",min,":",seg)
   if h==24:
      h2= h-24
      return (h2,":",min,":",seg)
   if h > 12:
      h1=h - 12
      return (h1,":",min,":",seg)


def main():
   h= int(input("escribir la h"))

   min= int(input("escribir los min"))

   seg= int(input("escribir los seg"))

   print(recibirTiempo(h,min,seg))

main()