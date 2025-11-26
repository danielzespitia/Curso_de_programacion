#include <iostream>

int main() {
    int numeroSecreto = 7;
    int intento;

    // El bloque 'do' se ejecuta al menos una vez.
    do {
        std::cout << "Adivina el número (entre 1 y 10): ";
        std::cin >> intento;

        if (intento != numeroSecreto) {
            std::cout << "Incorrecto. Intenta de nuevo." << std::endl;
        }
    // La condición se evalúa después de ejecutar el bloque.
    } while (intento != numeroSecreto);

    std::cout << "¡Felicidades! Adivinaste el número." << std::endl;

    return 0;
}