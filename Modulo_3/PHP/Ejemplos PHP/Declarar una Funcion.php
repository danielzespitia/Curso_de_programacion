<?php
// Aquí definimos nuestra herramienta, pero todavía no la usamos.
function mostrarSaludo($numero1, $numero2) {
    echo "¡Hola! Bienvenido a mi sitio web desde Maracaibo.\n";
    $suma = 5 + 6;
    echo "La suma de 5 + 6 es: $suma\n";
    $sumaconvariables = $numero1 + $numero2;
    echo "La suma de las variables es: $sumaconvariables\n";
}

// Ahora, usamos la herramienta llamándola por su nombre.
// Esto ejecuta el código que está dentro de la función.
mostrarSaludo(10, 100); 
?>