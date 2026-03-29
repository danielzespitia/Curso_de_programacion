// Incluimos las librerías necesarias.
#include <iostream>
#include <vector> // Necesaria para std::vector

int main() {
    // Declaramos un vector que almacenará números enteros.
    // Inicialmente está vacío.
    std::vector<int> numeros;

    // Añadimos elementos al final del vector con push_back().
    numeros.push_back(10); // El vector ahora es {10}
    numeros.push_back(20); // El vector ahora es {10, 20}
    numeros.push_back(30); // El vector ahora es {10, 20, 30}

    // Obtenemos y mostramos el tamaño actual del vector.
    std::cout << "El vector tiene " << numeros.size() << " elementos." << std::endl;

    // Accedemos a los elementos. Se puede usar [] o at().
    // at() es más seguro porque lanza un error si el índice está fuera de rango.
    std::cout << "El primer elemento es: " << numeros[0] << std::endl;
    std::cout << "El segundo elemento es: " << numeros.at(1) << std::endl;

    // Iteramos (recorremos) el vector para mostrar todos sus elementos.
    std::cout << "Contenido del vector: ";
    for (int i = 0; i < numeros.size(); ++i) {
        std::cout << numeros[i] << " ";
    }
    std::cout << std::endl;

    // O usando un bucle "for-each" (más moderno y seguro).
    std::cout << "Contenido con for-each: ";
    for (int numero : numeros) {
        std::cout << numero << " ";
    }
    std::cout << std::endl;

    // Eliminamos el último elemento.
    numeros.pop_back(); // El vector ahora es {10, 20}
    std::cout << "Después de pop_back(), el último elemento es: " << numeros.back() << std::endl;

    // Verificamos si el vector está vacío.
    if (!numeros.empty()) {
        std::cout << "El vector no está vacío." << std::endl;
    }

    return 0;
}