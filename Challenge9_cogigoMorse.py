morseDictionary = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....",
    "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "Ñ":"--.--", "O":"---",
    "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--",
    "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-",
    "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", ".":".-.-.-", ",":"--..--",
    "?":"..--..", '"':".-..-.", "/":"-..-."
}

def esMorse(frase:str):
    for letter in frase:
        if letter!="." and letter!="-" and letter!=" ":
            return 0 # devuelve 0 si no es Morse
    return 1 # devuelve 1 si es Morse

def aMorse(frase:str):
    nuevaFrase = "" # creamos un string vacío
    for letter in frase: # por cada letra de la frase:
        for key in morseDictionary.keys(): # por cada "key" de la lista de llaves del diccionario:
            if letter.upper() == key: # si la letra en mayúscula coincide con alguna "key":
                nuevaFrase += str(morseDictionary[key]) # nuevaFrase = al value de la llave guardada en "key"
                nuevaFrase += " " # añadimos para separar cada caractere
                break # decimos que deje de buscar parecidos en la lista
            elif letter == " ": # si es igual a un espacio:
                nuevaFrase += " " # añade el espacio --> habrá 2 espacios entre palabras en Morse
                break # decimos que deje de buscar parecidos en la lista
            if letter.upper() not in morseDictionary.keys(): # si letter no aparece en el diccionario:
                return "\nERROR: hay errores en la sintaxis de la frase introducida\n" # nuevaFrase = ERROR
    return nuevaFrase # devolvemos la nueva frase, en Morse

def aNatural(frase:str):
    listaPalabras = extraerPalabras(frase) # creamos una lista con las palabras de la frase
    nuevaFrase = "" # creamos un string vacío
    for letter in listaPalabras: # por cada letra de la frase:
        for value in morseDictionary.values(): # por cada "value" de la lista de valores del diccionario:
            if letter==value and letter!=" ": # si la letra (mayus, porque es de la lista) coincide en "value":
                nuevaFrase += getKeyFromValue(value) # obtenemos la llave conociendo el valor
                break
            elif letter == " ": # si la "letra" de la lista es un " ":
                nuevaFrase += " " # añadimos un espacio (para separar palabras entre sí)
                break # decimos que deje de buscar en la lista
            if letter not in morseDictionary.values(): # si letter no aparece en el diccionario:
                return "\nERROR: hay errores en la sintaxis de la frase introducida\n" # nuevaFrase = ERROR
    return nuevaFrase # devolvemos la nueva frase

def extraerPalabras(frase:str):
    frase += " " # para solucionar IndexError
    listaPalabras = [] # creamos una lista vacía para guardar las palabras
    palabra = "" # creamos un string vacío
    i = 0
    while i<len(frase)-1: # hasta len(frase)-1 porque le he añadido un char más con: frase += " "
        if i==0 and frase[i] == " ": # si hay espacio blanco antes de que comience la frase, lo quitamos
            continue
        if frase[i]!=" " and frase[i+1]!=" ": # si estamos dentro de una palabra
            palabra += frase[i]
        elif frase[i]!=" " and frase[i+1]==" ": # si estamos al final de una palabra
            palabra += frase[i] # completamos la palabra
            listaPalabras.append(palabra) # añadimos la palabra a la lista
            palabra = "" # reseteamos la palabra
        elif frase[i]==" " and frase[i+1]==" ": # si hay 2 espacios en blanco seguidos:
            listaPalabras.append(" ") # guardamos 1 en la lista --> para separación entre palabras
        i += 1
    return listaPalabras

def getKeyFromValue(value): # para obtener el valor de key conociendo value
    keys = [k for k, v in morseDictionary.items() if v == value]
    if keys: # si está en la lista, lo devuelve
        return keys[0]
    return None # si no está, devuelve 'None'

frase = input("Introduce una frase: ")
es_morse = esMorse(frase)
if es_morse == 0: # no es Morse
    nuevaFrase = aMorse(frase)
    if nuevaFrase != "\nERROR: hay errores en la sintaxis de la frase introducida\n":
        print("\nLa palabra o frase:\n""{0}""\n\nen Morse es:\n{1}".format(frase,nuevaFrase))
    else:
        print(nuevaFrase)
elif es_morse == 1: # es Morse
    nuevaFrase = aNatural(frase)
    if nuevaFrase != "\nERROR: hay errores en la sintaxis de la frase introducida\n":
        print("\nLa palabra o frase:\n""{0}""\n\nen natural es:\n{1}".format(frase,nuevaFrase))
    else:
        print(nuevaFrase)