<?php

$nombre = "Carlos Rivas";

// PHP ve el número sin decimales y sabe que $edad es un Integer.
$edad = 28;

// PHP ve el número con decimales y sabe que $altura es un Float.
$altura = 1.75;

// PHP ve la palabra 'true' y sabe que $esDesarrollador es un Boolean.
$esDesarrollador =  true;

$nombre_usuario = "admin";  // Usa letras y guion bajo
$_variableOculta = "secreto"; // Comienza con guion bajo
$valor1 = 100;              // Contiene números (pero no al principio)

echo "Ejemplos de nombres de variables VÁLIDOS:\n";
echo "nombre_usuario: " . $nombre_usuario . "\n";
echo "_variableOculta: " . $_variableOculta . "\n";
echo "valor1: " . $valor1 . "\n";
echo "\n----------------------------------------\n\n";

// El uso ToLower y ToUpper
$texto = "Hola Mundo";
echo "Texto original: " . $texto . "\n";
echo "Texto en minúsculas: " . strtolower($texto) . "\n";
echo "Texto en mayúsculas: " . strtoupper($texto) . "\n";

?>