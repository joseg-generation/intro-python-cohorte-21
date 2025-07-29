
# Hacer dinámicos los datos de nombre y apellido

name = input("Ingrese su nombre: ") # Detener la ejecución del programa y permitir el ingreso de un dato
last_name = input("Ingrese su apellido: ") # Detener la ejecución del programa y permitir el ingreso de un dato
job_name = input()

# App Incio de sesión
# Bienvenido, José Martínez

print("Bienvenido, " + name + " " + last_name) # concatenando el texto con los valores de las variables --> unir texto
print(f"Bienvenido, {name} {last_name}") # se formatea el texto y se permite inyectar las varibles de manera literal

print(name + " started their first Generation course today. They are training as a " + job_name + ". They found their cohort to be very <first adjective> but their teacher was, at least, <second adjective>. For lunch they have <first food> and <second food> while reviewing their notes. They feel <a feeling> but are determined to complete the course.")