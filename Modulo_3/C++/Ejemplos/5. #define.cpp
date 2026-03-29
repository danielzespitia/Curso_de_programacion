#include <iostream>

// --- Definición de constantes con '#define' ---
// Sintaxis: #define NOMBRE_CONSTANTE VALOR
// No se usa el operador de asignación (=) y no lleva punto y coma al final.
#define VELOCIDAD_LUZ 299792458
#define VERSION "1.0.2"

int main() {
    std::cout << "Este programa está en la versión: " << VERSION << std::endl;
    
    long long distancia_tierra_sol = 149600000000; // en metros
    
    // El preprocesador reemplazará 'VELOCIDAD_LUZ' por '299792458' antes de compilar.
    double tiempo_segundos = (double)distancia_tierra_sol / VELOCIDAD_LUZ;
    
    std::cout << "La luz del Sol tarda aproximadamente " << tiempo_segundos << " segundos en llegar a la Tierra." << std::endl;

    return 0;
}