// Ejercicio 4: Bucle for y Constantes con #define
// Utiliza #define para crear una constante simbólica llamada LIMITE con un valor de 10. 
// Luego, escribe un programa que pida al usuario un número y utilice un bucle for 
// para imprimir la tabla de multiplicar de ese número desde 1 hasta LIMITE.

#include <iostream>

// Definir una constante simbólica usando #define
#define LIMITE 10

int main() {
    int numero;

    // Pedir un número al usuario
    std::cout << "Introduce un numero para ver su tabla de multiplicar: ";
    std::cin >> numero;
    std::cout << "----------------------------------------------------" << std::endl;

    std::cout << "Tabla de multiplicar del " << numero << ":" << std::endl;

    // Bucle for para generar la tabla de multiplicar
    for (int i = 1; i <= LIMITE; ++i) {
        std::cout << numero << " x " << i << " = " << (numero * i) << std::endl;
    }

    return 0;
}
