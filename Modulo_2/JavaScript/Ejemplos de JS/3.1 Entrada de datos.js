let dato = prompt("Por favor, ingresa un dato:");
console.log("Has ingresado:", dato);
console.log(`Tipo de dato ingresado: ${dato}`);

// Convertir el dato ingresado a un número
let numero = Number(dato);
if (!isNaN(numero)) {
    console.log("El dato convertido a número es:", numero);
}

// Verificar si el dato es un número
if (isNaN(numero)) {
    console.log("El dato ingresado no es un número válido.");
}

// Convertir el dato ingresado a un booleano
let booleano = dato.toLowerCase() === "true";
console.log("El dato convertido a booleano es:", booleano); 

// Ejemplo de uso de prompt para obtener un número
let edad = prompt("¿Cuál es tu edad?");
if (edad !== null) {
    edad = Number(edad);
    if (!isNaN(edad)) {
        console.log("Tu edad es:", edad);
    } else {
        console.log("Por favor, ingresa un número válido para la edad.");
    }
}