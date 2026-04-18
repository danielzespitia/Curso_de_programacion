<?php

echo "## 1. Integer (Entero) ##\n";
$edad = 30; // Un número entero positivo
$temperatura = -5; // Un número entero negativo
var_dump($edad); // Salida: int(30)
var_dump($temperatura); // Salida: int(-5)
echo "\n";


echo "## 2. Float / Double (Decimal) ##\n";
$precio = 19.99; // Un número con punto decimal
$pi = 3.14159;
var_dump($precio); // Salida: float(19.99)
var_dump($pi); // Salida: float(3.14159)
echo "\n";


echo "## 3. String (Cadena de texto) ##\n";
$saludo = "¡Hola, Mundo!"; // Se pueden usar comillas dobles
$mensaje = 'Este es un texto.'; // O comillas simples
var_dump($saludo); // Salida: string(13) "¡Hola, Mundo!"
var_dump($mensaje); // Salida: string(18) "Este es un texto."
echo "\n";


echo "## 4. Boolean (Booleano) ##\n";
$esValido = true; // Representa verdadero
$estaLloviendo = false; // Representa falso
var_dump($esValido); // Salida: bool(true)
var_dump($estaLloviendo); // Salida: bool(false)
echo "\n";


echo "## 5. Array (Arreglo) ##\n";
$frutas = array("Manzana", "Banana", "Naranja");
$colores = ["Rojo", "Verde", "Azul"];
echo "El segundo color es: " . $colores[1] . "\n\n"; // Salida: El segundo color es: Verde


echo "## 6. NULL ##\n";
$variableNula = NULL;
$sinValor; // Una variable no definida también tiene el valor NULL

var_dump($variableNula); // Salida: NULL
// var_dump($sinValor); // También mostraría NULL, pero con una advertencia (Notice)
echo "\n";
