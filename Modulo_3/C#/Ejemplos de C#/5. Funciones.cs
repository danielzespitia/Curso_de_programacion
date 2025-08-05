// ==========================================================================================
// 5. FUNCIONES (MÉTODOS)
// ==========================================================================================
public class EjemploFunciones
{
    public static void ExplicarFunciones()
    {
        Console.WriteLine("\n\n--- 5. Funciones (o Métodos) ---");

        /*
         * CONCEPTO DE FUNCIÓN/MÉTODO:
         * Una función (en C#, comúnmente llamada "método" cuando está dentro de una clase)
         * es un bloque de código que realiza una tarea específica.
         * Permiten reutilizar código, organizar la lógica del programa y hacerlo más legible.
         *
         * Una función tiene una "firma" que define:
         * 1. Modificador de acceso (ej. 'public', 'private'): Quién puede llamarla.
         * 2. Tipo de retorno: El tipo de dato del valor que la función devuelve. Si no
         * devuelve nada, se usa la palabra clave 'void'.
         * 3. Nombre: Un nombre descriptivo para la función.
         * 4. Parámetros (opcional): Variables que la función recibe para trabajar con ellas.
        */

        // --- LLAMANDO A LAS FUNCIONES DE EJEMPLO ---

        // Llamada a una función que no devuelve nada ('void').
        SaludarUsuario("Maria");

        // Llamada a una función que devuelve un valor ('int').
        // Guardamos el resultado en una variable para usarlo después.
        int resultadoSuma = Sumar(15, 7);
        Console.WriteLine("El resultado de llamar a la función Sumar(15, 7) es: " + resultadoSuma);

        // Llamada a una función que devuelve una tupla (múltiples valores).
        var datosUsuario = ObtenerDatosUsuario();
        Console.WriteLine($"El usuario obtenido es {datosUsuario.Nombre} y tiene {datosUsuario.Edad} años.");
    }

    // --- DEFINICIÓN DE FUNCIONES DE EJEMPLO ---

    /// <summary>
    /// Esta es una función simple que no devuelve ningún valor (void).
    /// Recibe un parámetro de tipo string llamado 'nombre' y lo usa para imprimir un saludo.
    /// 'public' significa que puede ser llamada desde fuera de esta clase.
    /// 'static' significa que pertenece a la clase en sí, no a una instancia de la clase.
    /// </summary>
    /// <param name="nombre">El nombre de la persona a saludar.</param>
    public static void SaludarUsuario(string nombre)
    {
        Console.WriteLine($"\nLlamando a la función 'SaludarUsuario':");
        Console.WriteLine($"¡Hola, {nombre}! Bienvenido a la sección de funciones.");
    }

    /// <summary>
    /// Esta función recibe dos parámetros enteros ('a' y 'b') y devuelve un valor entero (int).
    /// La palabra clave 'return' se usa para especificar el valor que la función devolverá.
    /// </summary>
    /// <param name="a">El primer número a sumar.</param>
    /// <param name="b">El segundo número a sumar.</param>
    /// <returns>La suma de a y b.</returns>
    public static int Sumar(int a, int b)
    {
        int suma = a + b;
        return suma;
    }

    /// <summary>
    /// Esta función demuestra cómo devolver múltiples valores usando una tupla.
    /// El tipo de retorno es una tupla con dos elementos: un string y un int, con nombres.
    /// </summary>
    /// <returns>Una tupla que contiene el nombre y la edad de un usuario.</returns>
    public static (string Nombre, int Edad) ObtenerDatosUsuario()
    {
        Console.WriteLine("\nLlamando a la función 'ObtenerDatosUsuario' que devuelve una tupla:");
        string nombre = "David";
        int edad = 42;
        return (nombre, edad);
    }
}