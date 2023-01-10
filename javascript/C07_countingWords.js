/*
Reto #7
CONTANDO PALABRAS
Fecha publicación enunciado: 14/02/22
Fecha publicación resolución: 21/02/22
Dificultad: MEDIA

Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

Statement: Create a program that counts how many times each word is repeated and displays the final count of all of them.
- Punctuation marks are not part of the word.
- A word is the same even if it appears in upper and lower case.
- You cannot use language functions that automatically solve it.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

// create an string or array with all de chars we don't want
const spChars = /[^A-z0-9]/g;

// function to create objects
function objCreator(list){
    let objList = []; // empty list
    for(let i=0; i<list.length; i++){ // for every word in the list
        let counter = 0; // counter starts from 0
        for(let j=i; j<list.length; j++){ // for every word in the list starting in index = i
            // if the word doesn't exist in the objList
            if(list[j]===list[i] && objList.includes(objList.find(o => o.name === list[j]))===false){
                counter++; // counter = 1
                objList.push({name: list[j], counter}); // adds a new object to the objList
            }
            // if the word already exists in the objList
            else if(list[j]===list[i] && objList.includes(objList.find(o => o.name === list[j]))===true){
                // if it appears more than one time, counter of thar word = counter++
                if(objList[i] !== undefined) objList[i].counter++;
            }
        }
    }
    return objList; // returns the objList
}

// to split the original string
function countWords(str){
    /* to create a list that contains all the words, in lowercase, and without symbols.
    The filter is used to delete empty strings from the list, because replace and split
    add empty strings to the list */
    const wordList = str.toLowerCase().replace(spChars," ").split(" ").filter(word => word);
    const objList = objCreator(wordList); // to create an object list
    // to print the result
    for(element of objList){
        console.log(`The word "${element.name.toUpperCase()}" appears`, (element.counter>1 ? `${element.counter} times.` : `${element.counter} time.`));
    }
}

countWords("Hi, my name is naia. My full name is Naia Larrea (NLarrea). How is your day going?");