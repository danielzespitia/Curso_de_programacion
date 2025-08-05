using System;

// Un namespace es un contenedor para clases y otros namespaces. Ayuda a organizar el código
// y a prevenir conflictos de nombres. Imagínalo como una carpeta para tus archivos de código.
namespace FundamentosDeCSharp
{
    // Una clase es una plantilla para crear objetos. Contiene datos (campos o propiedades)
    // y comportamientos (métodos). Todo el código ejecutable en C# debe estar dentro de una clase.
    class ExplicacionGeneral
    {
        // El método Main es el punto de entrada de una aplicación de consola en C#.
        // Cuando ejecutas el programa, el código dentro de Main es lo primero que se ejecuta.
        static void Main(string[] args)
        {
            Console.WriteLine("--- Explorando Bucles y Condicionales en C# ---");

            // Llamamos a los métodos que demuestran los conceptos de condicionales y bucles.
            ExplicarCondicionales();
            ExplicarBucles();

            Console.WriteLine("\n--- Fin de la Demostración ---");
        }

        // ==========================================================================================
        // 1. ESTRUCTURAS CONDICIONALES
        // ==========================================================================================
        public static void ExplicarCondicionales()
        {
            Console.WriteLine("\n\n--- 1. Estructuras Condicionales ---");

            /*
             * CONCEPTO DE CONDICIONAL:
             * Las estructuras condicionales permiten que un programa ejecute diferentes bloques de
             * código dependiendo de si una condición booleana (true o false) se cumple o no.
             * Son la base para que un programa pueda tomar decisiones.
            */

            // --- IF / ELSE IF / ELSE ---
            /*
             * 'if': Ejecuta un bloque de código SI la condición especificada es verdadera.
             * 'else if': Si la condición del 'if' es falsa, evalúa una nueva condición.
             * Puedes tener tantos 'else if' como necesites.
             * 'else': Se ejecuta si NINGUNA de las condiciones anteriores ('if' o 'else if') fue verdadera.
            */
            Console.WriteLine("\n--- Ejemplo con if / else if / else ---");
            int hora = 14;
            Console.WriteLine($"Si la hora actual es {hora}:");

            if (hora < 12)
            {
                Console.WriteLine("¡Buenos días!");
            }
            else if (hora < 18)
            {
                Console.WriteLine("¡Buenas tardes!");
            }
            else
            {
                Console.WriteLine("¡Buenas noches!");
            }

            // --- SWITCH ---
            /*
             * La instrucción 'switch' es una alternativa al 'if-else if-else' que es más legible
             * cuando necesitas comparar una sola variable contra una serie de valores constantes.
             * 'case': Define un valor específico a comparar.
             * 'break': Es crucial. Termina la ejecución del switch. Sin él, el código continuaría
             * ejecutándose en los siguientes 'case' (fall-through).
             * 'default': Es opcional y actúa como el 'else'. Se ejecuta si ninguno de los 'case' coincide.
            */
            Console.WriteLine("\n--- Ejemplo con switch ---");
            int diaNumero = 3;
            Console.WriteLine($"Evaluando el día número {diaNumero}:");

            switch (diaNumero)
            {
                case 1:
                    Console.WriteLine("Es Lunes.");
                    break;
                case 2:
                    Console.WriteLine("Es Martes.");
                    break;
                case 3:
                    Console.WriteLine("Es Miércoles.");
                    break;
                case 4:
                    Console.WriteLine("Es Jueves.");
                    break;
                case 5:
                    Console.WriteLine("Es Viernes.");
                    break;
                case 6:
                case 7: // Se pueden agrupar casos
                    Console.WriteLine("Es fin de semana.");
                    break;
                default:
                    Console.WriteLine("Ese número de día no es válido.");
                    break;
            }
        }

        // ==========================================================================================
        // 2. BUCLES (LOOPS)
        // ==========================================================================================
        public static void ExplicarBucles()
        {
            Console.WriteLine("\n\n--- 2. Bucles (Loops) ---");
            /*
             * CONCEPTO DE BUCLE:
             * Un bucle es una estructura de control que permite repetir un bloque de código
             * múltiples veces. Son esenciales para tareas repetitivas, como recorrer colecciones
             * de datos o ejecutar una acción hasta que se cumpla una condición.
            */

            // --- BUCLE FOR ---
            /*
             * El bucle 'for' es ideal cuando sabes de antemano cuántas veces quieres que se repita
             * el bloque de código.
             * Consta de tres partes:
             * 1. Inicializador: Se ejecuta una sola vez al principio (ej. 'int i = 0').
             * 2. Condición: Se evalúa antes de cada iteración. Si es 'true', el bucle continúa.
             * 3. Iterador: Se ejecuta al final de cada iteración (ej. 'i++').
            */
            Console.WriteLine("\n--- Ejemplo de bucle for (contando hasta 5) ---");
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine("El contador 'for' está en: " + i);
            }

            // --- BUCLE WHILE ---
            /*
             * El bucle 'while' repite un bloque de código MIENTRAS una condición especificada
             * sea verdadera. La condición se comprueba ANTES de cada iteración.
             * Es útil cuando no sabes cuántas iteraciones se necesitarán.
            */
            Console.WriteLine("\n--- Ejemplo de bucle while ---");
            int contadorWhile = 0;
            while (contadorWhile < 3)
            {
                Console.WriteLine("El contador 'while' está en: " + contadorWhile);
                contadorWhile++; // Es crucial modificar la variable de la condición dentro del bucle para evitar un bucle infinito.
            }

            // --- BUCLE DO-WHILE ---
            /*
             * El bucle 'do-while' es similar al 'while', pero con una diferencia clave:
             * el bloque de código se ejecuta AL MENOS UNA VEZ, porque la condición se
             * evalúa DESPUÉS de la primera iteración.
            */
            Console.WriteLine("\n--- Ejemplo de bucle do-while ---");
            int contadorDo = 5;
            do
            {
                Console.WriteLine("El contador 'do-while' se ejecuta al menos una vez. Valor: " + contadorDo);
                contadorDo++;
            } while (contadorDo < 3); // La condición (5 < 3) es falsa, pero el bloque ya se ejecutó una vez.
        }
    }
}
