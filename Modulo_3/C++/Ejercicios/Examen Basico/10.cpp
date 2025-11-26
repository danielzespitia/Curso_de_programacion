// Ejercicio 10: Constantes const y Funciones void
// Crea un programa para calcular el perímetro de un círculo.
// 1. Declara una constante de tipo double usando la palabra clave const para el valor de Pi.
// 2. Escribe una función void llamada calcularPerimetro que no devuelva ningún valor 
//    pero que reciba como parámetro el radio del círculo.
// 3. Dentro de esta función, calcula el perímetro y muéstralo directamente en la consola.
// 4. Desde main, pide al usuario el radio y llama a la función calcularPerimetro.

#include <iostream>

// 1. Declarar una constante para PI usando 'const'
const double PI = 3.1415926535;

// 2. Declaración (prototipo) de la función void
void calcularPerimetro(double radio);

int main() {
    double radioUsuario;

    // 4. Pedir el radio al usuario
    std::cout << "Introduce el radio del circulo: ";
    std::cin >> radioUsuario;

    // Llamar a la función para que haga el cálculo y lo muestre
    calcularPerimetro(radioUsuario);

    return 0;
}

// Definición de la función
// Es 'void' porque no devuelve ningún valor. Su trabajo es imprimir.
void calcularPerimetro(double radio) {
    // 3. Calcular el perímetro
    double perimetro = 2 * PI * radio;
    
    // Mostrar el resultado directamente desde la función
    std::cout << "El perimetro del circulo es: " << perimetro << std::endl;
}
