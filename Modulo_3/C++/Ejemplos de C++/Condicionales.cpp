#include <iostream>

int main() {
    int edad;
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;

    // El programa evaluará las condiciones en orden.
    if (edad < 18) {
        // Este bloque se ejecuta si la edad es menor a 18.
        std::cout << "Eres menor de edad." << std::endl;
    } 
    
    else if (edad >= 18 && edad <= 65) {
        // Si no es menor de 18, comprueba si está entre 18 y 65.
        // '&&' es el operador Y lógico (ambas condiciones deben ser ciertas).
        std::cout << "Eres un adulto." << std::endl;
    } 
    
    else {
        // Si ninguna de las anteriores es cierta (mayor de 65).
        std::cout << "Eres un adulto mayor." << std::endl;
    }

    return 0;
}