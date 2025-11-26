// ----------------------------------------------------------------------------
// TEMA 3: FUNCIONES EN C++ (EXPLICACIÓN DETALLADA Y EJEMPLOS)
// ----------------------------------------------------------------------------
// Una función es un bloque de código que realiza una tarea específica.
// Nos permite organizar el código en partes reutilizables, lo que hace que
// nuestros programas sean más modulares, fáciles de leer y de mantener.
// ----------------------------------------------------------------------------

#include <iostream>
#include <string>

using namespace std;

// ----------------------------------------------------------------------------
// VARIABLES GLOBALES Y ÁMBITO
// ----------------------------------------------------------------------------
string variableGlobal = "Soy accesible desde cualquier parte de este archivo.";

// ----------------------------------------------------------------------------
// 1. PROTOTIPOS DE FUNCIONES
// ----------------------------------------------------------------------------
// Los prototipos permiten declarar funciones antes de definirlas.
// Así, el compilador sabe que existen y puede usarlas en cualquier orden.

// Función sin parámetros ni valor de retorno.
void saludar();

// Función que suma dos enteros y devuelve el resultado.
int sumar(int a, int b);

// Funciones para demostrar paso de parámetros.
void pasoPorValor(int num);
void pasoPorReferencia(int& num);
void pasoPorReferenciaConstante(const string& texto);

// Funciones sobrecargadas (mismo nombre, diferentes parámetros).
void imprimir(int valor);
void imprimir(double valor);
void imprimir(const string& valor);

// Función inline (sugerencia para el compilador).
inline int duplicar(int x);

// ----------------------------------------------------------------------------
// 2. DEFINICIÓN DE FUNCIONES
// ----------------------------------------------------------------------------

// 2.1. Función sin parámetros ni valor de retorno.
void saludar() {
    string mensaje = "¡Hola desde la funcion 'saludar'!";
    cout << "   " << mensaje << endl;
    cout << "   Acceso a la variable global desde 'saludar': \"" << variableGlobal << "\"" << endl;
}

// 2.2. Función que suma dos enteros.
int sumar(int a, int b) {
    int resultado = a + b;
    return resultado;
}

// 2.3. Paso de parámetros por valor.
void pasoPorValor(int num) {
    cout << "      -> Entrando a pasoPorValor. Valor recibido: " << num << endl;
    num = 99; // Solo modifica la copia local.
    cout << "      -> Saliendo de pasoPorValor. Valor modificado a: " << num << endl;
}

// 2.4. Paso de parámetros por referencia.
void pasoPorReferencia(int& num) {
    cout << "      -> Entrando a pasoPorReferencia. Valor recibido: " << num << endl;
    num = 99; // Modifica la variable original.
    cout << "      -> Saliendo de pasoPorReferencia. Valor modificado a: " << num << endl;
}

// 2.5. Paso por referencia constante (no permite modificar el argumento).
void pasoPorReferenciaConstante(const string& texto) {
    cout << "      -> Entrando a pasoPorReferenciaConstante." << endl;
    cout << "      -> El texto recibido es: \"" << texto << "\"" << endl;
    // texto = "Intento de modificar"; // ¡ERROR! No se puede modificar.
    cout << "      -> Saliendo de pasoPorReferenciaConstante." << endl;
}

// 2.6. Sobrecarga de funciones: mismo nombre, diferentes parámetros.
void imprimir(int valor) {
    cout << "Version para int: " << valor << endl;
}

void imprimir(double valor) {
    cout << "Version para double: " << valor << endl;
}

void imprimir(const string& valor) {
    cout << "Version para string: \"" << valor << "\"" << endl;
}

// 2.7. Función inline: sugerencia para copiar el código en vez de llamar.
inline int duplicar(int x) {
    return x * 2;
}

// ----------------------------------------------------------------------------
// 3. FUNCIÓN PRINCIPAL: main()
// ----------------------------------------------------------------------------
int main() {
    cout << "--- Inicio del programa en main() ---" << endl << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 1: LLAMADA A UNA FUNCIÓN SIMPLE
    cout << "1. Llamando a la funcion 'saludar':" << endl;
    saludar();
    cout << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 2: FUNCIÓN CON VALOR DE RETORNO
    cout << "2. Usando una funcion con valor de retorno:" << endl;
    int resultadoSuma = sumar(15, 7);
    cout << "El resultado de sumar(15, 7) es: " << resultadoSuma << endl;
    // Ejemplo adicional:
    cout << "El resultado de sumar(100, -50) es: " << sumar(100, -50) << endl << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 3: PASO DE PARÁMETROS (POR VALOR Y POR REFERENCIA)
    cout << "3. Demostracion de paso de parametros:" << endl;
    int miNumero = 10;
    cout << "   Variable 'miNumero' antes de las llamadas: " << miNumero << endl;

    // a) Paso por valor
    pasoPorValor(miNumero);
    cout << "   Variable 'miNumero' DESPUES de pasoPorValor: " << miNumero << " (sin cambios)" << endl;

    // b) Paso por referencia
    pasoPorReferencia(miNumero);
    cout << "   Variable 'miNumero' DESPUES de pasoPorReferencia: " << miNumero << " (¡cambio!)" << endl;

    // c) Paso por referencia constante
    string miTexto = "Este es un texto original.";
    cout << "\n   Llamando a pasoPorReferenciaConstante..." << endl;
    pasoPorReferenciaConstante(miTexto);
    cout << endl;

    // Ejemplo adicional: paso por referencia con varios tipos
    double otroNumero = 5.5;
    cout << "   Ejemplo adicional: paso por referencia con double (modificando valor):" << endl;
    auto modificarDouble = [](double& n) {
        cout << "      -> Valor recibido: " << n << endl;
        n *= 3;
        cout << "      -> Valor modificado: " << n << endl;
    };
    modificarDouble(otroNumero);
    cout << "   Valor de 'otroNumero' despues de modificarDouble: " << otroNumero << endl << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 4: SOBRECARGA DE FUNCIONES
    cout << "4. Demostracion de sobrecarga de funciones:" << endl;
    cout << "   Llamando a imprimir(100): ";
    imprimir(100);

    cout << "   Llamando a imprimir(3.1416): ";
    imprimir(3.1416);

    cout << "   Llamando a imprimir(\"Hola sobrecarga\"): ";
    imprimir(string("Hola sobrecarga")); // Se recomienda pasar string explícito

    // Ejemplo adicional:
    cout << "   Llamando a imprimir(\"123\"): ";
    imprimir(string("123")); // Llama a la versión de string
    cout << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 5: FUNCIONES INLINE
    cout << "5. Demostracion de funcion inline:" << endl;
    int valorOriginal = 25;
    int valorDuplicado = duplicar(valorOriginal);
    cout << "   El duplicado de " << valorOriginal << " es " << valorDuplicado << endl;
    // Ejemplo adicional:
    cout << "   El duplicado de 7 es " << duplicar(7) << endl << endl;

    // ------------------------------------------------------------------------
    // EJEMPLO 6: ÁMBITO DE LAS VARIABLES
    cout << "6. Demostracion de ambito de variables:" << endl;
    string variableLocal = "Solo soy visible dentro de main.";
    cout << "   Variable local de main: \"" << variableLocal << "\"" << endl;
    cout << "   Acceso a la variable global desde main: \"" << variableGlobal << "\"" << endl;

    // Shadowing (sombreado) de variables
    string variableConfusa = "Soy la version LOCAL de la variable.";
    cout << "\n   Ejemplo de shadowing:" << endl;
    { // Bloque interno
        string variableConfusa = "Soy la version del BLOQUE INTERNO.";
        cout << "      Dentro del bloque: " << variableConfusa << endl;
    }
    cout << "      Fuera del bloque: " << variableConfusa << endl;

    // Ejemplo adicional: variable global y local con el mismo nombre
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
