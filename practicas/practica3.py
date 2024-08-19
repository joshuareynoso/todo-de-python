#PROBEMA DE LA CAJA 

#inicio del programa
print("Bienvenido al programa que resta a una caja ")

def menu():
    print(" 1.agregar mas ancho a la caja")
    print(" 2.agregar mas largo a la caja")
    print(" 3.restar el ancho de la caja ")
    print(" 4.restar el largo de la caja")


menu()
while True:
    opciones=int(input("ingrese un opcion"))
   
    if opciones ==1:
        caja=int(input("ingre el ancho y largo de su caja :"))
        anchodelacaja=int(input("ingrese el ancho que quieres  agragar:"))
        calculo= caja + anchodelacaja 
        print(calculo)

    if opciones ==2:
        caja=int(input("ingre el ancho y largo de su caja :"))
        largodelacaja=int(input("ingrese el largo  que quieres agregar:"))
        calculo2= caja + largodelacaja 
        print(calculo2)

    elif opciones ==3:
        caja=int(input("ingre el ancho y largo de su caja :"))
        anchodelacaja=int(input("ingrese el ancho que quieres sacar:"))        
        calculo1= caja - anchodelacaja
        print(calculo1)

    elif opciones ==4:
        caja=int(input("ingre el ancho y largo de su caja :"))
        largodelacaja=int(input("ingrese el largo  que quieres sacar:"))
        calculo3= caja - largodelacaja
        print(calculo3)    
   
    
    
  

