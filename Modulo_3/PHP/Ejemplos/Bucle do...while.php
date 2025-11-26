<?php
echo "## 3. Ejemplo de bucle do...while ##\n";

$intentos = 0;
$pinCorrecto = false;

do {
    // Este bloque se ejecuta al menos la primera vez.
    $intentos++;
    echo "Intento #" . $intentos . ". Ingresando PIN...\n";

    // Simulamos que en el tercer intento se ingresa el PIN correcto.
    if ($intentos == 3) {
        $pinCorrecto = true;
        echo "PIN correcto. ¡Acceso concedido!\n";
    }

} while ($pinCorrecto == false); // La condición se revisa al final.

echo "\n";
?>