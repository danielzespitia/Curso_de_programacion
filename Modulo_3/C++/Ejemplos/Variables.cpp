#include <iostream>

int main() {
    // Declaración de una variable: tipo_dato nombre_variable;
    int x;
    char letra = 'A'; // Declaración de una variable de tipo char.

    // Inicialización: Asignar un valor por primera vez.
    x = 10; // Se le asigna el valor 10.

    // Declaración e inicialización en una sola línea.
    int y = 20;

    // Las variables pueden cambiar de valor.
    std::cout << "El valor inicial de y es: " << y << std::endl;
    y = 35; // Ahora 'y' vale 35.
    std::cout << "El nuevo valor de y es: " << y << std::endl;

    // Se pueden realizar operaciones con variables.
    int suma = x + y;
    std::cout << "La suma de x + y es: " << suma << std::endl;

    return 0;
}