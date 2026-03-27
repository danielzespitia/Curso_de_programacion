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

$igualdad = ($edad == $nombre); // true, porque compara solo el valor
$identidad = ($edad === $nombre); // false, porque compara valor y tipo
$diferente = ($edad != $nombre); // false, porque compara solo el valor
$noIdentico = ($edad !== $nombre); // true, porque compara valor y tipo
$mayor = ($edad > 18); // true
$menor = ($edad < 30); // true
$mayor_igual = ($edad >= 18); // true
$menor_igual = ($edad <= 30); // true

// ## 4. Operadores Lógicos ##
$esEstudiante = true;
$tieneBeca = false;

$and = $esEstudiante && $tieneBeca; // AND lógico
$or = $esEstudiante || $tieneBeca;  // OR lógico
$not = !$esEstudiante; // NOT lógico

// ## 5. Operadores de Incremento/Decremento ##
$contador = 5;
$contador++; // Aumenta el valor en 1
echo "Incremento (++): " . $contador . "\n"; // Salida: 6

$contador--; // Disminuye el valor en 1
echo "Decremento (--): " . $contador . "\n\n"; // Salida: 5
