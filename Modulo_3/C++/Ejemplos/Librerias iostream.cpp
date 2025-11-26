// Incluimos la librería para operaciones de entrada y salida.
#include <iostream>

int main() {
    // Declaramos una variable de tipo string para guardar el nombre del usuario.
    std::string nombre;

    // Usamos std::cout para pedirle al usuario que ingrese su nombre.
    std::cout << "Por favor, introduce tu nombre: ";

    // Usamos std::cin para leer el nombre que el usuario escribe en la consola
    // y lo guardamos en la variable 'nombre'.
    std::cin >> nombre;

    // Mostramos un saludo personalizado utilizando el nombre que leímos.
    std::cout << "Hola, " << nombre << ". ¡Bienvenido a C++!" << std::endl;
    
    // std::cerr se usa para mensajes de error. A menudo se muestra en la consola
    // de un color diferente para distinguirlo de la salida normal.
    std::cerr << "Este es un mensaje de error de ejemplo." << std::endl;

    return 0;
}