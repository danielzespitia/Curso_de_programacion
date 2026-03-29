<?php
echo "## 3. Ejemplo de if / elseif / else ##\n";

// La hora actual en formato de 24 horas (ej. 14 para las 2 PM)
$horaActual = 1;

if ($horaActual < 12) {
    echo "¡Buenos días!\n";
} 
else if ($horaActual < 18) {
    echo "¡Buenas tardes!\n";
} 
else {
    echo "¡Buenas noches!\n";
}
echo "\n";

// Condiciones con ToLower y ToUpper
$color = "Rojo";
if (strtolower($color) == "rojo") {
    echo "El color es rojo (comparación en minúsculas).\n";
} 
else if (strtoupper($color) == "ROJO") {
    echo "El color es rojo (comparación en mayúsculas).\n";
} 
else {
    echo "El color no es rojo.\n";
}
?>