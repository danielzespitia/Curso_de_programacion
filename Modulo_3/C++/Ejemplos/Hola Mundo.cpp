// Incluimos la librería iostream para poder usar cout y cin
#include <iostream>

int main() {

    std::cout << "¡Hola, mundo!" << std::endl;

    int edad; 
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;

    std::cout << "Tienes " << edad << " años." << std::endl;
    return 0;
}