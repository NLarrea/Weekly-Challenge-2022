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
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def checkTicTacToe(board: list):
    xWins = False
    oWins = False
    if len(board) != 3: return "Null" # the board has more than 3 rows
    # checks rows and columns
    for row in range(len(board)):
        if len(board[row]) != 3: return "Null" # a row has more or less than 3 columns
        xRow = 0
        oRow = 0
        xCol = 0
        oCol = 0
        for col in range(len(board[row])):
            # check rows
            if board[row][col] == "X": xRow += 1
            elif board[row][col] == "O": oRow += 1
            else: xRow,oRow = 0,0
            # check columns
            if board[col][row] == "X": xCol += 1
            elif board[col][row] == "O": oCol += 1
            else: xCol,oCol = 0,0
            # to see the counters
            # print("xRow: {0}\noCol: {1}\n".format(xRow,oRow))
            # print("xCol: {0}\noCol: {1}\n".format(xCol,oCol))
            # who wins
            if xRow==3 or oRow==3 or xCol==3 or oCol==3:
                if xRow==3 or xCol==3:
                    xWins = True
                elif oRow==3 or oCol==3:
                    oWins = True
            # check if there is a winner
            if (xWins or oWins) == True: break
    # if there is not a winner yet -> check diagonals
    if (xWins and oWins) != True:
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
            if (xd1 or xd2) == 3: xWins = True
            elif (od1 or od2) == 3: oWins = True
    if (xWins and oWins) == True: return "Null, both are winners" # both wins
    elif xWins == True: return "X wins"
    elif oWins == True: return "O wins"
    else: return "Draw" # there is not winner


# create the arrays
array1 = [["X","O","X"],["O","X","O"],["O","O","X"]] # X should win
array2 = [["","O","X"],["","X","O"],["","O","X"]] # there is no winner -> Draw
array3 = [["O","O","O"],["O","X","X"],["O","X","X"]] # O should win
array4 = [["X","X","X"],["O","X","X"],["X","O","X"]] # X should win
# see who is the winner
print("Result 1: {0}".format(checkTicTacToe(array1))) # X wins
print("Result 2: {0}".format(checkTicTacToe(array2))) # Draw
print("Result 3: {0}".format(checkTicTacToe(array3))) # O wins
print("Result 4: {0}".format(checkTicTacToe(array4))) # X wins