// ==========================================================================================
// 2. ARRAYS (ARREGLOS)
// ==========================================================================================
using System;

namespace FundamentosDeCSharp
{
    public class Program
    {
        // Método para explicar arrays
        public static void ExplicarArrays()
        {
            Console.WriteLine("\n\n--- 2. Arrays (Arreglos) ---");

            /*
             * CONCEPTO DE ARRAY:
             * Un array es una colección de elementos del MISMO TIPO, almacenados en una secuencia
             * contigua de memoria. Tienen un tamaño fijo que se define en su creación y no puede
             * cambiar.
             * Son útiles cuando sabes exactamente cuántos elementos necesitas almacenar.
             * El acceso a los elementos es muy rápido porque se hace a través de un índice
             * numérico que empieza en 0.
             *
    // (El contenido de explicación y ejemplos fue movido dentro del método ExplicarArrays)
        /*
         * CONCEPTO DE ARRAY:
         * Un array es una colección de elementos del MISMO TIPO, almacenados en una secuencia
         * contigua de memoria. Tienen un tamaño fijo que se define en su creación y no puede
         * cambiar.
         * Son útiles cuando sabes exactamente cuántos elementos necesitas almacenar.
         * El acceso a los elementos es muy rápido porque se hace a través de un índice
         * numérico que empieza en 0.
         *
         * Sintaxis: tipoDeDato[] nombreDelArray = new tipoDeDato[tamaño];
        */

            // --- DECLARACIÓN E INICIALIZACIÓN ---

            // Ejemplo 1: Crear un array de 5 enteros. Inicialmente, todos sus valores son 0.
            int[] calificaciones = new int[5];

            // Asignar valores a los elementos del array usando su índice.
            // El primer elemento está en el índice 0, el segundo en el 1, y así sucesivamente.
            calificaciones[0] = 10;
            calificaciones[1] = 8;
            calificaciones[2] = 9;
            calificaciones[3] = 7;
            calificaciones[4] = 10;
            // Intentar acceder a calificaciones[5] produciría un error (IndexOutOfRangeException).

            Console.WriteLine("El valor en el índice 2 del array 'calificaciones' es: " + calificaciones[2]);

            // Ejemplo 2: Declarar e inicializar un array con valores al mismo tiempo.
            // El compilador deduce el tamaño del array (en este caso, 4).
            string[] diasDeLaSemana = { "Lunes", "Martes", "Miércoles", "Jueves" };
            Console.WriteLine("El primer día del array 'diasDeLaSemana' es: " + diasDeLaSemana[0]);

            // --- RECORRER UN ARRAY ---
            Console.WriteLine("\nRecorriendo el array 'diasDeLaSemana' con un bucle 'for':");
            // Se puede usar un bucle 'for' para iterar sobre cada elemento.
            // La propiedad 'Length' nos da el tamaño total del array.
            for (int i = 0; i < diasDeLaSemana.Length; i++)
            {
                Console.WriteLine("Índice " + i + ": " + diasDeLaSemana[i]);
            }

            Console.WriteLine("\nRecorriendo el array 'calificaciones' con un bucle 'foreach':");
            // El bucle 'foreach' es una forma más simple y legible de recorrer una colección
            // cuando no necesitas el índice.
            foreach (int calificacion in calificaciones)
            {
                Console.WriteLine("Calificación: " + calificacion);
            }
            Console.WriteLine("\nRecorriendo el array 'diasDeLaSemana' con un bucle 'foreach':");
        }
    }
}
