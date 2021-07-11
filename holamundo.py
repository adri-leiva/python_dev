print("Hola mundo");




#comentario lineal
"""comentario multilinea (ctrl shift a) """ 





#VARIABLES (debilmente tipado)
variable_X = "valorX"; 
variable_Y = "ValorY"






#CONCATENACION (  +; f; format(...)  )
concateno = variable_X + " " + variable_Y
print( f"{variable_X} {variable_Y}")
print ("cadena original {} {} mas texto" . format(variable_Y,variable_X))
print (variable_X , variable_Y)







#TIPOS DE DATOS

nada = None
cadena = "es una cadena"
entero =  7
flotante = 13.4
booleano = True 
booleano = False

#tipo lista (list)
arreglo = [10,"cadena" , 11,5,4]
print(arreglo.pop(0))

#tipo tupla (tuple)
tupla = ("cadena", "a")

#diccionario- arreglos asociativos 
diccionario = {
    "index1" : "valor",
    "index2": "valor2"
}

#rango (devuelve un rango entre un numero y otro)
rango=range(9)

#metodo util ( devuelve una cadena indicando el tipo de dato con el que se trabaja)
print (type(range))




#CONVERTIR UN TIPO DE DATOS A OTRO
numeroEntero = int (7)
cadena = str(2)
numerofloat= float (8)






#ENTRADA DE DATOS (ingresa una cadena)
nombre = input ("¿Cual es tu nombre?")
