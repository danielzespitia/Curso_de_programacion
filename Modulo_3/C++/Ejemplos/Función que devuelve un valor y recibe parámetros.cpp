#include <iostream>

// --- Definición de la función ---
// Esta función devuelve un valor de tipo 'int'.
// Recibe dos parámetros de tipo 'int', que dentro de la función se llamarán 'num1' y 'num2'.
int sumar(int num1, int num2) {
    // Cuerpo de la función:
    int resultado = num1 + num2;
    // La palabra clave 'return' envía el valor de 'resultado' de vuelta
    // al lugar donde la función 'sumar' fue llamada.
    return resultado;
}

int main() {
    int a = 15;
    int b = 7;

    // --- Llamada a la función ---
    // Llamamos a 'sumar' y le "pasamos" los valores de 'a' y 'b'.
    // El valor que 'sumar' retorna se guarda en la variable 'resultadoSuma'.
    int resultadoSuma = sumar(a, b);

    std::cout << "El valor de a es: " << a << std::endl;
    std::cout << "El valor de b es: " << b << std::endl;
    std::cout << "La suma calculada por la función es: " << resultadoSuma << std::endl;

    // También se puede usar directamente sin guardar en una variable.
    std::cout << "Otra suma (100 + 50): " << sumar(100, 50) << std::endl;

    return 0;
}