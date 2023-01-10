# Reto #45
# CONTENEDOR DE AGUA
# Fecha publicación enunciado: 07/10/22
# Fecha publicación resolución: 14/11/22
# Dificultad: MEDIA
# 
# Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
# de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
# 
# - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
# 
#        ⏹
#        ⏹
#   ⏹💧💧⏹
#   ⏹💧⏹⏹💧⏹
#   ⏹💧⏹⏹💧⏹
#   ⏹💧⏹⏹⏹⏹
# 
# Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
# Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
# 
# Statement: Given an array of positive integers, where each represents units of stacked blocks, we must calculate how many units of water will be trapped between them.
# of stacked blocks, we must calculate how many units of water will be trapped between them.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def calculateWaterUnits(blockList):
    # if at least one of the blocks number is negative -> return message
    if any(num<0 for num in blockList): return "All the numbers must be positive!"
    # variables
    waterUnits = 0 # this will be the result
    wall = 0
    nextWall = 0
    index = 0 # to use in the loop
    for block in blockList:
        if index != len(blockList)-1 and (index == 0 or nextWall == block):
            # calculate walls
            wall = block if index == 0 else nextWall
            nextWall = 0
            nextBlockIndex = index + 1
            while nextBlockIndex < len(blockList):
                if blockList[nextBlockIndex] >= nextWall: nextWall = blockList[nextBlockIndex]
                nextBlockIndex += 1
        else:
            # calculate water units
            referenceWall = wall if nextWall > wall else nextWall
            currentBlocks = referenceWall - block
            waterUnits += currentBlocks if currentBlocks >= 0 else 0
        index += 1
    return waterUnits # return the result

print(calculateWaterUnits([4, 0, 3, 6])) # 5
print(calculateWaterUnits([4, 0, 3, 6, 1, 3])) # 7
print(calculateWaterUnits([5, 4, 3, 2, 1, 0])) # 0
print(calculateWaterUnits([0, 1, 2, 3, 4, 5])) # 0
print(calculateWaterUnits([4, 0, 3, 6, 1, 3, 0, 1, 6])) # 24