# Reto #10
# EXPRESIONES EQUILIBRADAS
# Fecha publicación enunciado: 07/03/22
# Fecha publicación resolución: 14/03/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a # ( c + d ) ] - 5 }
# - Expresión no balanceada: { a # ( c + d ) ] - 5 }
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def isBalanced(exp:str):
    openKey = "" # new empty string to save the open keys/brackets/parentheses
    for letter in exp:
        if letter=='{' or letter=='[' or letter=='(': # when open keys/brackets/parentheses:
            openKey += letter # add the key/bracket/parenthese to the string
        elif letter=='}' or letter==']' or letter==')': # when close keys/brackets/parentheses:
            if not openKey: return False # if string=empty, it's because there are more close than open keys/brackets/parentheses, so it's not balanced
            openKey = removeFromExpression(openKey,letter) # if the string is not empty: tries to delete de last open key/bracket/parenthese
    if openKey: # if string is not empty, returns False
        return False
    return True # if string is empty and there are no "errors", returns True

def removeFromExpression(exp:str, c):
    if not exp: return exp # if string is empty, returns the string
    if c == '}': # when c is a close key:
        if exp.endswith('{'): exp = exp[:-1] # if last char was an open key: removes the last char from string
        else: return exp # if the last char wasn't an open key, returns the string
    elif c == ']': # when c is a close bracket:
        if exp.endswith('['): exp = exp[:-1] # if last char was an open bracket: removes the last char from string
        else: return exp # if the last char wasn't an open bracket, returns the string
    elif c == ')': # when c is a close parenthese:
        if exp.endswith('('): exp = exp[:-1] # if last char was an open parenthese: removes the last char from string
        else: return exp # if the last char wasn't an open parenthese, returns the string
    return exp # when the last char is removed, returns the string

expression = str(input("\nIntroduce una expresión: ")) # ask for expression
balanced = isBalanced(expression) # check if it is balanced
# prints the result:
print("\nLa expresión {0} {1}".format(expression,"está balanceada" if balanced else "no está balanceada"))