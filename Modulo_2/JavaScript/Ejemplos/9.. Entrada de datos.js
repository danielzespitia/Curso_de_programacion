// Importar el módulo readline
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

// Crear una interfaz para leer y escribir
const rl = readline.createInterface({ input, output });

// Solicitar texto (nombre)
rl.question('Por favor, ingresa tu nombre: ', (nombre) => {
  console.log(`Hola, ${nombre}!`);

  // Solicitar un número (edad) dentro del callback de la primera pregunta
  rl.question('Ingresa tu edad: ', (edadString) => {
    const edadNumero = parseInt(edadString);

    if (!isNaN(edadNumero)) {
      console.log(`Tienes ${edadNumero} años.`);
      console.log(`El próximo año tendrás ${edadNumero + 1} años.`);
    } else {
      console.log('La edad ingresada no es un número válido.');
    }

    // Cerrar la interfaz readline, ya que hemos terminado de hacer preguntas
    rl.close();
  });
});

// El evento 'close' se dispara cuando la interfaz se cierra.
rl.on('close', () => {
  console.log('¡Adiós!');
  process.exit(0); // Termina el proceso de Node.js
});