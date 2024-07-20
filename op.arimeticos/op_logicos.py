#AND (tienen que tener las dos condiciones verdadero para que se a verdadero) 

resultado = True & True #devolvera verdadero 
resultado1 = False & True #devolvera falso 
resultado2 = True & False #devolvera falso 
resultado3 = False & False #devolvera falso 

#OR (solo devuelve falso si las dos condiciones se cumplen)

resultado4 = True | True #devolvera verdadero 
resultado5 = False | True #devolvera verdadero
resultado6 = True | False #devolvera verdadero
resultado7 = False | False #devolvera falso 


#NOT (nos invierte  el valor )

resultado8 = not True #devolvera falso
resultado9 =not  False #devolvera verdadero

print(resultado)