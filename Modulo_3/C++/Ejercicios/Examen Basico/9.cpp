// Ejercicio 9: Librerías vector y string
// Escribe un programa que pida al usuario que ingrese 3 de sus comidas favoritas. 
// Almacena cada comida en un vector de tipo string. Después de que el usuario 
// haya ingresado las tres, utiliza un bucle para recorrer el vector e imprimir 
// cada una de las comidas en la consola.

#include <iostream>
#include <vector>   // Para usar el contenedor std::vector
#include <string>   // Para usar el tipo de dato std::string

int main() {
    // Declarar un vector que almacenará strings
    std::vector<std::string> comidasFavoritas;
    std::string comidaTemporal;

    std::cout << "Por favor, introduce tus 3 comidas favoritas." << std::endl;

    // Bucle para pedir las 3 comidas
    for (int i = 0; i < 3; ++i) {
        std::cout << "Comida " << i + 1 << ": ";
        
        // std::getline es mejor para leer strings que pueden contener espacios
        // std::ws consume cualquier espacio en blanco inicial (como el 'enter' de una lectura anterior)
        std::getline(std::cin >> std::ws, comidaTemporal); 
        
        // Añadir la comida al final del vector
        comidasFavoritas.push_back(comidaTemporal);
    }

    std::cout << "\n--- Tus comidas favoritas son ---" << std::endl;

    // Bucle para recorrer el vector e imprimir su contenido
    for (int i = 0; i < comidasFavoritas.size(); ++i) {
        std::cout << "- " << comidasFavoritas[i] << std::endl;
    }

    return 0;
}
