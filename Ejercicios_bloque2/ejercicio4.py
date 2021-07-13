""" Ejercicio 4
Crear un script que tenga 4 variables, una lista, 
un string, un entero y un booleano y que imprima 
un mensaje segun el tipo de dato de cada variable. 
Usar Funciones """

""" def determinarElTipoDeVariable(variable):
    print (type(variable).__name__) """

var1 = ["a","b",1]
var2 = "string"
var3 = 3
var4 = True

validarTipo = lambda variable: type(variable).__name__

print(str(validarTipo(var1)))
print(str(validarTipo(var2)))
print(str(validarTipo(var3)))
print(str(validarTipo(var4)))
