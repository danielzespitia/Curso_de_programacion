// ==========================================================================================
        // 4. TUPLAS
        // ==========================================================================================
        class TuplasEjemplo
        {
            public static void ExplicarTuplas()
            {
                Console.WriteLine("\n\n--- 4. Tuplas ---");

                /*
                 * CONCEPTO DE TUPLA:
                 * Una tupla es una estructura de datos que permite agrupar un número fijo de elementos
                 * de DIFERENTES TIPOS en un solo objeto. Son una forma ligera y sencilla de agrupar
                 * datos sin tener que crear una clase o una estructura completa.
                 * Son muy útiles para devolver múltiples valores desde una función.
                 * Son inmutables por defecto, lo que significa que una vez creadas, sus valores
                 * no se pueden cambiar directamente (aunque se puede reasignar la tupla entera).
                */

                // --- CREACIÓN Y ACCESO A TUPLAS ---

                // Ejemplo 1: Crear una tupla sin nombres de elementos.
                // Los elementos se acceden con Item1, Item2, etc.
                (string, int, double) producto = ("Laptop Gamer", 1, 1200.50);
                Console.WriteLine("Accediendo a tupla sin nombres:");
                Console.WriteLine("Producto: " + producto.Item1);
                Console.WriteLine("Cantidad: " + producto.Item2);
                Console.WriteLine("Precio: " + producto.Item3);

                // Ejemplo 2: Crear una tupla con nombres de elementos (forma recomendada).
                // Esto hace el código mucho más legible.
                (string Nombre, string Apellido, int Edad) persona = ("Carlos", "Pérez", 25);
                Console.WriteLine("\nAccediendo a tupla con nombres:");
                Console.WriteLine("Nombre: " + persona.Nombre);
                Console.WriteLine("Apellido: " + persona.Apellido);
                Console.WriteLine("Edad: " + persona.Edad);

                // Las tuplas también se pueden usar como se ve en la sección de Funciones,
                // para devolver múltiples valores de forma limpia.
            }
        }
