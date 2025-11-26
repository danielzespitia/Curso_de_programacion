// Ejemplo con 'for': Imprimir la tabla de multiplicar del 7
const numeroTabla = 7;
console.log(`--- Tabla de Multiplicar del ${numeroTabla} ---`);

for (let i = 1; i <= 10; i++) {
    // i es el contador, empieza en 1, se ejecuta mientras sea <= 10, y aumenta en 1 en cada iteración.
    const resultado = numeroTabla * i;
    console.log(`${numeroTabla} x ${i} = ${resultado}`);
}


// Ejemplo con 'while': Simular una descarga de un archivo
let tamanoArchivo = 100; // en MB
let descargado = 0;
const velocidadDescarga = 13; // MB por segundo

console.log("\n--- Simulación de Descarga ---");
while (descargado < tamanoArchivo) {
    // El bucle se ejecuta mientras lo descargado sea menor que el tamaño total.
    console.log(`Descargando... ${descargado} de ${tamanoArchivo} MB.`);
    descargado += velocidadDescarga; // Aumentamos la cantidad descargada

    if (descargado > tamanoArchivo) {
        descargado = tamanoArchivo; // Para no mostrar más de 100MB descargados
    }
}

console.log(`Descargando... ${descargado} de ${tamanoArchivo} MB.`);
console.log("¡Descarga completada!");