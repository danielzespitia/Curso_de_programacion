// Selector de acción basado en el rol de un usuario
const rolUsuario = "EDITOR"; // Puede ser "ADMIN", "EDITOR", "VIEWER"

console.log(`El usuario tiene el rol: ${rolUsuario}.`);

switch (rolUsuario) {
    case "ADMIN":
        console.log("Acceso total: puede crear, editar y eliminar contenido.");
        break; // 'break' es crucial para no seguir ejecutando los siguientes casos.
    case "EDITOR":
        console.log("Acceso limitado: puede crear y editar su propio contenido.");
        break;
    case "VIEWER":
        console.log("Acceso de solo lectura: puede ver el contenido.");
        break;
    default: // Se ejecuta si ninguno de los casos anteriores coincide.
        console.log("Rol no reconocido. Acceso denegado.");
        break;
}
