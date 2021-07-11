""" 
EJERCICIO 7 
Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario

"""

num_a = int(input ("Ingrese el valor de a: "))
num_b = int(input ("Ingrese el valor de b: "))

resultado = " "
for indice in range(num_a,num_b):
  if  indice%2 != 0:
       resultado = resultado + str(indice) + ";"
print (resultado)   