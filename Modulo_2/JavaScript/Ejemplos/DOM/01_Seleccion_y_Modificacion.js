// 1. Selección de elementos

// Por ID (Método antiguo pero rápido)
const titulo = document.getElementById('titulo-principal');
console.log('Elemento por ID:', titulo);

// Por Selector CSS (Método moderno y versátil)
// Selecciona el primer elemento que coincida
const primerParrafo = document.querySelector('.texto');
console.log('Primer elemento .texto:', primerParrafo);

// Selecciona TODOS los elementos que coincidan
const todosLosParrafos = document.querySelectorAll('.texto');
console.log('Todos los elementos .texto:', todosLosParrafos);

// 2. Modificación de contenido

// Cambiar texto plano
titulo.textContent = 'DOM en JavaScript (Modificado)';

// Cambiar HTML interno (Cuidado con XSS si el contenido viene del usuario)
const contenedor = document.getElementById('contenedor-secundario');
// contenedor.innerHTML = '<p>He reemplazado todo el contenido de este div.</p>'; 

// 3. Modificación de estilos

// Accediendo a la propiedad style
primerParrafo.style.color = 'red';
primerParrafo.style.fontSize = '18px';
primerParrafo.style.backgroundColor = '#e0e0e0';

// 4. Modificación de atributos

const enlace = document.querySelector('#mi-enlace');

// Obtener valor
console.log('Href original:', enlace.getAttribute('href'));

// Cambiar valor
enlace.setAttribute('href', 'https://developer.mozilla.org');
enlace.textContent = 'Ir a MDN Web Docs';
enlace.setAttribute('target', '_blank'); // Abrir en nueva pestaña

// 5. Manipulación de Clases (ClassList)

// Agregar clase
titulo.classList.add('destacado');

// Verificar si tiene clase
if (titulo.classList.contains('destacado')) {
    console.log('El título está destacado');
}

// Quitar clase (descomentar para probar)
// titulo.classList.remove('destacado');
