// Ejercicio 2: Operadores y Librería cmath
// Crea un programa que solicite al usuario dos números. El programa debe calcular y mostrar:
// * La suma, resta, multiplicación y división de los dos números.
// * Utilizando la librería <cmath>, calcula y muestra la potencia del primer número 
//   elevado al segundo y la raíz cuadrada del primer número.

#include <iostream> // Para entrada/salida
#include <cmath>    // Para funciones matemáticas como pow() y sqrt()

int main() {
    double num1, num2; // Usamos double para mayor precisión

    // Solicitar los números al usuario
    std::cout << "Introduce el primer numero: ";
    std::cin >> num1;
    std::cout << "Introduce el segundo numero: ";
    std::cin >> num2;
    std::cout << "-------------------------" << std::endl;

    // Operaciones aritméticas básicas
    std::cout << "Suma: " << num1 + num2 << std::endl;
    std::cout << "Resta: " << num1 - num2 << std::endl;
    std::cout << "Multiplicacion: " << num1 * num2 << std::endl;
    
    // Comprobar si el segundo número es cero antes de dividir
    if (num2 != 0) {
        std::cout << "Division: " << num1 / num2 << std::endl;
    } else {
        std::cout << "Division: No se puede dividir por cero." << std::endl;
    }

    // Operaciones con la librería cmath
    std::cout << "Potencia (" << num1 << " elevado a " << num2 << "): " << pow(num1, num2) << std::endl;
    
    // Comprobar si el primer número es no negativo para la raíz cuadrada
    if (num1 >= 0) {
        std::cout << "Raiz cuadrada de " << num1 << ": " << sqrt(num1) << std::endl;
    } else {
        std::cout << "Raiz cuadrada de " << num1 << ": No se puede calcular la raiz de un numero negativo." << std::endl;
    }

    return 0;
}
