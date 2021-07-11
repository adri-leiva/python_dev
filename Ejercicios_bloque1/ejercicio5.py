""" 
EJERCICIO 5
Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario
"""

num_a= int(input ("ingrese el valor de a:"))
num_b= int(input ("ingrese el valor de b:"))

num = 0
for num in range(num_a,num_b+1):
    print (num) 