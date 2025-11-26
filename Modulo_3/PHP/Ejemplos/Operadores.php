<?php

// ## 1. Operadores Aritméticos ##
$numero1 = 10;
$numero2 = 3;

echo "Suma: " . ($numero1 + $numero2) . "\n";          // Salida: 13
echo "Resta: " . ($numero1 - $numero2) . "\n";         // Salida: 7
echo "Multiplicación: " . ($numero1 * $numero2) . "\n"; // Salida: 30
echo "División: " . ($numero1 / $numero2) . "\n";       // Salida: 3.33...
echo "Módulo: " . ($numero1 % $numero2) . "\n\n";         // Salida: 1 (el resto de 10/3)

// ## 2. Operadores de Asignación ##
$valor = 5;
$valor += 2; // Equivalente a: $valor = $valor + 2;
echo "Asignación con suma (+=): " . $valor . "\n\n"; // Salida: 7

// ## 3. Operadores de Comparación ##
$edad = 20;
$nombre = "20";

if ($edad == $nombre) {
    echo "== : Son iguales en valor.\n"; // Se ejecuta
}

if ($edad === $nombre) {
    echo "=== : Son idénticos en valor y tipo.\n"; // No se ejecuta porque uno es int y el otro string
}

if ($edad != 18) {
    echo "!= : Es diferente de 18.\n\n"; // Se ejecuta
}

// ## 4. Operadores Lógicos ##
$esEstudiante = true;
$tieneBeca = false;

if ($esEstudiante && $edad < 25) {
    echo "&& : Es un estudiante menor de 25 años.\n"; // Se ejecuta
}

if ($esEstudiante || $tieneBeca) {
    echo "|| : Es estudiante o tiene beca.\n\n"; // Se ejecuta
}

// ## 5. Operadores de Incremento/Decremento ##
$contador = 5;
$contador++; // Aumenta el valor en 1
echo "Incremento (++): " . $contador . "\n"; // Salida: 6

$contador--; // Disminuye el valor en 1
echo "Decremento (--): " . $contador . "\n\n"; // Salida: 5

// ## 6. Operador de Concatenación ##
$nombre = "Juan";
$apellido = "Pérez";
$nombreCompleto = $nombre . " " . $apellido;

echo "Concatenación (.): " . $nombreCompleto . "\n"; // Salida: Juan Pérez

?>