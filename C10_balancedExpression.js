/*
Reto #10
EXPRESIONES EQUILIBRADAS
Fecha publicación enunciado: 07/03/22
Fecha publicación resolución: 14/03/22
Dificultad: MEDIA

Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a # ( c + d ) ] - 5 }
- Expresión no balanceada: { a # ( c + d ) ] - 5 }

Statement: Create a program that checks whether the parentheses, braces, and square brackets in an expression are balanced.
- Balanced means that these delimiters are opened and closed in order and correctly.
- Parentheses, braces and square brackets are equally important. No one is more important than the other.
- Balanced expression: { [ a # ( c + d ) ] - 5 }
- Unbalanced expression: { { a # ( c + d ) ] - 5 }

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

const openRegex = /[\{\[\(]/g; // regular expression to find open keys
const closeRegex = /[\}\]\)]/g; // regular expresion to find close keys
const keyObj = {"{":"}", "[":"]", "(":")"};

function isBalanced(exp){
	let openKeys = "";
	for(element of exp.split("")){
		if((openRegex.exec(element)) !== null) openKeys += element;
		else if((closeRegex.exec(element)) !== null){
			if(openKeys.length === 0) return false;
			openKeys = removeFromExpression(openKeys, element);
			if(openKeys === false) return false
		}
	}
	if(openKeys.length !== 0) return false;
	return true;
}

function removeFromExpression(exp, c){
	const getKey = (c) => {
		return Object.keys(keyObj).find(key => keyObj[key] === c);
	}
	if(exp.length === 0) return exp; // if exp = empty -> return exp
	if(exp.endsWith(getKey(c))) exp = exp.slice(0, exp.length-1);
	else return false;
	return exp;
}

console.log(isBalanced("{a + b [c] * (2x2)}}}}"));
console.log(isBalanced("{ [ a * ( c + d ) ] - 5 }"));
console.log(isBalanced("{ a * ( c + d ) ] - 5 }"));
console.log(isBalanced("{a^4 + (((ax4)}"));
console.log(isBalanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"));
console.log(isBalanced("{{{{{{(}}}}}}"));
console.log(isBalanced("(a"));
console.log(isBalanced("{ ( ) [ ] }"))