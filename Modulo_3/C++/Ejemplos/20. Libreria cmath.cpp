// Incluimos las librerías necesarias.
#include <iostream>
#include <cmath> // Necesaria para las funciones matemáticas

int main() {
    double numero = 64.0;
    double base = 2.0;
    double exponente = 8.0;

    // Calcular la raíz cuadrada con sqrt().
    double raiz = sqrt(numero);
    std::cout << "La raíz cuadrada de " << numero << " es " << raiz << std::endl;

    // Calcular una potencia con pow(base, exponente).
    double potencia = pow(base, exponente);
    std::cout << base << " elevado a " << exponente << " es " << potencia << std::endl;

    // Redondear un número.
    double valor = 3.7;
    std::cout << "Redondeo hacia arriba (ceil) de " << valor << " es " << ceil(valor) << std::endl;
    std::cout << "Redondeo hacia abajo (floor) de " << valor << " es " << floor(valor) << std::endl;

    // Funciones trigonométricas (reciben el ángulo en radianes).
    double anguloRadianes = 1.5708; // Aproximadamente 90 grados
    std::cout << "El seno de " << anguloRadianes << " radianes es " << sin(anguloRadianes) << std::endl;
    
    // Valor absoluto
    double numNegativo = -15.5;
    std::cout << "El valor absoluto de " << numNegativo << " es " << fabs(numNegativo) << std::endl; // Para doubles/floats
    std::cout << "El valor absoluto de -10 es " << abs(-10) << std::endl; // Para enteros

    return 0;
}