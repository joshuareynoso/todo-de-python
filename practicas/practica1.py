#inicio del programa
lista =  []
sueldo = "tu sueldo es de 100000mil por semana"
def empleo():

    while True:
        empleado = str(input("cual es su nombre:"))   
    
        if empleado == "nico":
            print("faltan dos pasos para terminar el inicio de sesion")
            break
            #es para ingrensar un dato en una lista 
        
        elif empleado != "nico":
            print("su nombre de usuario es inconrecto")
                    

    while True:
            correo=str(input("ingrese su correo:"))   
            if correo == "pepe@gmail.com":
                print("falta un paso para poder iniciar secion")
                break
            else:
                print("tu correo electronico esta mal")
            
    while True:

            contraseña_del_empleador =str(input("ingrese su contraceña:"))
            if contraseña_del_empleador == "pepe1":
                print("ya pudo iniciar secion")
                lista.append(sueldo)
                break
                

            else:
                print("tu contraceña es incorrecta")
            
empleo()
print(lista)