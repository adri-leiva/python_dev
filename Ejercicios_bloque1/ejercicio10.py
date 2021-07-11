""" 
EJERCICIO 10
El programa tiene que pedir la nota de 15 alumnos 
y sacar por pantalla cuantos han aprobado y cuantos
 han suspendido.
"""

cant_aprob = 0;
cant_desaprob =0;

for contador in range (0,15):
    nota = int (input (" Ingrese nota: "))
    if nota >= 7:
        cant_aprob =+1

print (f"Cantidad de aprobados: {cant_aprob} y desaprobados {15-cant_aprob}"  )
