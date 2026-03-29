#include <iostream>

int main() {
    int dia;
    std::cout << "Introduce un número del 1 al 3 para elegir un día: ";
    std::cin >> dia;

    // La variable 'dia' se evalúa.
    switch (dia) {
        case '1': // Si 'dia' es 1
            std::cout << "Elegiste Lunes." << std::endl;
            break; // 'break' es crucial para salir del switch. Sin él, se ejecutarían los casos siguientes.
        case 2: // Si 'dia' es 2
            std::cout << "Elegiste Martes." << std::endl;
            break;
        case 3: // Si 'dia' es 3
            std::cout << "Elegiste Miércoles." << std::endl;
            break;
        default: // Si 'dia' no coincide con ningún caso.
            std::cout << "Número no válido." << std::endl;
            break;
    }
    return 0;
}