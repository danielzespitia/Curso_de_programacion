#include <iostream>

int main() {
    // Tipo int: para números enteros.
    int numeroEntero = 10;
    std::cout << "Entero: " << numeroEntero << std::endl;

    // Tipo double: para números con decimales de alta precisión.
    double numeroDecimalLargo = 3.1415926535;
    std::cout << "Double: " << numeroDecimalLargo << std::endl;

    // Tipo float: para números con decimales de menor precisión.
    float numeroDecimalCorto = 9.81f; // La 'f' final es buena práctica para literales float.
    std::cout << "Float: " << numeroDecimalCorto << std::endl;

    // Tipo char: para un solo carácter. Se usan comillas simples ''.
    char letra = 'A';
    std::cout << "Char: " << letra << std::endl;

    // Tipo bool: para valores de verdadero o falso.
    bool esVerdadero = true;
    std::cout << "Bool (true): " << esVerdadero << std::endl; // Imprimirá 1
    esVerdadero = false;
    std::cout << "Bool (false): " << esVerdadero << std::endl; // Imprimirá 0

    // Usando modificadores
    unsigned int edadSinSigno = 25; // Solo puede ser positivo.
    std::cout << "Unsigned Int: " << edadSinSigno << std::endl;

    short int numeroCorto = 32000;
    std::cout << "Short Int: " << numeroCorto << std::endl;
    
    long long int numeroMuyLargo = 987654321012345678;
    std::cout << "Long Long Int: " << numeroMuyLargo << std::endl;

    return 0;
}