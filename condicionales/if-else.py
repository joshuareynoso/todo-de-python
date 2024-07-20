#if True <
    #eston se ejecuta si es verdadero 

#if False
    #esto o se ejecuta porque es falso 

#if anidados y elif 
edad = 9

if edad >= 18: 
    print("puedes pasar")
else:
    print("no puedes pasar")


sueldo_mensual = 300000
gasto_mensual = 150000

if sueldo_mensual > 500000:
    
    if  sueldo_mensual - gasto_mensual > 120000:
        print("estas bien economicamente en cualquier parte del mundo ")
    else:
        print("estas gastando mucho ")

elif sueldo_mensual > 200000:
   
    if sueldo_mensual - gasto_mensual > 160000:
        print("estas bien economicamente  en latinoamirica")
    else:
        print("estas gastando mucho ")

else:
    print("sos pobre")