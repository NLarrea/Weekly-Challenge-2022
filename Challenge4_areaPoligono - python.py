# Reto #4
# ÁREA DE UN POLÍGONO
# Fecha publicación enunciado: 24/01/22
# Fecha publicación resolución: 31/01/22
# Dificultad: FÁCIL
#
# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

# FUNCIÓN: recibe un string con el nombre del poligono y sus dimensiones:
def area(poligono,b,h):
    if poligono.lower() == ("triangulo" or "triángulo"):
        area = (b*h)/2
    elif poligono.lower() == "cuadrado":
        area = b*h
    elif poligono.lower() == ("rectangulo" or "rectángulo"):
        area = b*h
    else:
        print("Lo siento, poligono no reconocido!\n")
        area = int(-1)
    return area

# Bucle para la introducción de datos (pequeña mejora):
while True:
    try:
        poligono = input("Introduce el nombre del poligono:\n")
        assert(poligono.isalpha())
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        break
    except(AssertionError):
        print("ERROR: debes introducir un nombre!\n")
    except(TypeError,ValueError):
        print("ERROR: debes introducir un numero!\n")
# Llamada a la función:
respuesta = area(poligono,base,altura)
# Si el nombre del polígono es válido, imprime el resultado:
if respuesta != -1:
    print("Area del {0}: {1}".format(poligono,respuesta))
