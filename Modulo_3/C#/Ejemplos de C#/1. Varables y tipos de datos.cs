using System;
using System.Collections.Generic; // Necesario para usar Listas (List<T>)

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
            Console.WriteLine("--- Explorando los Fundamentos de C# ---");

            // Llamamos a los diferentes métodos que hemos creado para demostrar cada concepto.
            // Esto mantiene el código organizado y fácil de seguir.
            ExplicarVariables();
            ExplicarArrays();
            ExplicarListas();
            ExplicarTuplas();
            ExplicarFunciones();

            Console.WriteLine("\n--- Fin de la Demostración ---");
        }

        // ==========================================================================================
        // 1. VARIABLES Y TIPOS DE DATOS
        // ==========================================================================================
        public static void ExplicarVariables()
        {
            Console.WriteLine("\n\n--- 1. Variables y Tipos de Datos ---");

            /*
             * CONCEPTO DE VARIABLE:
             * Una variable es un espacio en la memoria del computador donde se almacena un valor.
             * Cada variable tiene un nombre único (identificador) y un tipo de dato que define
             * qué clase de valor puede guardar (números, texto, etc.) y cuánta memoria ocupa.
             * En C#, que es un lenguaje de tipado estático, debes declarar el tipo de la variable
             * antes de poder usarla.
             *
             * La sintaxis es: tipoDeDato nombreDeVariable = valorInicial;
            */

            // --- TIPOS DE DATOS NUMÉRICOS ---

            // 'int': Se usa para almacenar números enteros (sin decimales).
            // Ocupa 32 bits en memoria. Es el tipo más común para números enteros.
            // Rango: -2,147,483,648 a 2,147,483,647.
            int edad = 30;
            Console.WriteLine("Ejemplo de 'int' (edad): " + edad);

            // 'double': Se usa para números de punto flotante de doble precisión (con decimales).
            // Es el tipo por defecto para números con decimales en C#. Es muy preciso.
            // Ocupa 64 bits. Para asignar un valor, puedes usar el sufijo 'd' o ninguno.
            double alturaEnMetros = 1.75;
            Console.WriteLine("Ejemplo de 'double' (altura): " + alturaEnMetros);

            // 'float': También para números con decimales, pero de precisión simple.
            // Ocupa menos memoria que 'double' (32 bits), pero es menos preciso.
            // Se debe usar el sufijo 'f' al asignar el valor.
            float pesoEnKg = 68.5f;
            Console.WriteLine("Ejemplo de 'float' (peso): " + pesoEnKg);

            // 'decimal': Se usa para cálculos financieros y monetarios donde la precisión
            // es extremadamente importante y no se pueden permitir errores de redondeo.
            // Ocupa 128 bits. Se debe usar el sufijo 'm' (de "money").
            decimal precioProducto = 19.99m;
            Console.WriteLine("Ejemplo de 'decimal' (precio): " + precioProducto);


            // --- TIPO DE DATO PARA TEXTO ---

            // 'string': Se usa para almacenar secuencias de caracteres (texto).
            // El valor se escribe entre comillas dobles "".
            string nombreCompleto = "Ana Sofía Rojas";
            Console.WriteLine("Ejemplo de 'string' (nombre): " + nombreCompleto);

            // 'char': Se usa para almacenar un único carácter Unicode.
            // El valor se escribe entre comillas simples ''.
            char inicial = 'A';
            Console.WriteLine("Ejemplo de 'char' (inicial): " + inicial);


            // --- TIPO DE DATO LÓGICO ---

            // 'bool': Se usa para almacenar valores booleanos, es decir, verdadero o falso.
            // Solo puede tener dos valores: 'true' o 'false'.
            bool esEstudiante = true;
            Console.WriteLine("Ejemplo de 'bool' (es estudiante): " + esEstudiante);


            // --- INFERENCIA DE TIPOS CON 'var' ---
            /*
             * La palabra clave 'var' le dice al compilador que infiera (deduzca) el tipo de la
             * variable a partir del valor que se le asigna en el momento de la declaración.
             * Una vez que el tipo es asignado, no puede cambiarse. Es solo un atajo para no
             * tener que escribir el tipo explícitamente.
            */
            var mensaje = "Este es un mensaje inferido como string.";
            var cantidad = 100; // Inferido como int.
            Console.WriteLine("Ejemplo de 'var' (mensaje): " + mensaje);
            Console.WriteLine("El tipo de 'cantidad' inferido es: " + cantidad.GetType().Name);
        }
    }
}    

        
        

        
        
