# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Fecha publicación enunciado: 10/01/22
# Fecha publicación resolución: 17/01/22
# Dificultad: DIFÍCIL
#
# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
#

def fibonacci(n,fib_anterior,fib_anterior2):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib_anterior+fib_anterior2

# Creación e inicialización de las variables:
fib_actual = int(0)
fib_anterior = int(0)
fib_anterior2 = int(0)
i = 0

# Bucle:
while i<50:
    fib_actual = fibonacci(i,fib_anterior,fib_anterior2)
    print(fib_actual,end=" ")
    if i >= 2:
        fib_anterior2 = fib_anterior
    fib_anterior = fib_actual
    i += 1