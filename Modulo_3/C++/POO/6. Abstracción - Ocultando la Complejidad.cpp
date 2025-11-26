// La abstracción consiste en mostrar solo la información esencial de un objeto al mundo exterior, ocultando los detalles complejos de su implementación. En C++, la abstracción se logra a través de:
//
// Encapsulamiento: Como ya vimos, oculta el estado interno.
//
// Clases Abstractas: Son clases que no pueden ser instanciadas (no se pueden crear objetos de ellas). Sirven como un contrato para las clases derivadas. Una clase se vuelve abstracta si tiene al menos una función virtual pura (una función virtual que se iguala a 0, como en el ejemplo de Animal).
//
// La clase Animal del ejemplo anterior es una clase abstracta porque te obliga a implementar el método hacerSonido en cualquier clase que herede de ella. No puedes crear un Animal genérico, debes crear un Perro o un Gato.
//
// Conceptos Adicionales Importantes
// Constructores y Destructores
// Constructor: Es un método especial que se llama automáticamente cuando se crea un objeto. Se usa para inicializar los atributos del objeto. Tiene el mismo nombre que la clase y no tiene tipo de retorno.
//

#include <iostream>

// Ejemplo de clase con constructor
class Rectangulo {
private:
    double base;
    double altura;
public:
    // Constructor
    Rectangulo(double b, double a) {
        base = b;
        altura = a;
        std::cout << "Rectángulo creado." << std::endl;
    }
};
// Destructor: Es un método especial que se llama automáticamente cuando un objeto es destruido (por ejemplo, al salir del ámbito donde fue creado). Se usa para liberar recursos (como memoria dinámica). Su nombre es el de la clase precedido por una tilde (~).

class MiClase {
public:
    // Destructor
    ~MiClase() {
        std::cout << "Objeto destruido." << std::endl;
    }
};
// Sobrecarga (Overloading)
// La sobrecarga permite tener múltiples funciones con el mismo nombre pero con diferentes parámetros (ya sea en número o en tipo). Esto también aplica a los constructores y a los operadores.
//
// Sobrecarga de Funciones:
//

void imprimir(int i) {
    std::cout << "Entero: " << i << std::endl;
}
void imprimir(double f) {
    std::cout << "Flotante: " << f << std::endl;
}
// Sobrecarga de Operadores: Permite redefinir el comportamiento de los operadores de C++ (como +, -, ==, <<) para tus propias clases.
//

class Punto {
public:
    int x, y;
    Punto(int x = 0, int y = 0) : x(x), y(y) {}

    // Sobrecarga del operador +
    Punto operator+(const Punto& p) {
        Punto temp;
        temp.x = x + p.x;
        temp.y = y + p.y;
        return temp;
    }
};
// Este recorrido te ofrece una base sólida y detallada de la Programación Orientada a Objetos en C++. La clave es practicar, crear tus propias clases, experimentar con la herencia y el polimorfismo para interiorizar cómo estos conceptos interactúan y te permiten escribir código más limpio, modular y reutilizable. ¡Feliz codificación!

int main() {
    // Prueba de constructor
    Rectangulo r(3, 4);

    // Prueba de sobrecarga de funciones
    imprimir(5);
    imprimir(3.14);

    // Prueba de sobrecarga de operadores
    Punto p1(1, 2), p2(3, 4);
    Punto p3 = p1 + p2;
    std::cout << "Punto suma: (" << p3.x << ", " << p3.y << ")" << std::endl;

    // Prueba de destructor (se llamará automáticamente al salir de main)
    MiClase obj;

    return 0;
}