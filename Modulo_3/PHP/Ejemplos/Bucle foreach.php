<?php
echo "## 4. Ejemplo de bucle foreach ##\n";

// Ejemplo 1: Recorriendo un array simple
echo "Lista de frutas:\n";
$frutas = ["Manzana", "Naranja", "Fresa", "Uva"];

foreach ($frutas as $fruta) {
    echo "- " . $fruta . "\n";
}

echo "\n";


// Ejemplo 2: Recorriendo un array asociativo (clave => valor)
echo "Capitales de países:\n";
$capitales = [
    "Venezuela" => "Caracas",
    "Francia" => "París",
    "Japón" => "Tokio"
];

forecah ($capitales as $pais => $capital) {
    echo "La capital de " . $pais . " es " . $capital . ".\n";
}
?>