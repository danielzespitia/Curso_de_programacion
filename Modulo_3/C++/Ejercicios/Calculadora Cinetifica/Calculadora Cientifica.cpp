#include <iostream>
#include <cmath>    // Para las funciones matemáticas (pow, sqrt, sin, cos, etc.)
#include <limits>   // Para numeric_limits, necesario para validar la entrada

// --- Prototipos de las Funciones ---
// Es una buena práctica declarar los prototipos al principio.
void mostrarMenu();
double obtenerNumero();
double gradosARadianes(double grados);

int main() {
    int opcion;
    double resultado = 0.0;
    double num1, num2;

    // El bucle principal 'do-while' asegura que el programa se ejecute al menos una vez
    // y continúe hasta que el usuario elija la opción de salir (0).
    do {
        mostrarMenu();
        std::cout << "Elige una opción: ";
        std::cin >> opcion;

        // --- Validación de Entrada ---
        // Si el usuario no introduce un número (p.ej. una letra), cin falla.
        while (std::cin.fail()) {
            std::cout << "Entrada no válida. Por favor, introduce un número: ";
            std::cin.clear(); // Resetea el flag de error de cin.
            // Ignora el resto de la línea de entrada incorrecta.
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cin >> opcion;
        }

        // El 'switch' dirige el flujo del programa basado en la opción del usuario.
        switch (opcion) {
            case 1: // Suma
                std::cout << "Introduce el primer número: ";
                num1 = obtenerNumero();
                std::cout << "Introduce el segundo número: ";
                num2 = obtenerNumero();
                resultado = num1 + num2;
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 2: // Resta
                std::cout << "Introduce el primer número: ";
                num1 = obtenerNumero();
                std::cout << "Introduce el segundo número: ";
                num2 = obtenerNumero();
                resultado = num1 - num2;
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 3: // Multiplicación
                std::cout << "Introduce el primer número: ";
                num1 = obtenerNumero();
                std::cout << "Introduce el segundo número: ";
                num2 = obtenerNumero();
                resultado = num1 * num2;
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 4: // División
                std::cout << "Introduce el dividendo: ";
                num1 = obtenerNumero();
                std::cout << "Introduce el divisor: ";
                num2 = obtenerNumero();
                if (num2 == 0) {
                    std::cout << "Error: No se puede dividir por cero." << std::endl;
                } else {
                    resultado = num1 / num2;
                    std::cout << "Resultado: " << resultado << std::endl;
                }
                break;
            case 5: // Potencia
                std::cout << "Introduce la base: ";
                num1 = obtenerNumero();
                std::cout << "Introduce el exponente: ";
                num2 = obtenerNumero();
                resultado = pow(num1, num2); // Uso de la función de <cmath>
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 6: // Raíz Cuadrada
                std::cout << "Introduce el número: ";
                num1 = obtenerNumero();
                if (num1 < 0) {
                    std::cout << "Error: No se puede calcular la raíz de un número negativo." << std::endl;
                } else {
                    resultado = sqrt(num1); // Uso de la función de <cmath>
                    std::cout << "Resultado: " << resultado << std::endl;
                }
                break;
            case 7: // Seno
                std::cout << "Introduce el ángulo en grados: ";
                num1 = obtenerNumero();
                resultado = sin(gradosARadianes(num1)); // Convertimos a radianes antes de calcular
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 8: // Coseno
                std::cout << "Introduce el ángulo en grados: ";
                num1 = obtenerNumero();
                resultado = cos(gradosARadianes(num1));
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 9: // Tangente
                std::cout << "Introduce el ángulo en grados: ";
                num1 = obtenerNumero();
                resultado = tan(gradosARadianes(num1));
                std::cout << "Resultado: " << resultado << std::endl;
                break;
            case 0: // Salir
                std::cout << "Saliendo de la calculadora. ¡Adiós!" << std::endl;
                break;
            default: // Opción no válida
                std::cout << "Opción no válida. Por favor, intenta de nuevo." << std::endl;
                break;
        }
        // Pausa para que el usuario pueda ver el resultado antes de que el menú se vuelva a mostrar.
        if (opcion != 0) {
            std::cout << "\nPresiona Enter para continuar...";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cin.get();
        }

    } while (opcion != 0);

    return 0;
}

// --- Definiciones de las Funciones Auxiliares ---

/**
 * @brief Muestra el menú de operaciones de la calculadora.
 */
void mostrarMenu() {
    // system("cls"); // Descomenta en Windows para limpiar la pantalla
    // system("clear"); // Descomenta en Linux/Mac para limpiar la pantalla
    std::cout << "\n--- Calculadora Científica ---" << std::endl;
    std::cout << "1. Suma" << std::endl;
    std::cout << "2. Resta" << std::endl;
    std::cout << "3. Multiplicación" << std::endl;
    std::cout << "4. División" << std::endl;
    std::cout << "5. Potencia (x^y)" << std::endl;
    std::cout << "6. Raíz Cuadrada" << std::endl;
    std::cout << "7. Seno" << std::endl;
    std::cout << "8. Coseno" << std::endl;
    std::cout << "9. Tangente" << std::endl;
    std::cout << "0. Salir" << std::endl;
    std::cout << "-----------------------------" << std::endl;
}

/**
 * @brief Lee un número del usuario y valida que la entrada sea correcta.
 * @return El número de tipo double introducido por el usuario.
 */
double obtenerNumero() {
    double numero;
    std::cin >> numero;
    while (std::cin.fail()) {
        std::cout << "Entrada no válida. Por favor, introduce un número: ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin >> numero;
    }
    return numero;
}

/**
 * @brief Convierte un ángulo de grados a radianes.
 * @param grados El ángulo en grados.
 * @return El ángulo equivalente en radianes.
 */
double gradosARadianes(double grados) {
    const double PI = 3.14159265358979323846;
    return grados * PI / 180.0;
}