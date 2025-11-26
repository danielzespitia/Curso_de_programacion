<?php
$usuario = [
    "nombre"   => "Carlos", // "nombre" es la clave, "Carlos" es el valor
    "apellido" => "García",
    "edad"     => 30
];

// Para obtener un valor, usamos la clave (un string) entre corchetes [].
echo "El nombre del usuario es: " . $usuario["nombre"] . "\n";
?>