""" 
Ejercicio 3
Programa que compruebe si una variable está vacia y si esta vacia,
rellenarla con texto en minusculas 
y mostrarlo en mayusculas"""

texto = " "

if len(texto.strip())<=0:
    texto = "minuscula"
    print(texto.upper())
else:
    print ("Texto no vacio")