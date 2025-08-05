<?php
// '$nombre' es un parámetro. Es un placeholder para el dato que recibiremos.
function saludoPersonalizado($nombre) {
    echo "Hola, " . $nombre . ". ¡Qué tengas un excelente día!\n";
}

// Llamamos a la misma función con diferentes datos de entrada (argumentos).
saludoPersonalizado("Ana");
saludoPersonalizado("Pedro");
saludoPersonalizado("Daniel")
?>

