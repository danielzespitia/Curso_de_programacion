// Usamos la directiva 'using' para importar el espacio de nombres 'System'.
// Esto nos da acceso a clases fundamentales como 'Console'.
using System;

// Definimos un espacio de nombres para organizar nuestro código.
namespace MiPrimeraApp
{
    // Creamos una clase llamada 'Program'. En C#, todo el código se ejecuta dentro de una clase.
    class Program
    {
        // Este es el método 'Main', el punto de entrada de nuestra aplicación.
        // El programa comienza a ejecutarse desde aquí.
        static void Main(string[] args)
        {
            // Usamos la clase 'Console' y su método 'WriteLine' para imprimir un texto en la consola.
            Console.WriteLine("¡Hola, Mundo desde C#!");

            // Espera a que el usuario presione una tecla antes de cerrar la consola.
            Console.ReadKey();
        }
    }
}