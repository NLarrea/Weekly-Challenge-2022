# Reto #24
# ITERATION MASTER
# Fecha publicación enunciado: 13/06/22
# Fecha publicación resolución: 20/06/22
# Dificultad: FÁCIL
#
# Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

print("\nFOR")
for i in range(1,100+1):
    print(i)

print("\nWHILE")
i = 1
while i<=100:
    print(i)
    i += 1

print("\nWHILE(TRUE)")
i = 1
while True:
    print(i)
    if i == 100: break
    i += 1

print("\nFUNCTION")
def print100(n):
    if n <= 100:
        print(n)
        print100(n+1)
print100(1)