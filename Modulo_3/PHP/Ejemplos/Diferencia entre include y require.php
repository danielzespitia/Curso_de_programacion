<?php

// config.php
$nombre_web = "Mi Sitio Web Esencial";

function mostrar_footer() {
    echo "<p>Copyright 2025 | Todos los derechos reservados.</p>";
}

## 1. Ejemplo con `include` ##

echo "--- Probando 'include' con un archivo que NO existe ---\n";
// Intentamos incluir un archivo que no está en la carpeta.
include 'archivo_inexistente.php';
// A pesar del error (Warning), el script NO se detiene y esta línea se ejecuta.
echo "Esta línea se muestra porque 'include' solo genera una advertencia (Warning).\n\n";


## 2. Ejemplo con `require` ##

echo "--- Probando 'require' para un archivo ESENCIAL que SÍ existe ---\n";
// 'require' es ideal para archivos de configuración, funciones o clases críticas.
require 'config.php';
echo "El nombre de la web es: " . $nombre_web . "\n"; // La variable $nombre_web está disponible.
mostrar_footer(); // La función mostrar_footer() también está disponible.
echo "\n";


echo "--- Probando 'require' con un archivo que NO existe ---\n";
echo "Esta línea se va a mostrar...\n";
// La siguiente línea causará un ERROR FATAL. El script se detendrá aquí.
require 'archivo_inexistente.php';

// ¡¡ESTA LÍNEA NUNCA SE EJECUTARÁ!!
echo "Esta línea no la verás nunca en la pantalla.\n";
?>