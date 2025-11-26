// Ejercicio 8: Paso por Valor vs. Paso por Referencia
// Crea un programa que demuestre la diferencia entre el paso por valor y el paso por referencia.
// 1. Define una función void llamada modificarPorValor que reciba un entero por valor.
// 2. Define otra función void llamada modificarPorReferencia que reciba un entero por referencia.
// 3. En main, declara una variable, llámala, imprímela, llama a ambas funciones y observa la diferencia.

#include <iostream>

// 1. Función que recibe un parámetro por valor
// Se crea una COPIA de la variable original. Los cambios solo afectan a la copia.
void modificarPorValor(int val) {
    std::cout << "  (Dentro de 'modificarPorValor') El valor recibido es: " << val << std::endl;
    val += 10;
    std::cout << "  (Dentro de 'modificarPorValor') El valor ahora es: " << val << std::endl;
}

// 2. Función que recibe un parámetro por referencia (usando '&')
// Se pasa una REFERENCIA a la variable original. Los cambios afectan a la variable original.
void modificarPorReferencia(int &ref) {
    std::cout << "  (Dentro de 'modificarPorReferencia') El valor recibido es: " << ref << std::endl;
    ref += 10;
    std::cout << "  (Dentro de 'modificarPorReferencia') El valor ahora es: " << ref << std::endl;
}

int main() {
    int numero = 20;

    std::cout << "--- Demostracion de Paso por Valor ---" << std::endl;
    std::cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << std::endl;
    modificarPorValor(numero);
    std::cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (SIN CAMBIOS)" << std::endl;
    
    std::cout << "\n--- Demostracion de Paso por Referencia ---" << std::endl;
    std::cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << std::endl;
    modificarPorReferencia(numero);
    std::cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (¡CAMBIO!)" << std::endl;

    return 0;
}
