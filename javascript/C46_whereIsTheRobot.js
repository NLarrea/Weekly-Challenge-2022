/*
Reto #46
¿DÓNDE ESTÁ EL ROBOT?
Fecha publicación enunciado: 14/11/22
Fecha publicación resolución: 21/11/22
Dificultad: MEDIA

Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cudrícula
representada por los ejes "x" e "y".
- El robot comienza en la coordenada (0, 0).
- Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos)
  que indican la secuencia de pasos a dar.
 - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene,
   y finalmente 2. El resultado en este caso sería (x: -5, y: 12)
- Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
- Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte
  positiva del eje "y".
- El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira
  90 grados en el sentido contrario a las agujas del reloj.

Statement: Calculate where a robot will be (its final coordinates) located on a cubicle represented by the x and y axes.
represented by the "x" and "y" axes.
- The robot starts at coordinate (0, 0).
- To instruct it to move, we send it an array consisting of integers (positive or negative)
  that indicate the sequence of steps to take.
 - For example: [10, 5, -2] indicates that first it moves 10 steps, stops, then 5, stops, then 2,
   and finally 2. The result in this case would be (x: -5, y: 12).
- If the number of steps is negative, it would move in the opposite direction to the one it is looking at.
- The first steps are made on the y-axis. We interpret that it is looking towards the positive part of the y-axis.
  positive side of the y-axis.
- The robot has a flaw in its programming: every time it finishes a sequence of steps it rotates
  90 degrees counterclockwise.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

// class to say which direction the robot is facing
class Direction{
    constructor(){
        this.position = "posY"; // initial direction = "posY"
    }
    turn(){
        // turn the robot 90 degrees
        if(this.position === "posY") this.position = "negX";
        else if(this.position === "negX") this.position = "negY";
        else if(this.position === "negY") this.position = "posX";
        else if(this.position === "posX") this.position = "posY";
    }
}

function whereIsTheRobot(steps){
    // initial position
    let x = 0;
    let y = 0;
    let stepDirection = new Direction(); // initial direction = "posY"
    // loop through the steps
    steps.forEach(step => {
        // add the step to the corresponding axis
        if(stepDirection.position === "posY") y += step;
        else if(stepDirection.position === "posX") x += step;
        else if(stepDirection.position === "negY") y -= step;
        else if(stepDirection.position === "negX") x -= step;
        stepDirection.turn(); // turn the robot 90 degrees
    })
    // return the final position
    return `x: ${x}, y: ${y}`;
}

console.log(whereIsTheRobot([10, 5, -2])); // x: -5, y: 12
console.log(whereIsTheRobot([0, 0, 0])); // x: 0, y: 0
console.log(whereIsTheRobot([])); // x: 0, y: 0
console.log(whereIsTheRobot([-10, -5, 2])); // x: 5, y: -12
console.log(whereIsTheRobot([-10, -5, 2, 4, -8])); // x: 9, y: -20