# Crear el diccionario con información personal 
informacion_personal = {
    "nombre": "Ronald",
    "edad": 49,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor para representar la profesión de la persona
informacion_personal["profesion"] = "Analista"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989647321"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Diccionario Final:")
print(informacion_personal)