/*
Reto #9
CÓDIGO MORSE
Fecha publicación enunciado: 02/03/22
Fecha publicación resolución: 07/03/22
Dificultad: MEDIA

Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

Statement: Create a program that is able to transform natural text to Morse code and vice versa.
- It should automatically detect what type it is and perform the conversion.
- Morse supports dash "-", period ".", a space " " between letters or symbols and two spaces between words " ".
- The Morse alphabet supported will be the one shown at https://es.wikipedia.org/wiki/Código_morse.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

// create a dictionary that contains all the Morse Code characters
const morseDic = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-",
    "L":".-..", "M":"--", "N":"-.", "Ñ":"--.--", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-",
    "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-",
    "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", ".":".-.-.-", ",":"--..--", "?":"..--..", '"':".-..-.",
    "/":"-..-."
};

/*
function getKeyByValue(object, value){
    return Object.keys(object).find(key => object[key] === value);
}
console.log(getKeyByValue(morseDic, ".-")); // A
*/

// a function to check if the string is Morse or Natural
function checkIfMorse(str){
    if(str === "") return "String is empty";
    for(char of str){
        if(char!==" " && char!=="-" && char!==".") return false;
    }
    return true;
}

function toNatural(str){
    const mList = str.split(" "); // to get a list of Morse characters
    let toNatural = ""; // empty string
    mList.forEach(element => {
        console.log(element)
        if(element !== "") toNatural += Object.keys(morseDic).find(key => morseDic[key] === element);
        else if(element === "") toNatural += " ";
    });
    return toNatural;
}

function toMorse(str){
    let toMorse = ""; // empty string
    for(element of str){
        // if element is not a space -> take its value from morseDic and add a space at the end
        if(element!==" ") toMorse += morseDic[element.toUpperCase()] + " ";
        // if element is a space -> add it
        else toMorse += element;
    }
    return toMorse;
}

const p1 = "Hi, my name is Naia"; // should return ".... .. --..--  -- -.--  -. .- -- .  .. ...  -. .- .. .-"
const p2 = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."; // should return "HELLO WORLD"

// FIRST EXAMPLE -> from natural to Morse
let isMorse = checkIfMorse(p1); // check if it's Morse or not
// transform to the other one
if(isMorse === true) var result = toNatural(p1);
else result = toMorse(p1);
// print the result
console.log(result); // .... .. --..--  -- -.--  -. .- -- .  .. ...  -. .- .. .-

// SECOND EXAMPLE -> from Morse to natural
isMorse = checkIfMorse(p2); // check if it's Morse Code or not
// transform to the other one
if(isMorse === true) result = toNatural(p2);
else result = toMorse(p2);
// print the result
console.log(result); // HELLO WORLD