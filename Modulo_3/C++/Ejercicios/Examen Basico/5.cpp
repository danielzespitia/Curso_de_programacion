// Ejercicio 5: Bucle while
// Crea un programa que simule un juego de adivinanza. El programa debe generar 
// un número secreto (puedes asignarlo tú mismo, por ejemplo, int numeroSecreto = 42;). 
// Luego, debe pedir al usuario que adivine el número. Utiliza un bucle while para que 
// el programa siga pidiendo un número mientras el usuario no adivine el correcto. 
// Proporciona pistas como "más alto" o "más bajo".

#include <iostream>

int main() {
    int numeroSecreto = 42;
    int intentoUsuario = 0; // Inicializar con un valor que no sea el secreto

    std::cout << "¡Adivina el numero secreto (entre 1 y 100)!" << std::endl;

    // El bucle se ejecuta mientras el intento del usuario sea diferente al número secreto
    while (intentoUsuario != numeroSecreto) {
        std::cout << "Introduce tu intento: ";
        std::cin >> intentoUsuario;

        if (intentoUsuario < numeroSecreto) {
            std::cout << "El numero secreto es mas alto." << std::endl;
        } else if (intentoUsuario > numeroSecreto) {
            std::cout << "El numero secreto es mas bajo." << std::endl;
        }
    }

    // Este mensaje solo se muestra cuando el bucle termina
    std::cout << "¡Felicidades! Adivinaste el numero secreto: " << numeroSecreto << std::endl;

    return 0;
}
