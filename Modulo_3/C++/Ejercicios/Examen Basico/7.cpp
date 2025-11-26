// Ejercicio 7: Funciones con Valor de Retorno
// Desarrolla un programa que contenga una función llamada calcularAreaRectangulo.
// 1. Declara (Prototipo) la función al inicio del programa.
// 2. La función debe recibir dos parámetros de tipo float: la base y la altura.
// 3. La función debe devolver el área calculada.
// 4. Desde la función main, solicita al usuario la base y la altura, llama a la función y muestra el resultado.

#include <iostream>

// 1. Declaración (Prototipo) de la función
float calcularAreaRectangulo(float base, float altura);

int main() {
    float baseUsuario, alturaUsuario;

    // Solicitar datos al usuario
    std::cout << "Introduce la base del rectangulo: ";
    std::cin >> baseUsuario;
    std::cout << "Introduce la altura del rectangulo: ";
    std::cin >> alturaUsuario;

    // Llamar a la función y guardar el valor devuelto en una variable
    float area = calcularAreaRectangulo(baseUsuario, alturaUsuario);

    // Mostrar el resultado
    std::cout << "El area del rectangulo es: " << area << std::endl;

    return 0;
}

// 2 y 3. Definición de la función
// Recibe dos parámetros float y devuelve un float
float calcularAreaRectangulo(float base, float altura) {
    // 3. Devolver el resultado del cálculo
    return base * altura;
}
