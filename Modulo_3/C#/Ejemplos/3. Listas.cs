// ==========================================================================================
        // 3. LISTAS (LIST<T>)
        // ==========================================================================================
        static void ExplicarListas()
        {
            Console.WriteLine("\n\n--- 3. Listas (List<T>) ---");

            /*
             * CONCEPTO DE LISTA:
             * Una lista (representada por la clase 'List<T>') es una colección de elementos del
             * mismo tipo, similar a un array, pero con una diferencia clave: su tamaño es DINÁMICO.
             * Puedes agregar o quitar elementos después de su creación, y la lista se ajustará
             * automáticamente.
             * Son extremadamente flexibles y son una de las colecciones más usadas en C#.
             * La 'T' en List<T> es un marcador de posición para el tipo de dato que contendrá
             * la lista (ej. List<int>, List<string>).
             *
             * Sintaxis: List<tipoDeDato> nombreDeLaLista = new List<tipoDeDato>();
            */

            // --- DECLARACIÓN Y MANIPULACIÓN ---

            // Crear una lista vacía de strings para almacenar nombres de frutas.
            List<string> listaDeFrutas = new List<string>();

           // Agregar elementos a la lista con el método .Add()
            Console.WriteLine("Agregando frutas a la lista...");
            
            listaDeFrutas.Add("Manzana");
            listaDeFrutas.Add("Banana");
            listaDeFrutas.Add("Naranja");
            listaDeFrutas.Add("Fresa");

            // La propiedad 'Count' nos da el número de elementos actual en la lista.
            Console.WriteLine("Ahora la lista tiene " + listaDeFrutas.Count + " frutas.");

            // Acceder a un elemento es igual que en los arrays, usando su índice.
            Console.WriteLine("La fruta en el índice 1 es: " + listaDeFrutas[1]);

            // Quitar un elemento de la lista con el método .Remove()
            Console.WriteLine("\nQuitando 'Banana' de la lista...");
            listaDeFrutas.Remove("Banana");
            Console.WriteLine("Ahora la lista tiene " + listaDeFrutas.Count + " frutas.");
            Console.WriteLine("La fruta en el índice 1 ahora es: " + listaDeFrutas[1]); // Ahora es "Naranja"

            // --- RECORRER UNA LISTA ---
            Console.WriteLine("\nRecorriendo la lista de frutas con 'foreach':");
            // La forma más común de recorrer una lista es con un bucle 'foreach'.
            foreach (string fruta in listaDeFrutas)
            {
                Console.WriteLine("- " + fruta);
            }
        }