import re
import os
import platform


# El siguiente modulo me permite identificar el sistema operativo 
import platform

#Creamos la funcion auxiliar que me permite limpiar el contenido 

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Creamos una funcion para leer texto por teclado 

def leer_texto(longitud_min = 0, longitud_max = 100, mensaje = None):
    print(mensaje) if mensaje else None

    while True: 
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        

# Funcion para validar el DNI

def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$',  dni):
        print('DNI incorrecto, debe cumplir el formato') 
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True
      
