 # Reto #0
 # EL FAMOSO "FIZZ BUZZ"
 # Fecha publicacion enunciado: 27/12/21
 # Fecha publicacion resolucion: 03/01/22
 # Dificultad: FACIL
 # Enunciado: Escribe un programa que muestre por consola (con un print) los n�meros de 1 a 100 (ambos incluidos y con un salto de l�nea entre cada impresi�n), sustituyendo los siguientes:
 # - Multiplos de 3 por la palabra "fizz".
 # - Multiplos de 5 por la palabra "buzz".
 # - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 #
 # Informacion adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "??reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solucion aportada.
 # - Revisare el ejercicio en directo desde Twitch el lunes siguiente al de su publicacion.
 # - Subire una posible solucion al ejercicio el lunes siguiente al de su publicacion.

for number in range(1,101): # range(i,j) -> cuenta desde i hasta j-1
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)