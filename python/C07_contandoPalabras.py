# Reto #7
# CONTANDO PALABRAS
# Fecha publicación enunciado: 14/02/22
# Fecha publicación resolución: 21/02/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# Creamos un string con todos los caracteres que no queremos tener en cuenta:
chars_to_replace = ""
# ASCII: letras mayus: [65-90], letras minus: [97-122]
i=32
while i<127:
    if i<65 or (i>90 and i<97) or i>122: # si i no está en este rango, no es una letra mayus/minus
        chars_to_replace += chr(i)
    i += 1

# Convertimos la frase en una lista de palabras que sean válidas:
def extraerPalabras(frase:str):
    frase = frase.lower() # pasamos la frase a minus
    # Sustituimos los caracteres que no queremos por espacios:
    for spChar in chars_to_replace:
        frase = frase.replace(spChar,' ')
    # Devolvemos la frase convertida en una lista de palabras:
    return frase.split()

# Contamos cuántas veces aparece cada palabra y lo guardamos en el diccionario:
def contarVecesPalabra(lista:list):
    # Creamos una lista vacía para guardar las palabras SIN REPETIRLAS:
    noRepes = []
    i = 0
    # Guardamos las palabras SIN REPETRILAS en la lista vacía:
    while i<len(lista):
        if i == 0: # siempre añade la primera palabra de la lista a la lista de noRepes:
            noRepes.append(lista[0])
        elif i!=0 and (lista[i] not in noRepes): # si ya hay palabras, si no estaban ya, las mete
            noRepes.append(lista[i])
        i += 1
    i = 0
    cuenta = 0 # inicio de la cuenta
    # Contamos cuántas veces aparece cada palabra en la lista comparándola con la otra:
    while i<len(noRepes):
        j = 0
        while j<len(lista):
            if noRepes[i] == lista[j]:
                cuenta += 1
            j += 1
        # RESULTADO:
        print("La palabra {0} aparece {1}".format(noRepes[i],cuenta),"vez" if cuenta==1 else "veces")
        cuenta = 0 # reinicio de la cuenta para la siguiente palabra
        i += 1

# Convertimos una frase cualquiera en una lista de palabras que sean válidas:
listaPalabras = extraerPalabras("Hola, mi nombre es larrea. Mi nombre completo es Naia Larrea (NLarrea).")
# Contamos cuántas veces aparece cada palabra y lo guardamos en el diccionario:
contarVecesPalabra(listaPalabras)