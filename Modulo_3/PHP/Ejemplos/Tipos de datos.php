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
// Una sintaxis más moderna y común:
$colores = ["Rojo", "Verde", "Azul"];
var_dump($frutas);
/*
Salida:
array(3) {
  [0]=>
  string(7) "Manzana"
  [1]=>
  string(6) "Banana"
  [2]=>
  string(7) "Naranja"
}
*/
echo "El segundo color es: " . $colores[1] . "\n\n"; // Salida: El segundo color es: Verde


echo "## 6. Object (Objeto) ##\n";
// Primero, definimos una "plantilla" o clase
class Persona {
    public $nombre;
    public $edad;
}

// Ahora creamos una instancia (un objeto) de esa clase
$estudiante = new Persona();
$estudiante->nombre = "Ana"; // Asignamos valores a sus propiedades
$estudiante->edad = 22;
var_dump($estudiante);
/*
Salida:
object(Persona)#1 (2) {
  ["nombre"]=>
  string(3) "Ana"
  ["edad"]=>
  int(22)
}
*/
echo "\n";


echo "## 7. NULL ##\n";
$variableNula = NULL;
$sinValor; // Una variable no definida también tiene el valor NULL
var_dump($variableNula); // Salida: NULL
// var_dump($sinValor); // También mostraría NULL, pero con una advertencia (Notice)
echo "\n";


echo "## 8. Resource (Recurso) ##\n";
// Un recurso es una variable especial que contiene una referencia a un recurso externo.
// Por ejemplo, al abrir un archivo o una conexión a base de datos.

// Usamos @fopen para suprimir errores si el archivo no existe para este ejemplo.
$manejadorArchivo = @fopen("ejemplo.txt", "r");
var_dump($manejadorArchivo);
/*
Salida (si el archivo existe): resource(5) of type (stream)
Salida (si no existe): bool(false)
*/
if ($manejadorArchivo) {
    echo "El tipo de recurso es: " . get_resource_type($manejadorArchivo) . "\n"; // Salida: El tipo de recurso es: stream
    fclose($manejadorArchivo); // Es importante cerrar los recursos cuando terminas de usarlos.
}

?>