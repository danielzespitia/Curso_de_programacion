// Los operadores nos permiten realizar operaciones con variables y valores.
// Aritméticos: +, -, *, /, % (módulo), ** (exponenciación).
// De Asignación: =, +=, -=, *=, /=.
// De Comparación: == (igual), === (estrictamente igual, compara valor y tipo), !=, !==, >, <, >=, <=.
// Lógicos: && (y), || (o), ! (no).
// Bit a bit: &, |, ^, ~, <<, >>.
 
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

// Ejemplo de uso de operadores bit a bit
let bitA = 5; // 0101 en binario
let bitB = 3; // 0011 en binario
console.log(`bitA & bitB: ${bitA & bitB}`); // AND
console.log(`bitA | bitB: ${bitA | bitB}`); // OR
console.log(`bitA ^ bitB: ${bitA ^ bitB}`); // XOR
console.log(`~bitA: ${~bitA}`); // NOT
console.log(`bitA << 1: ${bitA << 1}`); // Desplazamiento a la izquierda
console.log(`bitA >> 1: ${bitA >> 1}`); // Desplazamiento a la derecha

// Simulación del cálculo del total de un carrito de compras

const precioProductoA = 25.50; // Dólares
const cantidadProductoA = 2;
const precioProductoB = 10.00;
const cantidadProductoB = 5;

// Operadores Aritméticos: calculamos el subtotal
const subtotal = (precioProductoA * cantidadProductoA) + (precioProductoB * cantidadProductoB);
console.log("Subtotal:", subtotal);

// Operador de Asignación: calculamos el impuesto (IVA 16%)
const TASA_IVA = 0.16;
let total = subtotal;
total += subtotal * TASA_IVA; // Equivalente a: total = total + (subtotal * TASA_IVA)
console.log("Total con IVA:", total.toFixed(2)); // .toFixed(2) para redondear a 2 decimales

// Operadores Lógicos y de Comparación: aplicamos un descuento
const esClienteFrecuente = true;
const totalCompraMinimaParaDescuento = 100;

// Si el total es mayor a 100 Y es un cliente frecuente, tiene envío gratis.
if (total > totalCompraMinimaParaDescuento && esClienteFrecuente) {
    console.log("¡Felicidades! Calificas para envío gratis.");
} else {
    console.log("Costo de envío se aplicará en el checkout.");
}

// El operador ternario es una forma corta de un if/else
const mensajeStock = cantidadProductoA > 0 ? "Producto A está en stock" : "Producto A agotado";
console.log(mensajeStock);

// Operadores Bit a Bit: no son comunes en aplicaciones web, pero aquí un ejemplo
const a1 = 5; // 0101 en binario
const b1 = 3; // 0011 en binario
const resultadoAnd = a & b; // 0001 en binario, que es 1 en decimal
console.log("Resultado AND bit a bit:", resultadoAnd); // 1

// Operador de Exponenciación: calcular el cuadrado de un número
const numero = 4;
const cuadrado = numero ** 2; // 4 al cuadrado es 16
console.log("Cuadrado de", numero, "es:", cuadrado); // 16


