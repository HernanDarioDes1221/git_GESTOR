import copy
import csv
import helpers
import unittest
import database as db
import config

class TestDatabase(unittest.TestCase):

   #Creamos el metodo setUp para preparar los test 
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente("15J", "Marta", "Perez"),
            db.Cliente("48H", "Manolo", "Lopez"),
            db.Cliente("28Z", "Ana", "Garcia")
        ]

    
    # Esta es la primera prueba 
    
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("15J")
        cliente_inexistente = db.Clientes.buscar("99X")
        # La funcion assertIsNotNone define que el cliente si se encuentra en la lista 
        self.assertIsNotNone(cliente_existente)
        #La funcion assertIsNone comprueba que realmente este campo esta vacio y que el cliente no existe
        self.assertIsNone(cliente_inexistente)

    
    # Creamos un nuevo test para probar la creacion de un nuevo usuario 
        
    def test_crear_cliente(self):
        
        nuevo_cliente = db.Clientes.crear("39X", "Hector", "Costa")
        
        #Con la siguiente prueba comprobamos la longitud de la lista, pasando de 3 a 4 
        
        self.assertEqual(len(db.Clientes.lista), 4)
        
        # Con las siguientes pruebas comprobamos si existe el nombre, apellido y dni

        self.assertEqual(nuevo_cliente.dni, "39X")
        self.assertEqual(nuevo_cliente.nombre, "Hector")
        self.assertEqual(nuevo_cliente.apellido, "Costa")


    # Creamos otro test para modificar clientes 

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar("28Z"))
        cliente_modificado = db.Clientes.modificar("28Z", "Mariana", "Garcia")
        self.assertEqual(cliente_a_modificar.nombre, "Ana")
        self.assertEqual(cliente_modificado.nombre, "Mariana")


    # Creamos un test de borrar cliente 

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("48H")
        cliente_rebuscado = db.Clientes.buscar("48H")
        self.assertEqual(cliente_borrado.dni, "48H")
        self.assertIsNone(cliente_rebuscado)


    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223112S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))


    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'Garcia')

        dni, nombre, apellido = None, None, None
        with open (config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'Garcia')