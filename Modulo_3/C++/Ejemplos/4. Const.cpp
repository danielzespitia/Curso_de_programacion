#include <iostream>

int main() {
    // --- Declaración de constantes con 'const' ---
    // Se declaran como una variable normal, pero con 'const' al principio.
    // Es una convención escribirlas en MAYÚSCULAS para distinguirlas fácilmente.
    const double PI = 3.1415926535;
    const int DIAS_SEMANA = 7;
    const std::string MENSAJE_BIENVENIDA = "Bienvenido al calculador de áreas";

    std::cout << MENSAJE_BIENVENIDA << std::endl;

    double radio = 10.0;
    // Usamos la constante PI en un cálculo.
    double area = PI * radio * radio;

    std::cout << "El área de un círculo con radio " << radio << " es " << area << std::endl;
    std::cout << "Recuerda que la semana tiene " << DIAS_SEMANA << " días." << std::endl;

    // Si intentas modificar una constante, el compilador dará un error.
    // DIAS_SEMANA = 8; // ¡ERROR DE COMPILACIÓN! No se puede asignar a una variable que es const.

    return 0;
}