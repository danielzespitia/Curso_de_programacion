// Las funciones son bloques de código reutilizables.

// Declaración: Se definen con la palabra clave function y son "elevadas" (hoisted), lo que significa que pueden ser llamadas antes de ser declaradas.

// Expresión: Se asignan a una variable. No son elevadas, por lo que solo pueden ser llamadas después de su definición.

// Escenario: Calcular el área y el perímetro de un rectángulo.

// 1. Declaración de Función (Function Declaration)
// Esta función es "elevada" (hoisted), por lo que podríamos llamarla antes de esta línea.
function calcularArea(ancho, alto) {
    const area = ancho * alto;
    return area; // 'return' devuelve un valor que puede ser usado fuera de la función.
}

// 2. Expresión de Función (Function Expression)
// Esta función está asignada a una constante. No es hoisted.
const calcularPerimetro = function(ancho, alto) {
    const perimetro = 2 * (ancho + alto);
    return perimetro;
};

// Uso de las funciones
const anchoRectangulo = 10;
const altoRectangulo = 5;

const areaResultante = calcularArea(anchoRectangulo, altoRectangulo);
console.log(`El área de un rectángulo de ${anchoRectangulo}x${altoRectangulo} es ${areaResultante}.`);

const perimetroResultante = calcularPerimetro(anchoRectangulo, altoRectangulo);
console.log(`El perímetro del mismo rectángulo es ${perimetroResultante}.`);