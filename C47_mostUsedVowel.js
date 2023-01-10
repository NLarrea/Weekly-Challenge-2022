/*
Reto #47
vowel MÁS COMÚN
Fecha publicación enunciado: 21/11/22
Fecha publicación resolución: 28/11/22
Dificultad: FÁCIL

Enunciado: Crea un función que reciba un texto y retorne la vowel que más veces se repita.
Si no hay voweles podrá devolver vacío.

Statement: Create a function that receives a text and returns the most repeated vowel.
If there are no vowels it may return empty.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function mostUsedVowel(text){
    let vowelCount = {} // empty object
    // loop through the text in lowercase and normalize the accents
    text.toLowerCase().normalize('NFD').split("").forEach(char => {
        // check if the char is a vowel
        if("aeiou".includes(char)){
            // if the vowel is in the object, increase its counter, else add it to the object
            (char in vowelCount)? vowelCount[`${char}`]++ : vowelCount[`${char}`] = 1;
        }
    })
    let mostRepeated = []; // empty list to store the most repeated vowels
    let maxRepeated = 0; // variable to store the number of max repeated vowels
    // loop through the object
    for(vowel in vowelCount){
        let count = vowelCount[vowel]; // store the value of the counter of each vowel
        if(count >= maxRepeated){
            // if the counter is greater than the max repeated, empty the list and add the vowel
            if(count > maxRepeated) mostRepeated = [];
            mostRepeated.push(vowel); // add the vowel to the list
            maxRepeated = count; // update the max repeated
        }
    }
    return (mostRepeated.length !== 0)? mostRepeated : "There are no vowels";
}

console.log(mostUsedVowel("Hello")); // ['e', 'o']
console.log(mostUsedVowel("ghdjf")); // "There are no vowels"
console.log(mostUsedVowel("Hello World")); // ['o']
console.log(mostUsedVowel("This is a good day")); // ['i',  'a', 'o']
console.log(mostUsedVowel("Hola, ¿qué tal estás hoy?")); // ['a']