""" 
Ejercicio 2
Escribir un programa que añada valores a una lista
mientras su longitud sea menor a 120 y 
luego mostrar la lista.
Plus Usar while y for.
 """
import random

def crearListaAleatoriaConFOR(longiutd_arreglo=1):
    #Crea una lista de nros enteros, de longitud n
    nuevaLista = []
    for indice in range(0,longiutd_arreglo):
        nuevaLista.append(random.randint(1,100))

    return (nuevaLista) 

def crearListaAleatoriaConWHILE(longiutd_arreglo=1):
    #Crea una lista de nros enteros, de longitud n
    nuevaLista = []
    indice =0
    while indice<120:
        nuevaLista.append(random.randint(1,100))
        indice += 1
    return (nuevaLista) 
    
print ("\n CON FOR")
listaRamdon=crearListaAleatoriaConFOR(120)
print (listaRamdon)

print ("\n CON WHILE")
listaRamdon2 =crearListaAleatoriaConWHILE(120)
print (listaRamdon)