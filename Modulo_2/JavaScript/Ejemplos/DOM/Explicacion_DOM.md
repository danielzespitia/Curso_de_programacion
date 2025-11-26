# El DOM (Document Object Model) en JavaScript

## 1. ¿Qué es el DOM?

El **DOM** (Document Object Model o Modelo de Objetos del Documento) es una interfaz de programación para documentos web. Representa la página web de manera que los programas (como JavaScript) pueden cambiar la estructura, el estilo y el contenido del documento. El DOM representa el documento como nodos y objetos; de esta forma, los lenguajes de programación pueden conectarse a la página.

Imagina el DOM como un **árbol genealógico** de todos los elementos que componen tu página HTML. El navegador lee tu HTML y construye este árbol en memoria.

## 2. La Estructura de Árbol

El DOM organiza el documento HTML en una estructura jerárquica de árbol.

- **Raíz (Root):** El punto de partida, generalmente el objeto `document` o la etiqueta `<html>`.
- **Ramas y Hojas:** Cada etiqueta HTML (`<body>`, `<div>`, `<p>`, `<a>`) es un nodo en este árbol.

### Tipos de Nodos Principales:

1.  **Document Node:** Representa todo el documento. Es el punto de entrada al DOM (`document`).
2.  **Element Node:** Representa una etiqueta HTML (ej. `<div>`, `<p>`).
3.  **Text Node:** Representa el texto dentro de una etiqueta. (Ojo: los saltos de línea y espacios a veces cuentan como nodos de texto vacíos).
4.  **Attribute Node:** Representa los atributos de las etiquetas (ej. `class="btn"`, `href="..."`), aunque en el DOM moderno se suelen acceder como propiedades de los elementos.
5.  **Comment Node:** Representa los comentarios de HTML `<!-- Comentario -->`.

## 3. Accediendo al DOM (Selección de Elementos)

Para manipular algo, primero necesitas encontrarlo. JavaScript nos ofrece varios métodos para "agarrar" elementos del árbol.

### Métodos Tradicionales:

- `document.getElementById('id')`: Busca un elemento por su atributo `id`. Es muy rápido y devuelve un único elemento.
- `document.getElementsByClassName('clase')`: Devuelve una colección (HTMLCollection) de todos los elementos que tengan esa clase.
- `document.getElementsByTagName('etiqueta')`: Devuelve una colección de todos los elementos con ese nombre de etiqueta (ej. todos los `<p>`).

### Métodos Modernos (Recomendados):

- `document.querySelector('selectorCSS')`: Devuelve el **primer** elemento que coincida con el selector CSS especificado (ej. `.mi-clase`, `#mi-id`, `div > p`).
- `document.querySelectorAll('selectorCSS')`: Devuelve una **NodeList** (lista de nodos) con **todos** los elementos que coincidan.

```javascript
// Ejemplos
const titulo = document.getElementById("titulo-principal");
const primerParrafo = document.querySelector(".texto-intro");
const todosLosBotones = document.querySelectorAll("button");
```

## 4. Manipulación del DOM

Una vez que tienes una referencia a un elemento, puedes cambiarlo.

### Cambiar Contenido:

- `elemento.innerHTML`: Permite leer o escribir el contenido HTML interno (incluyendo etiquetas hijas).
- `elemento.textContent`: Permite leer o escribir solo el texto, ignorando las etiquetas HTML. Es más seguro y rápido si solo cambias texto.
- `elemento.innerText`: Similar a `textContent`, pero respeta los estilos CSS (como `display: none`).

### Cambiar Estilos:

Puedes acceder a la propiedad `style` del elemento. Las propiedades CSS con guiones se convierten a camelCase (ej. `background-color` -> `backgroundColor`).

```javascript
const caja = document.querySelector(".caja");
caja.style.backgroundColor = "red";
caja.style.fontSize = "20px";
caja.style.display = "none"; // Ocultar
```

### Manipular Clases (ClassList):

Es la forma moderna y limpia de manejar estilos CSS predefinidos.

- `elemento.classList.add('nueva-clase')`: Agrega una clase.
- `elemento.classList.remove('clase-vieja')`: Elimina una clase.
- `elemento.classList.toggle('activo')`: Si la tiene la quita, si no la tiene la pone.
- `elemento.classList.contains('clase')`: Devuelve `true` o `false` si tiene la clase.

### Manipular Atributos:

- `elemento.getAttribute('href')`: Obtiene el valor de un atributo.
- `elemento.setAttribute('src', 'imagen.jpg')`: Cambia o crea un atributo.
- `elemento.removeAttribute('disabled')`: Elimina un atributo.

## 5. Creación y Eliminación de Elementos (DOM Traversing y Modification)

No solo puedes cambiar lo que existe, puedes crear cosas nuevas.

### Crear Elementos:

1.  **Crear el nodo:** `const nuevoDiv = document.createElement('div');`
2.  **Configurarlo:** `nuevoDiv.textContent = 'Hola soy nuevo';`
3.  **Insertarlo en el DOM:** Necesitas un padre para insertarlo.
    - `padre.appendChild(nuevoDiv)`: Lo agrega al final de los hijos del padre.
    - `padre.prepend(nuevoDiv)`: Lo agrega al principio.
    - `padre.insertBefore(nuevoDiv, referencia)`: Lo inserta antes de un nodo de referencia.

### Eliminar Elementos:

- `elemento.remove()`: El elemento se elimina a sí mismo (Método moderno).
- `padre.removeChild(hijo)`: Método antiguo, necesitas referencia al padre y al hijo.

## 6. Navegación por el DOM (Traversing)

A veces tienes un elemento y quieres moverte a sus parientes.

- **Hijos:**
  - `elemento.children`: Colección de elementos hijos (solo etiquetas).
  - `elemento.childNodes`: Colección de todos los nodos hijos (incluye texto y comentarios).
  - `elemento.firstElementChild` / `elemento.lastElementChild`: Primer y último hijo elemento.
- **Padres:**
  - `elemento.parentElement`: El elemento padre directo.
  - `elemento.closest('selector')`: Busca el ancestro más cercano que cumpla con el selector (muy útil).
- **Hermanos:**
  - `elemento.nextElementSibling`: El siguiente hermano (etiqueta).
  - `elemento.previousElementSibling`: El hermano anterior.

## 7. Eventos del DOM

El DOM no es estático; reacciona al usuario. Los eventos son señales de que algo ocurrió (clic, tecla presionada, carga terminada).

### Escuchar Eventos (Event Listeners):

La mejor práctica es usar `addEventListener`.

```javascript
const boton = document.querySelector("#mi-boton");

boton.addEventListener("click", function (evento) {
  console.log("¡Hiciste clic!");
  // 'evento' contiene información sobre el clic (coordenadas, tecla, etc.)
  console.log(evento.target); // El elemento que disparó el evento
});
```

### Tipos comunes de eventos:

- **Mouse:** `click`, `dblclick`, `mouseenter`, `mouseleave`, `mousemove`.
- **Teclado:** `keydown`, `keyup`, `keypress`.
- **Formulario:** `submit`, `change`, `input`, `focus`, `blur`.
- **Documento:** `DOMContentLoaded` (cuando el HTML ha cargado), `load` (cuando todo, incluidas imágenes, ha cargado).

## Resumen Visual

```
Document
 └── html
      ├── head
      │    ├── title
      │    └── meta
      └── body
           ├── h1 ("Título")
           ├── div (id="contenedor")
           │    ├── p ("Texto")
           │    └── button ("Click")
           └── script
```

Entender el DOM es fundamental porque es el puente entre la lógica de tu código JavaScript y lo que el usuario ve e interactúa en el navegador.
