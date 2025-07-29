
# Listas -- > permiten almacenar una serie de elementos separados por comas.

peliculas_favoritas = []

# print(peliculas_favoritas)

peliculas_favoritas.append("Batman")
peliculas_favoritas.append("Superman")
peliculas_favoritas.append("RoboCop")


# print(peliculas_favoritas)

# Carrito de compras --Cuando van al supermercado

#Entramos al super
carrito = []

#Pasillo de las frutas
frutas = []
frutas.append("Manzanas")
frutas.append("Peras")

#print(carrito)

# Pasillo de granos
granos = []
granos.append("Arroz")


carrito.append(frutas)
carrito.append(granos)

# [ ['Manzanas', 'Peras'], ['Arroz'] ]
#              0               1

frutas.append("Mango")

# print(carrito)

# estructura de datos clave /valor (Diccionarios)
# palabra (clave): definición (valor)

# manejar información de un usuario (Netflix)
print("Bienvenido a Nexflix, registre su cuenta!!")
print("##########################")
nombre_de_usuario = input("Ingrese su nombre: ")
apellido_de_usuario = input("Ingrese su apellido: ")
email = input("Ingrese su email: ")
contrasena = input("Ingrese su contraseña: ")
edad = input("Ingrese su edad: ")

user = {
   "name": nombre_de_usuario,
   "last_name": apellido_de_usuario,
   "email": email,
   "password": contrasena,
   "age": edad,
   "pay": False,
   "fav_movies": []
}

print("######################")
print("### Registro exitoso! ###")
print("######################")
print(f"Sus datos son: {user['name']} {user['last_name']} {user["email"]}")

# fav_movie_1 = input("Ingresa tu película fav 1: ")
# fav_movie_2 = input("Ingresa tu película fav 2: ")


# user["fav_movies"].append(fav_movie_1)
# user["fav_movies"].append(fav_movie_2)

#print(f" Tu peliculas fav son: {user["fav_movies"][0]} y {user["fav_movies"][1]}")

# user_2 = {
#    "name": "Pedro",
#    "last_name": apellido_de_usuario,
#    "email": email,
#    "password": contrasena,
#    "age": 20,
#    "pay": False,
#    "fav_movies": []
# }