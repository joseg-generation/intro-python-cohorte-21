
# Funciones incorporadas  --> Vienen incluidas dentro del lenguaje:

# print("Texto que se imprime")
range(0, 45)

numers = [23,45,67,89,3,4,67,78,23,34, 56, 567, 56,2345,345,34,1,6,7]

# print(numers[0]+numers[1])

# print(sum(numers))  # sumar una lista de números


# Calcular el máximo de una lista de números
numero_max = 0
for numero in numers:
    if numero > numero_max:
        numero_max = numero
print(numero_max)

print(max(numers))