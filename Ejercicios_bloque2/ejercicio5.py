""" 
EJERCICIO 5: 
Crear una lista con el contenido de esta tabla:

Accion          Aventura            Deportes
GTA             ASSINS              FIFA 21
COD             CRASH               PRO 21
PUGB            POP                 MOTO_GP21

Mostrar esta informacion ordenada
"""

tabla = [
    
    {
        "categoria" : "ACCION",
        "juegos" : ["GTA", "COD", "PUGB"]
    },

    {
        "categoria" : "AVENTURA",
        "juegos" : ["ASSINS", "CRASH", "POP"]
    },

    {
        "categoria" : "DEPORTE",
        "juegos" : ["FIFA21", "PRO21", "MOTO_GP21"]
    }

]

for elementoCategoria in tabla:
    print ("\n" + elementoCategoria['categoria'])
    for elementoJuego in elementoCategoria['juegos']:
        print (elementoJuego)