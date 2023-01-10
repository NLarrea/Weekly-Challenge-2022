/*
Reto #50
LA ENCRIPTACIÓN DE KARACA
Fecha publicación enunciado: 12/11/22
Fecha publicación resolución: 19/12/22
Dificultad: FÁCIL

Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el
algoritmo de encriptación de Karaca (debes buscar información sobre él).

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function karaca(text, isKaraca){
    let result = "";

    text.toLowerCase().split(" ").forEach(word => {
        if(isKaraca){
            result += word.replace("aca", "").split("").reverse().join("")
                .replaceAll("0", "a")
                .replaceAll("1", "e")
                .replaceAll("2", "i")
                .replaceAll("3", "o")
                .replaceAll("4", "u")
            result += " ";
        } else {
            result += word.split("").reverse().join("")
                .replaceAll("a", "0")
                .replaceAll("e", "1")
                .replaceAll("i", "2")
                .replaceAll("o", "3")
                .replaceAll("u", "4")
            result += "aca ";
        }
    });

    return result;
}

console.log(karaca("placa", false)); // 0c0lpaca
console.log(karaca("0c0lpaca", true)); // placa

console.log(karaca("Este es el penúltimo reto de programación del año", false)); // 1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca
console.log(karaca("1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca", true)) // este es el penúltimo reto de programación del año