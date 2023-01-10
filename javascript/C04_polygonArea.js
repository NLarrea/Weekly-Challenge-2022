/*
Reto #4
ÁREA DE UN POLÍGONO
Fecha publicación enunciado: 24/01/22
Fecha publicación resolución: 31/01/22
Dificultad: FÁCIL

Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.

Statement: Create ONE FUNCTION (it is important that it is only one) that is able to calculate and return the area of a polygon.
- The function will receive by parameter only ONE polygon at a time.
- The polygons supported will be Triangle, Square and Rectangle.
- Print the calculation of the area of one polygon of each type.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

class Polygon { // parent class
    // protected atributes
    _base;
    _height;
    // parent constructor
    constructor(b, h){
        this._base = b;
        this._height = h;
    }
    // method
    area(){
        return this._base * this._height;
    }
}

class Triangle extends Polygon { // child class
    constructor(b, h) {
        super(b,h); // to use the parent's constructor
    }
    area(){
        return (this._base * this._height) / 2; // the area of a triangle
    }
}

class Square extends Polygon { // child class
    constructor(b){
        super(b,b); // to use the parent's constructor
    }
    area(){
        return super.area(); // to use the parent's area() method
    }
}

class Rectangle extends Polygon { // child class
    constructor(b, h){
        super(b,h); // to use the parent's constructor
    }
    area(){
        return super.area(); // to use the parent's area() method
    }
}

// ONE FUNCTION that receives one polygon and returns its area
function printArea(polygon){
    return polygon.area();
}

// calculate the area of the following polygons:
console.log(printArea(new Triangle(4,5))); // 10
console.log(printArea(new Square(5))); // 25
console.log(printArea(new Rectangle(25,4))); // 100