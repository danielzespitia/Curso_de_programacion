// Ejercicio 6: Bucle do-while y switch
// Escribe un programa que muestre un menú simple con tres opciones: 
// 1. Saludar, 2. Despedirse, 3. Salir. El programa debe usar un bucle do-while 
// para mostrar el menú repetidamente hasta que el usuario elija la opción "Salir". 
// Utiliza una estructura switch para manejar la opción seleccionada por el usuario.

#include <iostream>

int main() {
    int opcion;

    // El bucle do-while asegura que el menú se muestre al menos una vez
    do {
        // Mostrar el menú
        std::cout << "\n--- MENU ---" << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Elige una opcion: ";
        std::cin >> opcion;

        // Estructura switch para manejar la opción del usuario
        switch (opcion) {
            case 1:
                std::cout << "¡Hola! Que tengas un buen dia." << std::endl;
                break; // 'break' es crucial para salir del switch
            case 2:
                std::cout << "¡Adios! Vuelve pronto." << std::endl;
                break;
            case 3:
                std::cout << "Saliendo del programa..." << std::endl;
                break;
            default: // Se ejecuta si la opción no es 1, 2 ni 3
                std::cout << "Opcion no valida. Por favor, intenta de nuevo." << std::endl;
                break;
        }

    } while (opcion != 3); // El bucle continúa mientras la opción no sea 3

    return 0;
}
