#include <iostream>

int main() {
    int contador = 0;

    // Mientras 'contador' sea menor que 5, el bucle continuará.
    while (contador < 5) {
        std::cout << "Contador en: " << contador << std::endl;
        contador++; // Es fundamental modificar la variable de control dentro del bucle para evitar un ciclo infinito.
    }
    return 0;
}