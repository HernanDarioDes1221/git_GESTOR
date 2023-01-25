from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db 
from pydantic import BaseModel, constr, validator
import helpers


class ModeloCliente(BaseModel):
        dni: constr(min_length=3, max_length=3)
        nombre: constr(min_length=2, max_length=30)
        apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente):
    @validator('dni')
    def validar_dni(cls, dni):
        if helpers.dni_valido(dni, db.Clientes.lista):
            return dni            
        raise ValueError("Cliente ya existente o DNI incorrecto")
          
      
# Lo primero es crear una aplicacion de tipo FastAPI

app = FastAPI(
      title="API del Gestor de Clientes",
      description="Ofrece diferentes funciones para gestionar los clientes"
      )

# Cuando se tienen simbolos diferentes se deben definir unas cabeceras para que las reconosca dentro del scrip
headers = {"content-type": "charset=utf-8"}

'''
# Creamos una funcion asincrona que me permite que no se bloquee el proceso, sino que se ejecute paralelamente en la memoria 
# Utilizamos un decorador para poder llamar la funcion, y le definimos la ubicacion '/' Raiz, como solo es una funcion de consulta utilizo el metodo GET

@app.get("/")
async def index():
        content = {"mensaje":"!Hola Mundo!"}
        return JSONResponse(content=content, headers=headers )

@app.get('/html/')
async def html():
        content = """"
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>¡Hola mundo!</title>
            </head>
            <body>
                <h1>¡Hola mundo!</h1>
            </body>
            </html>
        """
        return Response(content=content, media_type="text/html")
'''

@app.get('/clientes/', tags=['CLIENTES'])
async def clientes():
        content = [ cliente.to_dict() for cliente in db.Clientes.lista]
        return JSONResponse(content=content, headers=headers)


@app.get('/clientes/buscar/{dni}', tags=['CLIENTES'])
async def clientes_buscar(dni = str):
        cliente = db.Clientes.buscar(dni=dni)
        if not cliente:
                raise HTTPException(status_code = 404, detail="Cliente no encontrado")
        return JSONResponse(content=cliente.to_dict(), headers=headers)


@app.post("/clientes/crear/" , tags=['CLIENTES'])
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        headers = {"content-type": "charset=utf-8"}
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no creado")




@app.put('/clientes/actualizar/', tags=['CLIENTES'])
async def clientes_actualizar(datos: ModeloCliente):
      if db.Clientes.buscar(datos.dni):
            cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
            if cliente:
                  return JSONResponse(content=cliente.to_dict(), headers=headers)
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
      
@app.delete('/clientes/borrar/{dni}', tags=['CLIENTES'])
async def clientes_borrar(dni: str):
        if db.Clientes.buscar(dni=dni):
            cliente = db.Clientes.borrar(dni=dni)
            return JSONResponse(content=cliente.to_dict(), headers=headers)
        raise HTTPException(status_code=404, detail="Cliente no encontrado")


print ("Servidor de la API...")