const lista = document.getElementById('lista-tareas');
const btnAgregar = document.getElementById('btn-agregar');
const btnEliminar = document.getElementById('btn-eliminar-ultima');

let contador = 3;

// Función para agregar un elemento
btnAgregar.addEventListener('click', () => {
    // 1. Crear el elemento (todavía no está en el DOM, está en memoria)
    const nuevaTarea = document.createElement('li');
    
    // 2. Configurar el elemento
    nuevaTarea.textContent = `Tarea nueva ${contador}`;
    nuevaTarea.style.color = 'green';
    
    // 3. Insertar en el DOM
    // appendChild lo agrega al final de la lista
    lista.appendChild(nuevaTarea);
    
    contador++;
});

// Función para eliminar el último elemento
btnEliminar.addEventListener('click', () => {
    // Verificar si hay hijos
    if (lista.lastElementChild) {
        // Opción 1: Eliminar desde el padre
        lista.removeChild(lista.lastElementChild);
        
        // Opción 2: El elemento se elimina a sí mismo (más moderno)
        // lista.lastElementChild.remove();
    } else {
        alert('No hay más tareas para eliminar');
    }
});

// Ejemplo avanzado: Insertar antes de un elemento específico
// Vamos a insertar un título antes de la lista dinámicamente
const tituloLista = document.createElement('h3');
tituloLista.textContent = 'Mis Pendientes:';

// insertBefore(nuevoNodo, nodoReferencia)
// document.body es el padre, lista es la referencia
document.body.insertBefore(tituloLista, lista);
