#include <iostream>

int main() {
    // Este bucle se ejecutará 5 veces.
    // 1. Inicialización: 'int i = 0;' se ejecuta una sola vez al empezar.
    // 2. Condición: 'i < 5;' se comprueba antes de cada repetición. Si es falso, el bucle termina.
    // 3. Incremento: 'i++' se ejecuta después de cada repetición.
    for (int i = 0; i < 5; i++) {
        std::cout << "El valor de i es: " << i << std::endl;
    }
    return 0;
}