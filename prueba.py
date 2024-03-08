"""genrador de nombre de usuario : solicita al usuario su nombre, apellido y
 año de nacimiento, y generar un nombre de usuario combinandolos

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Birthday = input("Ingrese el año de nacimiento: ")

print("Su nombre de usuario es: "Nombre + Apellido + Birthday) 
print(f"Su nombre de usuario es: {Nombre}{Apellido}{Birthday}")
print("Su nombre de usuario es: {}{}{}".format(Nombre,Apellido,Birthday))"""

#Calcular el IMC de una persona

"""Altura = input("ingrese su altura en metros: ")
Altura= float(Altura)

Peso = float(input("Ingrese su peso en Kilogramo: "))

IMC = Peso / (Altura**2)

print("Su IMC es: ", IMC)"""


#adivinar el numero

"""import random

Numero_Para_Adivinar = random.randint(1,100)
Numero_Del_Usuario = int(input("Adivina el numero: "))

if Numero_Para_Adivinar < Numero_Del_Usuario:
    print("El numero es demasiado alto")
elif Numero_Para_Adivinar > Numero_Del_Usuario:
    print("El numero es demasiado bajo")
else:
    print("GANASTES!!!!!")"""


#Listas

"""Lista = [1,2,3,4,5,6,7,8,9]
Lista2 = [3.5,6.5,9.3,8.2]
Lista3 = ["Alejandro",2004,1.87,False]

Tabla = [[1,2,3],
         [4,5,6],
         [7,8,9]] 

print(Tabla[1][0])
print(Lista2)
Lista2.append("hola") #para agregar un dato a la lista
print(Lista2)
"""

#cojuntos

"""Conjunto1 = {1,2,3,4,5}
Conjunto2 = {4,5,6,7,8}

print(Conjunto1.union(Conjunto2))
print(Conjunto1.intersection(Conjunto2))
print(Conjunto1.difference(Conjunto2))"""

#Lista de compra

"""Elemento_Lista_Compra =  ""
Lista_Compra = []
Contador_Elementos = 0




while Elemento_Lista_Compra != "fin":
    Elemento_Lista_Compra = input("Por favor ingrese un elemento de la lista de compra:")
    Contador_Elementos+=1

    if Elemento_Lista_Compra != "fin":
        Lista_Compra.append((Contador_Elementos,Elemento_Lista_Compra))

print("\n"*20)
for Elemento in Lista_Compra:
    print("{}. {}".format(Elemento[0], Elemento[1]))
"""

#Aplicacion para guardar libros
"""Lista_Libros = []

while True:
    Nombre = input("Ingrese el nombre del libro: ")
    Autores = input("Ingrese los autores del libro separados por comas: ")
    Numero_Pagina =  int(input("Ingresse el numero de paginas del libro:"))

    Libro = {
        "Nombre": Nombre,
        "Autores": Autores,
        "Numero_de_paginas": Numero_Pagina
        
    }
    Lista_Libros.append(Libro)
    Terminar = input("Desea Terminar? (S/N)")
    if  Terminar == "s":
        break

for Libro in Lista_Libros:
    
    print(f"El libro {Libro['Nombre']} fue escrito por {Libro['Autores']} y tiene {Libro['Numero_de_pagina']} pagina")
"""

    

#juego 21
import random

JUEGO=[]
while True:
    print('bienvenido a mi casino')
    Jugador = random.randint(2, 26)
    Dealer = random.randint(2, 26)
    while True:
        print('el jugador saco: ',Jugador, 'el dealer saco: ',Dealer)
        Quiere_Mas_Cartas = input('quiere mas cartas? S/N')
        if Quiere_Mas_Cartas == 's':
            Jugador =Jugador + random.randint(1, 13)
        else:
            if Jugador == 21 or (Jugador > Dealer and Jugador <21):
                print('gano el jugador')
                JUEGO.append('Jugador')
                break
            elif Jugador == Dealer:
                print('Gano el diler') 
                JUEGO.append('Dealer')
                break
            else:
                print("gano el dealer")
                JUEGO.append('Dealer')
                break         
    preguntar_si_acaba_el_juego = input('Desea terminar el juego? S/N')
    if preguntar_si_acaba_el_juego == 's':
        break

        
    



