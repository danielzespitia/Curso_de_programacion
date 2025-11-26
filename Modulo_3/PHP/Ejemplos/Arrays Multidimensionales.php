<?php
$estudiantes = [
    [ "nombre" => "Elena", "nota" => 95 ], // Índice 0
    [ "nombre" => "Miguel", "nota" => 82 ], // Índice 1
    [ "nombre" => "Sofía", "nota" => 100 ] // Índice 2
];

// Para acceder, encadenamos los corchetes. Primero el índice del array exterior,
// y luego la clave del array interior.
echo "La nota de Miguel (estudiante en índice 1) es: " . $estudiantes[1]["nota"] . "\n";
?>