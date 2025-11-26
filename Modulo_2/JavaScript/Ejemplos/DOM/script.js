// Esperamos a que todo el contenido del DOM esté cargado antes de ejecutar nuestro script.
// Esta es una buena práctica para asegurar que todos los elementos HTML existen cuando intentamos seleccionarlos.
document.addEventListener('DOMContentLoaded', () => {

    // ===================================================================================
    // PARTE 1: SELECCIÓN DE ELEMENTOS Y NAVEGACIÓN
    // Aquí demostramos las diferentes formas de "agarrar" elementos del HTML.
    // ===================================================================================

    const runSelectionBtn = document.getElementById('run-selection-btn');

    runSelectionBtn.addEventListener('click', () => {
        console.log('--- INICIANDO SELECCIÓN Y NAVEGACIÓN ---');

        // 1.1: Seleccionar por ID (el más rápido y específico)
        // Devuelve un único elemento.
        const mainTitle = document.getElementById('main-title');
        mainTitle.style.color = '#cc33ff'; // Cambiamos el color para ver el efecto
        console.log('Elemento por ID:', mainTitle);

        // 1.2: Seleccionar por Nombre de Clase
        // Devuelve una HTMLCollection (parecida a un array) de todos los elementos con esa clase.
        const highlightedItems = document.getElementsByClassName('highlight-item');
        console.log('Elementos por Clase:', highlightedItems);
        // Para manipularlos, debemos iterar sobre la colección.
        for (let item of highlightedItems) {
            item.style.backgroundColor = '#cc33ff';
        }

        // 1.3: Seleccionar por Nombre de Etiqueta (Tag)
        // Devuelve una HTMLCollection de todos los elementos con esa etiqueta.
        const allParagraphs = document.getElementsByTagName('p');
        console.log('Elementos por Etiqueta (párrafos):', allParagraphs);

        // 1.4: Métodos Modernos con Selectores CSS (muy potentes)
        // querySelector: Devuelve el *primer* elemento que coincide con el selector CSS.
        const subtitle = document.querySelector('.subtitle');
        console.log('Elemento con querySelector (.subtitle):', subtitle);
        
        const firstHighlightedItem = document.querySelector('.highlight-item');
        console.log('Primer elemento con querySelector (.highlight-item):', firstHighlightedItem);

        // querySelectorAll: Devuelve una NodeList (parecida a un array) de *todos* los elementos que coinciden.
        const allCards = document.querySelectorAll('.card');
        console.log('Todos los elementos con querySelectorAll (.card):', allCards);
        allCards.forEach((card, index) => {
            // Podemos usar métodos de array como forEach.
            card.style.borderTop = `5px solid #${Math.floor(Math.random()*16777215).toString(16)}`;
        });

        // 1.5: Navegación por el DOM
        // Desde un elemento, podemos movernos a sus parientes.
        const selectionContainer = document.getElementById('selection-container');
        console.log('Contenedor de selección:', selectionContainer);
        
        // Padre
        const parentOfContainer = selectionContainer.parentElement;
        console.log('Padre del contenedor:', parentOfContainer);
        parentOfContainer.style.backgroundColor = '#eafaf1';

        // Hijos (solo elementos, ignora texto y comentarios)
        const containerChildren = selectionContainer.children;
        console.log('Hijos del contenedor:', containerChildren);

        // Siguiente hermano (elemento)
        const nextSibling = selectionContainer.nextElementSibling;
        console.log('Siguiente hermano del contenedor:', nextSibling);
        
        console.log('--- FIN DE SELECCIÓN Y NAVEGACIÓN ---');
    });


    // ===================================================================================
    // PARTE 2: MANIPULACIÓN DE CONTENIDO Y ATRIBUTOS
    // Cómo cambiar lo que se ve dentro de los elementos y sus atributos.
    // ===================================================================================
    const runManipulationBtn = document.getElementById('run-manipulation-btn');

    runManipulationBtn.addEventListener('click', () => {
        // 2.1: Cambiar contenido de texto con .textContent (seguro y rápido)
        const textToChange = document.getElementById('text-to-change');
        textToChange.textContent = '¡El texto ha sido actualizado! Esto es solo texto plano.';

        // 2.2: Cambiar contenido HTML con .innerHTML (potente pero usar con cuidado)
        // ADVERTENCIA: Nunca uses .innerHTML con datos de un usuario para evitar ataques XSS.
        const htmlToChange = document.getElementById('html-to-change');
        htmlToChange.innerHTML = '<h2>¡HTML Inyectado!</h2><p>Acabamos de reemplazar el contenido con nuevas etiquetas <strong>HTML</strong>.</p>';

        // 2.3: Manipular atributos
        const mainLink = document.getElementById('main-link');
        mainLink.setAttribute('href', 'https://www.google.com');
        mainLink.setAttribute('target', '_blank'); // Abrir en una nueva pestaña
        mainLink.textContent = 'Ir a Google';

        const mainImage = document.getElementById('main-image');
        mainImage.src = 'https://placehold.co/100x100/3498db/ffffff?text=Cambiado';
        mainImage.alt = 'Imagen modificada con JavaScript';
        console.log('Nuevo href del enlace:', mainLink.getAttribute('href'));
    });


    // ===================================================================================
    // PARTE 3: MANIPULACIÓN DE ESTILOS
    // Cómo cambiar la apariencia de los elementos.
    // ===================================================================================
    const styleBox = document.getElementById('style-box');

    // 3.1: Cambiar estilos en línea con .style
    styleBox.addEventListener('mouseover', () => {
        styleBox.style.backgroundColor = '#9b59b6';
        styleBox.style.borderRadius = '50%';
    });
    styleBox.addEventListener('mouseout', () => {
        styleBox.style.backgroundColor = '#e74c3c';
        styleBox.style.borderRadius = '5px';
    });

    // 3.2: Manipular clases con .classList (la forma recomendada)
    // Es mejor tener los estilos en CSS y usar JS para añadir/quitar clases.
    styleBox.addEventListener('click', () => {
        styleBox.classList.toggle('box-active-style');
    });


    // ===================================================================================
    // PARTE 4: CREACIÓN Y ELIMINACIÓN DE ELEMENTOS
    // Cómo añadir y quitar elementos de la página dinámicamente.
    // ===================================================================================
    const itemList = document.getElementById('item-list');
    const addItemBtn = document.getElementById('add-item-btn');
    const addMultipleBtn = document.getElementById('add-multiple-btn');
    const removeLastBtn = document.getElementById('remove-last-btn');

    // 4.1: Crear y añadir un solo elemento
    addItemBtn.addEventListener('click', () => {
        const newItem = document.createElement('li'); // 1. Crear el elemento
        newItem.textContent = `Nuevo Ítem #${itemList.children.length + 1}`; // 2. Configurar
        itemList.appendChild(newItem); // 3. Añadir al DOM
    });

    // 4.2: Eliminar un elemento
    removeLastBtn.addEventListener('click', () => {
        const lastItem = itemList.lastElementChild;
        if (lastItem) {
            lastItem.remove(); // El método .remove() es la forma moderna y fácil.
        } else {
            alert('No hay más ítems para eliminar.');
        }
    });
    
    // 4.3: Crear y añadir múltiples elementos de forma eficiente
    // Usamos un DocumentFragment para evitar múltiples "reflows" del DOM, mejorando el rendimiento.
    addMultipleBtn.addEventListener('click', () => {
        const fragment = document.createDocumentFragment(); // 1. Crear un fragmento en memoria
        for (let i = 0; i < 5; i++) {
            const newItem = document.createElement('li');
            newItem.textContent = `Ítem Múltiple ${i + 1}`;
            fragment.appendChild(newItem); // 2. Añadir elementos al fragmento (no al DOM real)
        }
        itemList.appendChild(fragment); // 3. Añadir el fragmento completo al DOM de una sola vez.
    });


    // ===================================================================================
    // PARTE 5: MANEJO DE EVENTOS
    // Cómo hacer que la página reaccione a las acciones del usuario.
    // ===================================================================================
    const mainForm = document.getElementById('main-form');
    const textInput = document.getElementById('text-input');
    const keyOutput = document.getElementById('key-output');

    // 5.1: Evento de envío de formulario y .preventDefault()
    mainForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Evita que la página se recargue (comportamiento por defecto del formulario)
        alert(`Formulario enviado con el valor: ${textInput.value}`);
        textInput.value = ''; // Limpiar el input
    });

    // 5.2: Eventos de teclado
    textInput.addEventListener('keydown', (event) => {
        // El objeto 'event' contiene información sobre el evento, como la tecla presionada.
        keyOutput.textContent = event.key;
    });

    // 5.3: Delegación de Eventos (Técnica avanzada y eficiente)
    // En lugar de poner un 'listener' en cada 'li', ponemos uno solo en el padre 'ul'.
    // Esto funciona incluso para los 'li' que añadamos en el futuro.
    itemList.addEventListener('click', (event) => {
        // Comprobamos si el elemento que originó el clic (event.target) es un LI.
        if (event.target && event.target.tagName === 'LI') {
            // Si es así, le aplicamos el estilo.
            event.target.classList.toggle('item-completed');
            console.log(`Clic en tarea: "${event.target.textContent}"`);
        }
    });

});
