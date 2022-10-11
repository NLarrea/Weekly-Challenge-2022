# Reto #21
# CALCULADORA .TXT
# Fecha publicación enunciado: 23/05/22
# Fecha publicación resolución: 01/06/22
# Dificultad: MEDIA
#
# Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
# - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

import re

# open the Challenge21.txt file to read
with open("Challenge21.txt", "r") as file:
    content = "" # empty string to save the elements
    for line in file:
        content += line.replace("\n", "") # to save the content of the file in a "one-line" single string

# print(content) # 5+2-1*8-15+4/2
# to make a list of numbers
numbers = re.split('[+\-*/]', content) # list of numbers, but they're strings
numbers = [eval(i) for i in numbers] # converts strings list in int list
# print(numbers) # [ 5, 2, 1, 8, 15, 4, 2 ]
# to make a list of operators
operators = [i for i in content if not(i.isnumeric())] # list of operators
# print(operators) # [ '+', '-', '*', '-', '+', '/' ]
result = numbers[0]
for pos in range(len(operators)):
    if operators[pos] == "+": result += numbers[pos+1]
    elif operators[pos] == "-": result -= numbers[pos+1]
    elif operators[pos] == "*": result *= numbers[pos+1]
    elif operators[pos] == "/": result /= numbers[pos+1]
    else: print("It is not possible to solve this.")
print("The result of '{0}' is: {1}".format(content, result))