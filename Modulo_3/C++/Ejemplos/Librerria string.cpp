// Incluimos la librería para poder usar la clase std::string.
#include <iostream>
#include <string> // Necesaria para std::string

int main() {
    // Creación de strings.
    std::string saludo = "Hola";
    std::string objetivo = "mundo";

    // Concatenación de strings con el operador '+'.
    std::string fraseCompleta = saludo + ", " + objetivo + "!";
    std::cout << "Frase completa: " << fraseCompleta << std::endl;

    // Obtener la longitud de un string.
    std::cout << "La longitud de la frase es: " << fraseCompleta.length() << " caracteres." << std::endl;

    // Acceder a un carácter específico usando el operador [].
    // Los índices empiezan en 0.
    std::cout << "El primer carácter es: " << fraseCompleta[0] << std::endl;
    std::cout << "El quinto carácter es: " << fraseCompleta[4] << std::endl;

    // Modificar un carácter.
    fraseCompleta[0] = 'h'; // Cambiamos 'H' por 'h'.
    std::cout << "Frase modificada: " << fraseCompleta << std::endl;

    // Buscar una subcadena dentro del string con find().
    // Devuelve la posición inicial de la subcadena o un valor especial (std::string::npos) si no la encuentra.
    size_t posicion = fraseCompleta.find("mundo");
    if (posicion != std::string::npos) {
        std::cout << "'mundo' se encontró en la posición: " << posicion << std::endl;
    } else {
        std::cout << "'mundo' no se encontró." << std::endl;
    }

    // Extraer una subcadena con substr(inicio, longitud).
    std::string sub = fraseCompleta.substr(6, 5); // Extrae "mundo"
    std::cout << "Subcadena extraída: " << sub << std::endl;

    return 0;
}