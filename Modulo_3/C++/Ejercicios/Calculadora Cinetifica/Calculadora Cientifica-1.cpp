#include <iostream> // Para entrada y salida (cin, cout)
#include <cmath>    // Para funciones matemáticas (sqrt, pow, sin, cos, tan, log)
#include <limits>   // Para limpiar el buffer de entrada en caso de error

// Constante para la conversión de grados a radianes
const double PI = 3.14159265358979323846;

// --- Prototipos de las funciones ---
// Así, el programa principal (main) sabe que estas funciones existen.

void mostrarMenu();
void sumar();
void restar();
void multiplicar();
void dividir();
void potencia();
void raizCuadrada();
void seno();
void coseno();
void tangente();
void logaritmoNeperiano();
void limpiarPantalla(); // Función de utilidad para mejorar la legibilidad

int main() {
    int opcion;

    // El bucle do-while asegura que el menú se muestre al menos una vez
    do {
        mostrarMenu();
        std::cout << "Seleccione una operación: ";
        std::cin >> opcion;

        // Validar que la entrada sea un número
        if (std::cin.fail()) {
            std::cout << "\nError: Por favor, ingrese solo un número.\n";
            std::cin.clear(); // Limpia el estado de error de cin
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Descarta la entrada incorrecta
            opcion = -1; // Asigna un valor inválido para que el switch no haga nada
        }

        limpiarPantalla(); // Limpia la consola para una mejor visualización

        switch (opcion) {
            case 1:  sumar();                 break;
            case 2:  restar();                break;
            case 3:  multiplicar();           break;
            case 4:  dividir();               break;
            case 5:  potencia();              break;
            case 6:  raizCuadrada();          break;
            case 7:  seno();                  break;
            case 8:  coseno();                break;
            case 9:  tangente();              break;
            case 10: logaritmoNeperiano();    break;
            case 0:
                std::cout << "¡Gracias por usar la calculadora! ¡Hasta luego!\n";
                break;
            default:
                std::cout << "Opción no válida. Por favor, intente de nuevo.\n";
                break;
        }

        if (opcion != 0) {
             std::cout << "\nPresione Enter para continuar...";
             std::cin.get(); // Espera la primera pulsación de Enter
             std::cin.get(); // Espera la segunda (necesario después de un 'cin >>')
             limpiarPantalla();
        }

    } while (opcion != 0);

    return 0;
}

// --- Implementación de las funciones ---

void mostrarMenu() {
    std::cout << "==== CALCULADORA CIENTÍFICA ====\n";
    std::cout << "1. Sumar                  6. Raíz Cuadrada\n";
    std::cout << "2. Restar                 7. Seno(x)\n";
    std::cout << "3. Multiplicar            8. Coseno(x)\n";
    std::cout << "4. Dividir                9. Tangente(x)\n";
    std::cout << "5. Potencia (x^y)         10. Logaritmo Neperiano(x)\n";
    std::cout << "0. SALIR\n";
    std::cout << "==================================\n";
}

void limpiarPantalla() {
#ifdef _WIN32
    system("cls");
#else
    // Para Linux y macOS
    system("clear");
#endif
}

// --- Operaciones Aritméticas ---

void sumar() {
    double a, b;
    std::cout << "--- Suma ---\n";
    std::cout << "Ingrese el primer número: "; std::cin >> a;
    std::cout << "Ingrese el segundo número: "; std::cin >> b;
    std::cout << "Resultado: " << a << " + " << b << " = " << a + b << std::endl;
}

void restar() {
    double a, b;
    std::cout << "--- Resta ---\n";
    std::cout << "Ingrese el primer número: "; std::cin >> a;
    std::cout << "Ingrese el segundo número: "; std::cin >> b;
    std::cout << "Resultado: " << a << " - " << b << " = " << a - b << std::endl;
}

void multiplicar() {
    double a, b;
    std::cout << "--- Multiplicación ---\n";
    std::cout << "Ingrese el primer número: "; std::cin >> a;
    std::cout << "Ingrese el segundo número: "; std::cin >> b;
    std::cout << "Resultado: " << a << " * " << b << " = " << a * b << std::endl;
}

void dividir() {
    double a, b;
    std::cout << "--- División ---\n";
    std::cout << "Ingrese el dividendo: "; std::cin >> a;
    std::cout << "Ingrese el divisor: "; std::cin >> b;
    
    // VALIDACIÓN: No se puede dividir por cero
    if (b == 0) {
        std::cout << "Error: No se puede dividir entre cero.\n";
    } else {
        std::cout << "Resultado: " << a << " / " << b << " = " << a / b << std::endl;
    }
}

// --- Funciones Científicas ---

void potencia() {
    double base, exponente;
    std::cout << "--- Potencia ---\n";
    std::cout << "Ingrese la base: "; std::cin >> base;
    std::cout << "Ingrese el exponente: "; std::cin >> exponente;
    std::cout << "Resultado: " << base << "^" << exponente << " = " << pow(base, exponente) << std::endl;
}

void raizCuadrada() {
    double numero;
    std::cout << "--- Raíz Cuadrada ---\n";
    std::cout << "Ingrese un número: "; std::cin >> numero;

    // VALIDACIÓN: No se puede calcular la raíz de un número negativo
    if (numero < 0) {
        std::cout << "Error: No se puede calcular la raíz cuadrada de un número negativo.\n";
    } else {
        std::cout << "Resultado: La raíz cuadrada de " << numero << " es " << sqrt(numero) << std::endl;
    }
}

void seno() {
    double grados;
    std::cout << "--- Seno ---\n";
    std::cout << "Ingrese el ángulo en GRADOS: "; std::cin >> grados;
    double radianes = grados * PI / 180.0; // Conversión a radianes
    std::cout << "El seno de " << grados << " grados es: " << sin(radianes) << std::endl;
}

void coseno() {
    double grados;
    std::cout << "--- Coseno ---\n";
    std::cout << "Ingrese el ángulo en GRADOS: "; std::cin >> grados;
    double radianes = grados * PI / 180.0; // Conversión a radianes
    std::cout << "El coseno de " << grados << " grados es: " << cos(radianes) << std::endl;
}

void tangente() {
    double grados;
    std::cout << "--- Tangente ---\n";
    std::cout << "Ingrese el ángulo en GRADOS: "; std::cin >> grados;
    
    // VALIDACIÓN: La tangente es indefinida para 90, 270, etc.
    if (fmod(grados, 180) == 90) {
        std::cout << "Error: La tangente es indefinida para " << grados << " grados.\n";
    } else {
        double radianes = grados * PI / 180.0; // Conversión a radianes
        std::cout << "La tangente de " << grados << " grados es: " << tan(radianes) << std::endl;
    }
}

void logaritmoNeperiano() {
    double numero;
    std::cout << "--- Logaritmo Neperiano ---\n";
    std::cout << "Ingrese un número: "; std::cin >> numero;

    // VALIDACIÓN: El logaritmo solo está definido para números positivos
    if (numero <= 0) {
        std::cout << "Error: El logaritmo solo está definido para números positivos.\n";
    } else {
        std::cout << "El logaritmo neperiano de " << numero << " es " << log(numero) << std::endl;
    }
}