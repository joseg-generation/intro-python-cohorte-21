

# Realizar: Suma, Resta, Multiplicación y División de dos números

# Se definen las funciones para cada operación
# Definir función que imprima resultado
# Capturar datos para realizar las operaciones (entrada del usuario: input)

# Al utilizar funciones --- Se declara y después se invoca

# Operaciones matemáticas 
def sumar(num1, num2):
    return num1 + num2
   

def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1*num2


def dividir(num1, num2):
    return num1/num2


# Función para imprimir
def imprimir_resultado(resultado):
    print(f"El resultado de la operación es: {resultado}")

print("Bienvenido a la APP de Calculadora!")
operacion_a_realizar = input("Indica la operación matemática que deseas realizar: sumar, resta, multi, divide: ")

if (operacion_a_realizar == "sumar" or operacion_a_realizar == "restar" or operacion_a_realizar == "multi" or operacion_a_realizar == "divide"):
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if (operacion_a_realizar == "sumar"):
        resultado = sumar(num1, num2)
    elif (operacion_a_realizar == "restar"):
        resultado = restar(num1, num2)
    elif (operacion_a_realizar == "multi"):
        resultado = multiplicar(num1, num2)
    elif (operacion_a_realizar == "divide"):
        resultado = dividir(num1, num2)
    else:
        print("Opción no válida!!")
 
    imprimir_resultado(resultado)
else:
    print("Opción no válida!!")