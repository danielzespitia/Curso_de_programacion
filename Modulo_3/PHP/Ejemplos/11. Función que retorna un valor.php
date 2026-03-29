<?php
function sumar($num1, $num2) {
    $resultado = $num1 + $num2;
    return $resultado; // En lugar de imprimir, la función devuelve el valor.
}

// Llamamos a la función y su valor devuelto se almacena en la variable $total.
$total = sumar(10, 5); 

echo "El resultado de la suma es: " . $total . "\n";
?>