import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("------------------------")
        print("  Bienvenido al Gestor  ")
        print("------------------------")
        print("[1] Listar los clientes ")
        print("[2] Buscar un cliente   ")
        print("[3] Anadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Salir               ")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == str("1"):
            print("Listando los clientes... \n")
            for cliente in db.Clientes.lista:
                print(cliente)
            
        elif opcion == str('2'):
            print("Buscando un cliente... \n")
            dni = helpers.leer_texto(3 , 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no econtrado.")

        elif opcion == str('3'):
            print("Anadiendo un cliente... \n")
            
            dni = None
            while True:
                dni = helpers.leer_texto(3 , 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente creado correctamente.")

        elif opcion == str('4'):
            print("Modificando un cliente... \n")
            dni = helpers.leer_texto(3 , 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                print("Cliente modificado correctamente.")
            
            else:
                print("Cliente no encontrado.")



            print("Borrando un cliente... \n")
            dni = helpers.leer_texto(3 , 3, "DNI (2 int y 1 char)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")


        elif opcion == str('6'):
            print("Saliendo... \n")

            break

        input("\nPresione ENTER para continuar...")


