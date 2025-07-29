
# Variables y tipos de datos

# variable = valor que se le asigna
# variables deben ser lo mas descriptivas en lo posible
# nomeclatura snare_case (python)
# camelCase (JavaScript)

#Enteros Integer --> se almacen números enteros

edad_estudiante = 44
entero_uno = 100

# type() es una función incoporada de python que nos entrega el tipo de dato en de variable
type(entero_uno)

# print(f"Esto es un texto y le podemos incluir una variable: {entero_uno}")
# print("Esto es un texto y le podemos incluir una variable: {entero_uno}")

# De punto flotante - Float  --> Tipo de datos número decimales

promedio_de_notas = 6.5

# Cadenas, String, texto, cadenas de caracteres --> siempre van entre comillas

saludo_de_bienvenida = 'Hola equipo, buena semana!!'

promedio_de_notas = "hola mundo"


# Boolean -> Booleano Permite almacenar dos posibles valores Verdadero o Falso y su utilidad principal es para tomar decisiones.

# En python True / False --> La primera letra en Mayúscula

es_de_dia = False

# gestión de pago de suscripción

mesualidad_pagada = True


print(type(es_de_dia))


# manejar información de un usuario (Netflix)

nombre_de_usuario = "Juanito"
apellido_de_usuario = "Pérez"
email = "email@gmail.com"
contrasena = "1203123123"

mensualidad_pagada = True
pelicula_fav_1 = "Batman"
pelicula_fav_2 = "Superman"



print("Login exitoso!")
print(f"Bienvenido a Netflix {nombre_de_usuario} {apellido_de_usuario}")
print(f"Tu lista de pelis es: {pelicula_fav_1}, {pelicula_fav_2}")