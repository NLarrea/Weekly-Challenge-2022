# Reto #18
# TRES EN RAYA
# Fecha publicación enunciado: 02/05/22
# Fecha publicación resolución: 09/05/22
# Dificultad: DIFÍCIL
#
# Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def checkTicTacToe(board: list):
    if len(board) != 3: return "Null" # the board has more than 3 rows
    # checks rows and columns
    for row in range(len(board)):
        if len(board[row]) != 3: return "Null" # a row has more or less than 3 columns
        xRow = 0
        oRow = 0
        xCol = 0
        oCol = 0
        for col in range(len(board[row])):
            # for the rows
            if board[row][col] == "X": xRow += 1
            elif board[row][col] == "O": oRow += 1
            else: xRow,oRow = 0,0
            # for columns
            if board[col][row] == "X": xCol += 1
            elif board[col][row] == "O": oCol += 1
            else: xCol,oCol = 0,0
            # to see the counters
            # print("xRow: {0}\noCol: {1}\n".format(xRow,oRow))
            # print("xCol: {0}\noCol: {1}\n".format(xCol,oCol))
            # who wins
            if xRow==3 or oRow==3 or xCol==3 or oCol==3:
                if xRow==3 or xCol==3:
                    return "X wins"
                elif oRow==3 or oCol==3:
                    return "O wins"
    # now we know the dimensions of the board are correct -> same rows and columns
    # checks diagonals
    xd1,xd2,od1,od2 = 0,0,0,0
    for pos in range(len(board)):
        if board[pos][pos] == "X": xd1 += 1
        elif board[pos][pos] == "O": od1 += 1
        if board[pos][3-pos-1] == "X": xd2 += 1
        elif board[pos][3-pos-1] == "O": od2 += 1
        # to see counters
        # print("xd1: {0}\txd2: {1}".format(xd1,xd2))
        # print("od1: {0}\tod2: {1}".format(od1,od2))
        # who wins
        if (xd1 or xd2) == 3: return "X wins"
        elif (od1 or od2) == 3: return "O wins"
    for row in range(len(board)):
        for col in range(3):
            if board[col][row] == "": return "Null"
    return "Draw"


# create the arrays
array1 = [["X","O","X"],["O","X","O"],["O","O","X"]] # X should win
array2 = [["","O","X"],["","X","O"],["","O","X"]] # there are white spaces -> should be a null
array3 = [["O","O","O"],["O","X","X"],["O","X","X"]] # O should win
array4 = [["X","X","X"],["O","X","X"],["X","O","X"]] # X should win
# see who is the winner
print("Result 1: {0}".format(checkTicTacToe(array1))) # X wins
print("Result 2: {0}".format(checkTicTacToe(array2))) # Null
print("Result 3: {0}".format(checkTicTacToe(array3))) # O wins
print("Result 4: {0}".format(checkTicTacToe(array4))) # X wins