 # Reto #17
 # LA CARRERA DE OBSTÁCULOS
 # Fecha publicación enunciado: 25/04/22
 # Fecha publicación resolución: 02/05/22
 # Dificultad: MEDIA
 #
 # Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 # carrera de obstáculos.
 # - La función recibirá dos parámetros:
 #      - Un array que sólo puede contener String con las palabras "run" o "jump"
 #      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 # - La función imprimirá cómo ha finalizado la carrera:
 #      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 #        variará el símbolo de esa parte de la pista.
 #      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 #      - Si hace "run" en "|" (valla), se variará la pista por "/".
 # - La función retornará un Boolean que indique si ha superado la carrera.
 # Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def checkResult(array:list,track:str):
    # checks whitch one has bigger length:
    totalActions = len(array) if len(array)>len(track) else len(track)
    minActions = len(array) if len(array)<len(track) else len(track)
    athleteTrack = "" # empty string to save the results
    for i in range(0,totalActions):
        if i >= minActions: athleteTrack += "?" # if index is bigger than the minActions, fill with "?"
        else:
            if array[i]=="RUN" and track[i]=="_": athleteTrack += "_" # it's correct
            elif array[i]=="JUMP" and track[i]=="|": athleteTrack += "|" # it's correct
            elif array[i]=="RUN" and track[i]=="|": athleteTrack += "/" # not correct
            elif array[i]=="JUMP" and track[i]=="_": athleteTrack += "x" # not correct
            else: athleteTrack += "?" # when there is another type of input (char) in the string
        i += 1 # for the loop
    return athleteTrack # returns the result
        
print("\nRace 1 result:",checkResult(["RUN", "JUMP", "RUN", "JUMP", "RUN"], "_|_|_")) # race 1
print("Race 2 result:",checkResult(["RUN", "RUN", "RUN", "JUMP", "RUN"], "_|_|_")) # race 2
print("Race 3 result:",checkResult(["RUN", "RUN", "JUMP", "JUMP", "RUN"], "_|_|_")) # race 3
print("Race 4 result:",checkResult(["RUN", "RUN", "JUMP", "JUMP", "RUN"], "_|_|_|_")) # race 4
print("Race 5 result:",checkResult(["RUN", "JUMP", "RUN", "JUMP"], "_|_|_")) # race 5
print("Race 6 result:",checkResult(["RUN", "JUMP", "RUN", "JUMP", "RUN", "JUMP", "RUN"], "_|_|_")) # race 6
print("Race 7 result:",checkResult(["JUMP", "JUMP", "JUMP", "JUMP", "JUMP"], "|||||")) # race 7
print("Race 8 result:",checkResult(["JUMP", "JUMP", "JUMP", "JUMP", "JUMP"], "||?||")) # race 8