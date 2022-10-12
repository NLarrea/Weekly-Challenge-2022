# Reto #25
# PIEDRA, PAPEL, TIJERA
# Fecha publicación enunciado: 20/06/22
# Fecha publicación resolución: 27/06/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def rockScissorsPaper(game):
    p1 = 0
    p2 = 0
    for moves in game:
        if len(moves) == 1: # there is only one move from each player
            if game[0] == game[1]: return "Tie" # there is no winner
            elif (game[0]=="R" and game[1]=="S") or (game[0]=="S" and game[1]=="P") or (game[0]=="P" and game[1]=="R"):
                return "Player 1 wins"
            else: return "Player 2 wins"
        else:
            for move in moves:
                if move == moves[1]: continue # it would be a tie
                elif (move=="R" and moves[1]=="S") or (move=="S" and moves[1]=="P") or (move=="P" and moves[1]=="R"):
                    p1 += 1 # player1 wins this move
                else: p2 += 1 # player2 wins this move
    if p1 == p2: return "Tie"
    elif p1 > p2: return "Player 1 wins"
    else: return "Player 2 wins"

print(rockScissorsPaper(list("R","R"))) # Tie
print(rockScissorsPaper(("R","S"))) # Player 1 wins
print(rockScissorsPaper(("P","S"))) # Player 2 wins
print(rockScissorsPaper((("R", "R"),("S", "S"),("P", "P")))) # Tie
print(rockScissorsPaper((("R", "S"),("S", "P"),("S", "R")))) # Player 1 wins
print(rockScissorsPaper((("R", "P"),("S", "R"),("P", "S")))) # Player 2 wins