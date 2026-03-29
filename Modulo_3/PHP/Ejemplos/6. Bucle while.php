<?php
echo "## 2. Ejemplo de bucle while ##\n";

$bateria = 100; // Nivel de batería inicial

while ($bateria > 0) {
    echo "Batería restante: " . $bateria . "%. Usando el dispositivo.\n";
    $bateria -= 10; // Disminuimos la batería en cada ciclo.
}

echo "¡Batería agotada! El bucle ha terminado.\n\n";
?>