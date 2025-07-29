
# sentencia if elif

# == igualdad
# > mayor que
# < menor que
# % módulo (resto)  -->>> LO
# / division 3/3 --> 1
# % resto 3%3 ---> 0


numero = int(input("Ingresa tu número: "))

# verificar si un número es divisible entre 3 y 5
if numero % 3 == 0 and numero % 5 == 0: #devuelve implicitamente True o False
    print("FizzBuzz")
elif numero % 3 == 0: # verificar si un número es divisible entre 3
    print("Fizz")
elif numero % 5 == 0: # verificar si un número es divisible entre 5
    print("Buzz")
else:
    print(numero)

