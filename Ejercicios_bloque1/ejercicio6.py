""" Ejercicio 6
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""


for num in range(1,11): 
    print (f"\n ______TABLA del {num}_________ ")
    for indice in range(1,11):
        print (f"{num}*{indice}={num*indice}")
