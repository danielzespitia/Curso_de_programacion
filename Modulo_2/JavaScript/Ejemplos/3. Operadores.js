// Los operadores nos permiten realizar operaciones con variables y valores.
// Aritméticos: +, -, *, /, % (módulo), ** (exponenciación).
// De Asignación: =, +=, -=, *=, /=.
// De Comparación: == (igual), === (estrictamente igual, compara valor y tipo), !=, !==, >, <, >=, <=.
// Lógicos: && (y), || (o), ! (no).
 
// Ejemplo de uso de operadores aritméticos
let a = 10;
let b = 5;
let suma = a + b; // Suma
let resta = a - b; // Resta
let multiplicacion = a * b; // Multiplicación
let division = a / b; // División
let modulo = a % b; // Módulo (resto de la división)
let exponenciacion = a ** b; // Exponenciación
console.log(`Suma: ${suma}`);
console.log(`Resta: ${resta}`);
console.log(`Multiplicación: ${multiplicacion}`);
console.log(`División: ${division}`);
console.log(`Módulo: ${modulo}`);   
console.log(`Exponenciación: ${exponenciacion}`);

// Ejemplo de uso de operadores de asignación
let x = 20;
x += 5; // Equivalente a x = x + 5
console.log(`Nuevo valor de x después de +=: ${x}`);
x -= 3; // Equivalente a x = x - 3
console.log(`Nuevo valor de x después de -=: ${x}`);
x *= 2; // Equivalente a x = x * 2
console.log(`Nuevo valor de x después de *=: ${x}`);
x /= 4; // Equivalente a x = x / 4
console.log(`Nuevo valor de x después de /=: ${x}`);
x %= 3; // Equivalente a x = x % 3
console.log(`Nuevo valor de x después de %=: ${x}`);

// Ejemplo de uso de operadores de comparación
let y = 10;
let z = 20;
console.log(`y es igual a z? ${y == z}`); // Igualdad
console.log(`y es estrictamente igual a z? ${y === z}`); // Igualdad estricta
console.log(`y es diferente de z? ${y != z}`); // Desigualdad
console.log(`y es estrictamente diferente de z? ${y !== z}`); // Desigualdad estricta
console.log(`y es mayor que z? ${y > z}`); // Mayor que
console.log(`y es menor que z? ${y < z}`); // Menor que
console.log(`y es mayor o igual que z? ${y >= z}`); // Mayor o igual que
console.log(`y es menor o igual que z? ${y <= z}`); // Menor o igual que

// Ejemplo de uso de operadores lógicos
let aVerdadero = true;
let bFalso = false;
console.log(`aVerdadero && bFalso: ${aVerdadero && bFalso}`); // AND lógico
console.log(`aVerdadero || bFalso: ${aVerdadero || bFalso}`); // OR lógico
console.log(`!aVerdadero: ${!aVerdadero}`); // NOT lógico
