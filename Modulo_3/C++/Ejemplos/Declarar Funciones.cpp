#include <iostream> // Se incluye para poder usar std::cout y std::string
#include <string>

// A continuación, se muestra el código C++ que explica y demuestra la anatomía de una función.

/*
 * =================================================================================
 * -- ANATOMÍA DE UNA FUNCIÓN --
 * =================================================================================
 *
 * Toda función en C++ tiene la siguiente estructura básica:
 *
 * tipo_de_retorno  nombre_de_la_funcion(tipo_parametro1 nombre_parametro1, tipo_parametro2 nombre_parametro2) {
 * // Cuerpo de la función:
 * // Aquí va el conjunto de instrucciones que realiza la función.
 *
 * return valor; // Se usa si la función devuelve un valor.
 * }
 *
 * --- EXPLICACIÓN DE CADA PARTE ---
 *
 * 1. tipo_de_retorno:
 * Es el tipo de dato del valor que la función devuelve o "retorna" cuando termina su ejecución.
 * Si la función no devuelve nada, se usa la palabra clave 'void'.
 *
 * 2. nombre_de_la_funcion:
 * Es el nombre que le das a la función. Debe ser descriptivo de la tarea que realiza.
 * Por ejemplo: calcularSuma, imprimirReporte, etc.
 *
 * 3. parámetros (entre paréntesis):
 * Son los valores o variables que la función recibe como entrada para trabajar con ellos.
 * Cada parámetro se especifica con su tipo y un nombre.
 * Una función puede no tener parámetros, en cuyo caso los paréntesis se dejan vacíos ().
 *
 * 4. cuerpo de la función (entre llaves {}):
 * Contiene el código (las instrucciones) que se ejecutará cuando la función sea "llamada" o "invocada".
 *
 * 5. return valor;:
 * Es la instrucción que finaliza la función y devuelve un 'valor' al lugar desde donde fue llamada.
 * La ejecución de la función termina inmediatamente en la línea del 'return'.
 * Si el tipo de retorno es 'void', no es necesario incluir un 'return' o se puede usar 'return;' sin un valor.
 *
 */

// --- EJEMPLO 1: Función con retorno y parámetros ---
// Esta función toma dos enteros y devuelve su suma.

// tipo_de_retorno -> int (devuelve un número entero)
// nombre_de_la_funcion -> sumar
// parámetros -> (int numero1, int numero2)
int sumar(int numero1, int numero2) {
    // -- Cuerpo de la función --
    int resultado = numero1 + numero2; // Realiza la operación de suma.

    // La instrucción 'return' devuelve el valor de 'resultado'.
    return resultado;
}


// --- EJEMPLO 2: Función sin retorno (void) y con un parámetro ---
// Esta función recibe un nombre y lo imprime en un saludo. No devuelve nada.

// tipo_de_retorno -> void (no devuelve ningún valor)
// nombre_de_la_funcion -> saludar
// parámetros -> (std::string nombre)
void saludar(std::string nombre) {
    // -- Cuerpo de la función --
    std::cout << "¡Hola, " << nombre << "! Bienvenido al programa." << std::endl;

    // Como es 'void', no es necesario un 'return'. La función termina al llegar a la llave de cierre.
}


// --- EJEMPLO 3: Función sin retorno (void) y sin parámetros ---
// Esta función simplemente muestra un menú. No necesita datos de entrada ni devuelve nada.

// tipo_de_retorno -> void
// nombre_de_la_funcion -> mostrarMenu
// parámetros -> () (paréntesis vacíos)
void mostrarMenu() {
    // -- Cuerpo de la función --
    std::cout << "\n--- MENÚ ---\n";
    std::cout << "1. Iniciar\n";
    std::cout << "2. Salir\n";
    // No hay 'return'
}


// --- FUNCIÓN PRINCIPAL 'main' ---
// Todo programa en C++ comienza su ejecución aquí.
// Desde 'main' llamaremos a las otras funciones que hemos creado.

int main() {
    // Llamada a la función 'saludar' y le pasamos "Ana" como argumento del parámetro 'nombre'.
    saludar("Ana");

    // Llamada a la función 'sumar'.
    // Le pasamos 5 y 3 como argumentos. El valor que devuelve (8) se guarda en la variable 'resultadoSuma'.
    int resultadoSuma = sumar(5, 3);
    std::cout << "El resultado de la suma es: " << resultadoSuma << std::endl;

    // Llamada a la función 'mostrarMenu'. Como no tiene parámetros, los paréntesis van vacíos.
    mostrarMenu();

    return 0; // La función 'main' devuelve 0 para indicar que el programa terminó sin errores.
}