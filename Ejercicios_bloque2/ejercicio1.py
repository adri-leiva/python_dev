""" 
Ejercicio 1 
Hacer un programa que tenga una lista de 8 nros enteros y haga los siguiente:
- Recorrer la lista
- Ordenarla y mostrarla
- Mostrar su longitud 
- Buscar un elemento (Que el usuario pida por teclado"""

import random
from warnings import formatwarning



def crearListaAleatoria(longiutd_arreglo=1):
    #Crea una lista de nros enteros, de longitud n
    nuevaLista = []
    for indice in range(0,longiutd_arreglo):
        nuevaLista.append(random.randint(1,100))

    return (nuevaLista) 


listaRamdon=crearListaAleatoria(8)

print ("RECORRO LA LISTA")
for elemento in listaRamdon:
    print (elemento)

print ("ORDENO LA LISTA y LA MUESTRO")
listaRamdon.sort()
print (listaRamdon)

print (f"LONGITUD:  {len(listaRamdon)}")

print ("BUSCAR ELEMENTO")
elementoABuscar = int(input ("Ingrese el elemento a buscar: "))
print(elementoABuscar in listaRamdon)
