// Ejemplo práctico de declaración de variables para una tienda online

// Usamos 'let' para el nombre de usuario porque podría querer cambiarlo más adelante.
let nombreUsuario = "AlexDev";
console.log("Nombre de usuario inicial:", nombreUsuario);

// El usuario decide cambiar su nombre.
nombreUsuario = "AlexDeveloper99";
console.log("Nombre de usuario actualizado:", nombreUsuario);

// Usamos 'const' para la fecha de registro, ya que es un dato que nunca cambiará.
const fechaDeRegistro = "2024-01-10";
console.log("Registrado el:", fechaDeRegistro);

// Intentar reasignar una constante arrojará un error.
// Descomenta la siguiente línea para ver el error en la consola.
// fechaDeRegistro = "2024-02-15"; // TypeError: Assignment to constant variable.

// Usamos 'const' para un objeto de configuración.
// Aunque el objeto en sí no puede ser reasignado, sus propiedades internas sí pueden cambiar.
const configuracionCuenta = {
    tema: "oscuro",
    notificaciones: true
};

// Modificamos una propiedad del objeto constante. Esto es válido.
configuracionCuenta.tema = "claro";
console.log("Tema actualizado:", configuracionCuenta.tema);