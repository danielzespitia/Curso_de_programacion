<?php

// ## 1. Las variables comienzan con el signo de dólar ($) ##
// ## 2. PHP infiere el tipo de dato automáticamente ##
// ## 3. Reglas para nombrar variables ##
// PHP ve las comillas y sabe que $nombre es un String.

$nombre = "Carlos Rivas";

// PHP ve el número sin decimales y sabe que $edad es un Integer.
$edad = 28;

// PHP ve el número con decimales y sabe que $altura es un Float.
$altura = 1.75;

// PHP ve la palabra 'true' y sabe que $esDesarrollador es un Boolean.
$esDesarrollador =  true;


// Imprimimos los valores y sus tipos para verificar la inferencia de PHP.
// Usamos var_dump() que muestra el tipo de dato y el valor.
echo "Ejemplo de Inferencia de Tipos:\n";

echo "\n----------------------------------------\n\n";


// ## 3. Reglas para nombrar variables ##

// Nombres de variables VÁLIDOS:
$nombre_usuario = "admin";  // Usa letras y guion bajo
$_variableOculta = "secreto"; // Comienza con guion bajo
$valor1 = 100;              // Contiene números (pero no al principio)

echo "Ejemplos de nombres de variables VÁLIDOS:\n";
echo "nombre_usuario: " . $nombre_usuario . "\n";
echo "_variableOculta: " . $_variableOculta . "\n";
echo "valor1: " . $valor1 . "\n";
echo "\n----------------------------------------\n\n";


// Nombres de variables INVÁLIDOS (estos causarían un error si se descomentan):

// $1valor = 200;           // ERROR: No puede comenzar con un número.
// $mi-variable = "hola";   // ERROR: No puede contener guiones medios (-). Solo guion bajo (_).
// $nombre con espacio = "";// ERROR: No puede contener espacios.


// ## Reasignación de variables ##
// El tipo de una variable puede cambiar si le asignas un valor de otro tipo.

$miVariable = "Texto inicial";
echo "Valor y tipo iniciales:\n";
var_dump($miVariable); // Salida: string(13) "Texto inicial"

$miVariable = 50; // Ahora le asignamos un número entero.
echo "\nValor y tipo después de reasignar:\n";
var_dump($miVariable); // Salida: int(50)

?>