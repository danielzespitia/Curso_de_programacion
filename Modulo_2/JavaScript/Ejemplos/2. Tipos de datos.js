// JavaScript tiene varios tipos de datos primitivos y un tipo complejo (objeto).
// Primitivos: String (texto), Number (números), Boolean (verdadero/falso), null 
// (valor nulo intencional), undefined (variable declarada pero sin valor), Symbol 
// (valor único e inmutable) y BigInt (números enteros muy grandes).

// Complejo: Object (colecciones de datos y entidades más complejas).

// Perfil de un producto en un e-commerce

// String: para nombres, descripciones, etc.
const nombreProducto = "Laptop Pro-Gaming XG-3000";
console.log(`Nombre del producto: ${nombreProducto}`);

// Number: para precios, cantidades, IDs numéricos.
let precio = 1499.99;
let stock = 15;

// Boolean: para estados, como disponibilidad o si tiene descuento.
const disponible = true;
const tieneDescuento = false;

// null: se usa para indicar la ausencia intencional de un valor.
// Por ejemplo, si un producto no tiene cupón, lo establecemos como nulo.
let cuponDescuento = null;

// undefined: indica que una variable no ha recibido un valor.
// Si no hemos definido las especificaciones extra, su valor será undefined.
let especificacionesExtra;

// Object: para agrupar toda la información del producto.
const producto = {
    nombre: nombreProducto,
    precioUnitario: precio,
    unidadesEnStock: stock,
    estaDisponible: disponible,
    // Los objetos pueden contener otros objetos (anidación)
    detalles: {
        marca: "TechPro",
        modelo: "XG-3000",
        ram: "32GB DDR5"
    }
};

console.log("Nombre del producto:", producto.nombre);
console.log("Marca:", producto.detalles.marca);
console.log("¿Hay especificaciones extra?", especificacionesExtra); // undefined
console.log("Cupón aplicable:", cuponDescuento); // null