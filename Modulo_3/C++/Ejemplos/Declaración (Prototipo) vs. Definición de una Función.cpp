#include <iostream>
#include <string>

// --- Prototipos de las funciones ---
// Le decimos al compilador: "Oye, más adelante en el código existirán estas funciones.
// Confía en mí y déjame usarlas".
void saludarUsuario(std::string nombre);
double calcularAreaCirculo(double radio);


// --- Función principal ---
int main() {
    std::string usuario = "Ana";
    saludarUsuario(usuario); // Funciona porque el prototipo fue declarado antes.

    double radio = 5.0;
    double area = calcularAreaCirculo(radio); // También funciona gracias al prototipo.
    std::cout << "El área de un círculo con radio " << radio << " es " << area << std::endl;

    return 0;
}


// --- Definiciones de las funciones ---
// Aquí, después de main, escribimos el código completo de cada función.

// Definición de la función saludarUsuario
void saludarUsuario(std::string nombre) {
    std::cout << "¡Hola, " << nombre << "! Que tengas un buen día." << std::endl;
}

// Definición de la función calcularAreaCirculo
double calcularAreaCirculo(double radio) {
    const double PI = 3.14159;
    return PI * radio * radio;
}