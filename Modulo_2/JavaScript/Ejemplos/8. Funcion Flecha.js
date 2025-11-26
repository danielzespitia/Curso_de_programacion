// Una sintaxis más corta para escribir expresiones de función. Son especialmente útiles para 
// funciones anónimas y tienen un comportamiento diferente con la palabra clave this.

// Mismo ejemplo anterior, pero refactorizado con funciones flecha.

// Función flecha para calcular el área.
// Si la función tiene una sola línea de código que es un 'return',
// se pueden omitir las llaves {} y la palabra 'return'.
const calcularAreaFlecha = (ancho, alto) => ancho * alto;

// Función flecha para calcular el perímetro con cuerpo explícito.
const calcularPerimetroFlecha = (ancho, alto) => {
    const perimetro = 2 * (ancho + alto);
    return perimetro;
};

// Uso de las funciones flecha
const anchoRectangulo = 20;
const altoRectangulo = 8;

const areaResultante = calcularAreaFlecha(anchoRectangulo, altoRectangulo);
console.log(`(Flecha) El área de un rectángulo de ${anchoRectangulo}x${altoRectangulo} es ${areaResultante}.`);

const perimetroResultante = calcularPerimetroFlecha(anchoRectangulo, altoRectangulo);
console.log(`(Flecha) El perímetro del mismo rectángulo es ${perimetroResultante}.`);