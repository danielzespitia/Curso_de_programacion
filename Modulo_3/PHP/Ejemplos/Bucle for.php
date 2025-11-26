<?php
echo "## 1. Ejemplo de bucle for (Tabla del 5) ##\n";

// Este bucle se ejecutará 10 veces.
// 1. Inicialización: $i = 1 (el contador empieza en 1)
// 2. Condición: $i <= 10 (el bucle continúa mientras $i sea menor o igual a 10)
// 3. Incremento: $i++ (en cada vuelta, se suma 1 a $i)
for ($i = 1; $i <= 10; $i++) {
    echo "5 x " . $i . " = " . (5 * $i) . "\n";
}
echo "\n";
?>