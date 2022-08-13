 # Reto #1
 # ¿ES UN ANAGRAMA?
 # Fecha publicación enunciado: 03/01/22
 # Fecha publicación resolución: 10/01/22
 # Dificultad: MEDIA
 #
 # Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 # Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 # NO hace falta comprobar que ambas palabras existan.
 # Dos palabras exactamente iguales no son anagrama.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

# Definición de las variables a utilizar:
while(True):
    cad1 = input("Introduce la primera palabra: ")
    cad2 = input("Introduce la segunda palabra: " )
    if not(cad1.isalpha()) or not(cad2.isalpha()):
        print("ERROR: las dos palabras deben contener solo letras!\n")
    else:
        break

# Si no tienen el mismo tamaño no merece la pena compararlos:
if len(cad1) != len(cad2):
    print("\n{0} y {1} no son anagramas".format(cad1,cad2))
# Si son la misma palabra, no son anagramas:
elif cad1.lower() == cad2.lower():
    print("\n{0} y {1} son la misma palabra, no son anagramas".format(cad1,cad2))
else:
    # Creamos cadenas vacías para almacenar los strings como arrays de caracteres:
    arr1,arr2 = [],[]
    # Almacenamos los strings en las cadenas:
    for letter in cad1:
        arr1.append(letter.lower())
    for letter in cad2:
        arr2.append(letter.lower())
    # Ordenamos los dos arrays para compararlos:
    arr1.sort()
    arr2.sort()

    # CONDICIONES DE NO IGUALDAD:
    if arr1 != arr2:
        print("\n{0} y {1} no son anagramas".format(cad1,cad2))
    else:
        print("\n{0} y {1} son anagramas".format(cad1,cad2))