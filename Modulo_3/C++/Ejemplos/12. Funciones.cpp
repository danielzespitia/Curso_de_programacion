#include <iostream>
#include <string>

using namespace std;

string variableGlobal = "Soy accesible desde cualquier parte de este archivo.";

void saludar();

int sumar(int a, int b);

void pasoPorValor(int num);
void pasoPorReferencia(int &num);
void pasoPorReferenciaConstante(const string &texto);

void imprimir(int valor);
void imprimir(double valor);
void imprimir(const string &valor);

inline int duplicar(int x);



void saludar()
{
    string mensaje = "¡Hola desde la funcion 'saludar'!";
    cout << "   " << mensaje << endl;
    cout << "   Acceso a la variable global desde 'saludar': \"" << variableGlobal << "\"" << endl;
}

int sumar(int a, int b)
{
    int resultado = a + b;
    return resultado;
}

void pasoPorValor(int num)
{
    cout << "      -> Entrando a pasoPorValor. Valor recibido: " << num << endl;
    num = 99;
    cout << "      -> Saliendo de pasoPorValor. Valor modificado a: " << num << endl;
}

void pasoPorReferencia(int &num)
{
    cout << "      -> Entrando a pasoPorReferencia. Valor recibido: " << num << endl;
    num = 99;
    cout << "      -> Saliendo de pasoPorReferencia. Valor modificado a: " << num << endl;
}

void pasoPorReferenciaConstante(const string &texto)
{
    cout << "      -> Entrando a pasoPorReferenciaConstante." << endl;
    cout << "      -> El texto recibido es: \"" << texto << "\"" << endl;

    cout << "      -> Saliendo de pasoPorReferenciaConstante." << endl;
}

void imprimir(int valor)
{
    cout << "Version para int: " << valor << endl;
}

void imprimir(double valor)
{
    cout << "Version para double: " << valor << endl;
}

void imprimir(const string &valor)
{
    cout << "Version para string: \"" << valor << "\"" << endl;
}

inline int duplicar(int x)
{
    return x * 2;
}

int main()
{
    cout << "--- Inicio del programa en main() ---" << endl
         << endl;

    cout << "1. Llamando a la funcion 'saludar':" << endl;
    saludar();
    cout << endl;

    cout << "2. Usando una funcion con valor de retorno:" << endl;
    int resultadoSuma = sumar(15, 7);
    cout << "El resultado de sumar(15, 7) es: " << resultadoSuma << endl;

    cout << "El resultado de sumar(100, -50) es: " << sumar(100, -50) << endl
         << endl;

    cout << "3. Demostracion de paso de parametros:" << endl;
    int miNumero = 10;
    cout << "   Variable 'miNumero' antes de las llamadas: " << miNumero << endl;

    pasoPorValor(miNumero);
    cout << "   Variable 'miNumero' DESPUES de pasoPorValor: " << miNumero << " (sin cambios)" << endl;

    pasoPorReferencia(miNumero);
    cout << "   Variable 'miNumero' DESPUES de pasoPorReferencia: " << miNumero << " (¡cambio!)" << endl;

    string miTexto = "Este es un texto original.";
    cout << "\n   Llamando a pasoPorReferenciaConstante..." << endl;
    pasoPorReferenciaConstante(miTexto);
    cout << endl;

    double otroNumero = 5.5;
    cout << "   Ejemplo adicional: paso por referencia con double (modificando valor):" << endl;
    auto modificarDouble = [](double &n)
    {
        cout << "      -> Valor recibido: " << n << endl;
        n *= 3;
        cout << "      -> Valor modificado: " << n << endl;
    };
    modificarDouble(otroNumero);
    cout << "   Valor de 'otroNumero' despues de modificarDouble: " << otroNumero << endl
         << endl;

    cout << "4. Demostracion de sobrecarga de funciones:" << endl;
    cout << "   Llamando a imprimir(100): ";
    imprimir(100);

    cout << "   Llamando a imprimir(3.1416): ";
    imprimir(3.1416);

    cout << "   Llamando a imprimir(\"Hola sobrecarga\"): ";
    imprimir(string("Hola sobrecarga"));

    cout << "   Llamando a imprimir(\"123\"): ";
    imprimir(string("123"));
    cout << endl;

    cout << "5. Demostracion de funcion inline:" << endl;
    int valorOriginal = 25;
    int valorDuplicado = duplicar(valorOriginal);
    cout << "   El duplicado de " << valorOriginal << " es " << valorDuplicado << endl;

    cout << "   El duplicado de 7 es " << duplicar(7) << endl
         << endl;

    cout << "6. Demostracion de ambito de variables:" << endl;
    string variableLocal = "Solo soy visible dentro de main.";
    cout << "   Variable local de main: \"" << variableLocal << "\"" << endl;
    cout << "   Acceso a la variable global desde main: \"" << variableGlobal << "\"" << endl;

    string variableConfusa = "Soy la version LOCAL de la variable.";
    cout << "\n   Ejemplo de shadowing:" << endl;
    {
        string variableConfusa = "Soy la version del BLOQUE INTERNO.";
        cout << "      Dentro del bloque: " << variableConfusa << endl;
    }
    cout << "      Fuera del bloque: " << variableConfusa << endl;

    int valor = 5;
    cout << "\n   Ejemplo adicional de shadowing con variable global:" << endl;
    {
        int valor = 100;
        cout << "      Valor dentro del bloque: " << valor << endl;
    }
    cout << "      Valor fuera del bloque: " << valor << endl;

    cout << "\n--- Fin del programa en main() ---" << endl;
    return 0;
}
