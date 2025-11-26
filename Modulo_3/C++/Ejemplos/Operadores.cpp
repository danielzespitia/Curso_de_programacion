// Ejemplos de operadores en C++
#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Operadores aritméticos
    int a = 10, b = 3;
    int suma = a + b;  // 13
    int resta = a - b; // 7
    int mult = a * b;  // 30
    int div = a / b;   // 3
    int resto = a % b; // 1

    // Operadores de incremento y decremento
    int x = 5;
    x++; // x = 6
    x--; // x = 5

    // Operadores de asignación
    int c = 10;
    c += 2; // c = 12
    c -= 3; // c = 9
    c *= 2; // c = 18
    c /= 3; // c = 6
    c %= 4; // c = 2

    // Operadores relacionales
    bool igual = (a == b);      // false
    bool distinto = (a != b);   // true
    bool mayor = (a > b);       // true
    bool menor = (a < b);       // false
    bool mayorIgual = (a >= b); // true
    bool menorIgual = (a <= b); // false

    // Operadores lógicos
    bool y = (true && false); // false
    bool o = (true || false); // true
    bool no = !true;          // false

    // Operadores bit a bit
    int b1 = a & b;  // AND bit a bit
    int b2 = a | b;  // OR bit a bit
    int b3 = a ^ b;  // XOR bit a bit
    int b4 = ~a;     // NOT bit a bit
    int b5 = a << 1; // Desplazamiento a la izquierda
    int b6 = a >> 1; // Desplazamiento a la derecha

    // Operador condicional (ternario)
    int edad = 18;
    string mensaje = (edad >= 18) ? "Mayor de edad" : "Menor de edad";

    // Operador de dirección y desreferenciación
    int var = 10;
    int *ptr = &var;  // operador & (dirección)
    int valor = *ptr; // operador * (desreferenciación)

    // Operador de acceso a miembros
    struct Persona
    {
        int edad;
    };
    Persona p;
    p.edad = 20; // operador punto
    Persona *q = &p;
    q->edad = 25; // operador flecha

    // Operador sizeof
    int tam = sizeof(int); // tamaño en bytes de int

    // Operador coma
    int d, e, f;
    d = (e = 3, f = e + 2); // e=3, f=5, d=5

    // Operador de conversión de tipo (cast)
    double pi = 3.14;
    int entero = (int)pi; // entero = 3

    // Mostrar algunos resultados
    cout << "Suma: " << suma << endl;
    cout << "Resto: " << resto << endl;
    cout << "Mayor: " << mayor << endl;
    cout << "Mensaje: " << mensaje << endl;
    cout << "Valor apuntado por ptr: " << valor << endl;
    cout << "p.edad: " << p.edad << ", q->edad: " << q->edad << endl;
    cout << "Tamaño de int: " << tam << endl;
    cout << "d: " << d << ", e: " << e << ", f: " << f << endl;
    cout << "Entero (cast de pi): " << entero << endl;

    return 0;
}