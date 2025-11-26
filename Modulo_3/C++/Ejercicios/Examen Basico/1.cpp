// Ejercicio 1: "Hola Mundo" y Tipos de Datos
// Escribe un programa que imprima en la consola el mensaje "¡Hola, Mundo!". 
// Luego, declara e inicializa una variable para cada uno de los siguientes tipos de datos: 
// entero (int), flotante (float), carácter (char) y booleano (bool). 
// Finalmente, imprime el valor de cada una de estas variables.

#include <iostream> // Librería para entrada y salida de datos (como imprimir en consola)

int main() {
    // Imprimir el clásico "Hola, Mundo"
    std::cout << "¡Hola, Mundo!" << std::endl;
    std::cout << "-------------------------" << std::endl;

    // Declaración e inicialización de variables
    int numeroEntero = 25;
    float numeroFlotante = 99.99f; // La 'f' indica que es un float
    char caracter = 'A';
    bool valorBooleano = true;

    // Imprimir los valores de las variables
    std::cout << "Valor del entero: " << numeroEntero << std::endl;
    std::cout << "Valor del flotante: " << numeroFlotante << std::endl;
    std::cout << "Valor del caracter: " << caracter << std::endl;
    std::cout << "Valor del booleano: " << valorBooleano << std::endl; // Imprimirá 1 para true, 0 para false

    return 0; // Indica que el programa terminó exitosamente
}

