

# bucle for in
# se utilizan normalmente cuando se conoce la cantidad de repeticiones

lista_de_estudiantes = ["Alejandra", "Luis", "Alberto", "José", "Daniel"]

top_10_chile = ["Batman", "Amy", "Casa De Papel"]

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
limite = int(input("Hasta que número quieres imprimir el FizzBuzz: "))

numeros = range(1, limite + 1) # En la lista que se genera no incluye el punto de corte (segundo número)

for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0: #devuelve implicitamente True o False
     print("FizzBuzz")
    elif numero % 3 == 0: # verificar si un número es divisible entre 3
     print("Fizz")
    elif numero % 5 == 0: # verificar si un número es divisible entre 5
     print("Buzz")
    else:
     print(numero)