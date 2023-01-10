/* Reto #49
EL DETECTOR DE HANDLES
Fecha publicación enunciado: 05/11/22
Fecha publicación resolución: 12/12/22
Dificultad: FÁCIL

Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente
Expresiones Regulares.
Debes crear una expresión regular para cada caso:
- Handle usuario: Los que comienzan por "@"
- Handle hashtag: Los que comienzan por "#"
- Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function handleDetector(text){
    // regex to find elements
    const user = /^@[A-Za-z0-9\_\.\-]*/gm;
    const hashtag = /^#[A-Za-z0-9]*/gm;
    const web1 = /(?:^https:\/\/)/gm;
    const web2 = /(?:^http:\/\/)/gm;
    const web3 = /(?:^www\.)/gm;

    // new list to save the matches
    let matched = [];
    
    text.split(", ").forEach(word => {
        if(word.match(user) || word.match(hashtag) || word.match(web1) || word.match(web2) || word.match(web3)) matched.push(word);
    })
    return matched;
}

// SOME EXAMPLES
const userList = "@NLarrea, @n.loust, wef@user, @user123, 123user@";
const hashtagList = "#octoverse, #javascript, this#not, not#hashtag, lastTry#";
const webList = "https://github.com, https:/github.com, http://google.es, www.codedex.io, www.toptal.com";
const popurri = "@nloust_, n@larrea, www.github.com, ww.github.com, github.www.com, #awesome, https;//nothing"

console.log(handleDetector(userList)); // [ '@NLarrea', '@n.loust', '@user123' ]
console.log(handleDetector(hashtagList)); // [ '#octoverse', 'javascript' ]
console.log(handleDetector(webList)); // [ 'https://github.com', 'http://google.es', 'www.codedex.io', 'www. toptal.com' ]
console.log(handleDetector(popurri)); // [ '@nloust_', 'www.github.com', '#awesome' ]