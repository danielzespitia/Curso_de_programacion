<?php
echo "## 3. Ejemplo de if / elseif / else ##\n";

// La hora actual en formato de 24 horas (ej. 14 para las 2 PM)
$horaActual = 1;

if ($horaActual < 12) {
    echo "¡Buenos días!\n";
} 
else if ($horaActual < 18) {
    // Esta condición se revisa solo si la primera ($horaActual < 12) fue falsa.
    echo "¡Buenas tardes!\n";
} 
else {
    // Este bloque se ejecuta si ninguna de las condiciones anteriores fue verdadera.
    echo "¡Buenas noches!\n";
}
echo "\n";
?>