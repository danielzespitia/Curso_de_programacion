#include <iostream>

// --- Definición de la función ---
// Esta función es de tipo 'void', por lo que no devuelve ningún valor.
// Tampoco tiene parámetros (paréntesis vacíos), ya que su tarea es siempre la misma: mostrar un menú.
void mostrarMenu() {
    std::cout << "===== MENÚ PRINCIPAL =====" << std::endl;
    std::cout << "1. Iniciar juego" << std::endl;
    std::cout << "2. Ver puntuaciones" << std::endl;
    std::cout << "3. Salir" << std::endl;
    std::cout << "========================" << std::endl;
}

int main() {
    // --- Llamada a la función ---
    // Para ejecutar el código dentro de la función, simplemente escribimos su nombre seguido de paréntesis.
    std::cout << "Bienvenido al programa." << std::endl;
    mostrarMenu(); // El programa salta a la función, la ejecuta, y luego continúa desde aquí.

    std::cout << "Por favor, elija una opción." << std::endl;

    return 0;
}