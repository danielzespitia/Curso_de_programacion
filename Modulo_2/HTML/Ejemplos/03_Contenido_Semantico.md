# Guía Detallada: Contenido Semántico y Estructural

Estas etiquetas definen la estructura y el significado de las diferentes partes de tu página web, ayudando a los navegadores y buscadores a entender tu contenido.

---

## 1. `<div>` (División)

**Descripción:**  
Es el contenedor genérico por excelencia. No tiene significado semántico por sí mismo. Se usa para agrupar elementos con fines de estilo (CSS) o scripting (JS). Es un elemento de bloque.

**Ejemplo:**

```html
<div class="tarjeta-usuario">
  <img src="foto.jpg" />
  <p>Nombre Usuario</p>
</div>
```

---

## 2. `<main>`

**Descripción:**  
Especifica el contenido principal y único del documento. No debe haber más de un `<main>` visible en el documento. No debe incluir contenido que se repita en otras páginas (como menús de navegación, footers, sidebars).

**Ejemplo:**

```html
<body>
  <header>...</header>
  <main>
    <h1>Artículo Principal</h1>
    <p>Contenido del artículo...</p>
  </main>
  <footer>...</footer>
</body>
```

---

## 3. `<header>`

**Descripción:**  
Representa un contenedor para contenido introductorio o un conjunto de enlaces de navegación. Puede contener encabezados (`h1`-`h6`), logos, formularios de búsqueda, etc.
Puede usarse como cabecera de la página o cabecera de una sección (`<article>`, `<section>`).

**Ejemplo:**

```html
<header>
  <img src="logo.png" alt="Logo" />
  <nav>...</nav>
</header>
```

---

## 4. `<footer>`

**Descripción:**  
Define el pie de página de un documento o sección. Suele contener información de derechos de autor, enlaces a términos de uso, contacto, etc.

**Ejemplo:**

```html
<footer>
  <p>&copy; 2025 Mi Empresa</p>
  <a href="/contacto">Contacto</a>
</footer>
```

---

## 5. `<nav>` (Navegación)

**Descripción:**  
Define una sección que contiene enlaces de navegación (menús). No todos los enlaces deben estar en un `<nav>`, solo los bloques principales de navegación.

**Ejemplo:**

```html
<nav>
  <ul>
    <li><a href="#inicio">Inicio</a></li>
    <li><a href="#servicios">Servicios</a></li>
  </ul>
</nav>
```

---

## 6. `<section>`

**Descripción:**  
Representa una sección genérica de un documento. Se usa para agrupar contenido temáticamente relacionado. Generalmente, cada `<section>` debería tener un encabezado (`h2`-`h6`).

**Diferencia con `<div>`:**  
Usa `<section>` cuando el contenido tiene un tema relacionado. Usa `<div>` solo para contenedores de diseño sin significado.

**Ejemplo:**

```html
<section id="sobre-nosotros">
  <h2>Sobre Nosotros</h2>
  <p>Somos una empresa dedicada a...</p>
</section>
```

---

## 7. `<article>`

**Descripción:**  
Especifica contenido independiente y autónomo. El contenido debería tener sentido por sí mismo y poder distribuirse independientemente del resto del sitio (ej. un post de blog, una noticia, un comentario).

**Ejemplo:**

```html
<article>
  <h2>El futuro de la IA</h2>
  <p>Publicado el 26/11/2025</p>
  <p>La inteligencia artificial está...</p>
</article>
```

---

## 8. `<aside>`

**Descripción:**  
Define contenido que está relacionado tangencialmente con el contenido que lo rodea (como una barra lateral). A menudo se usa para sidebars, cajas de publicidad, o grupos de enlaces.

**Ejemplo:**

```html
<aside>
  <h3>Artículos Relacionados</h3>
  <ul>
    ...
  </ul>
</aside>
```

---

## 9. `<ul>` (Lista Desordenada)

**Descripción:**  
Define una lista donde el orden de los ítems no importa. Se muestra con viñetas (bullet points) por defecto.

**Hijos permitidos:** Solo elementos `<li>`.

**Ejemplo:**

```html
<ul>
  <li>Leche</li>
  <li>Pan</li>
  <li>Huevos</li>
</ul>
```

---

## 10. `<ol>` (Lista Ordenada)

**Descripción:**  
Define una lista donde el orden sí importa. Se muestra con números (1, 2, 3...) por defecto.

**Atributos:**

- `type`: "1", "a", "A", "i", "I" (cambia el tipo de numeración).
- `start`: Número en el que empieza la lista.

**Ejemplo:**

```html
<ol>
  <li>Paso 1: Abrir archivo</li>
  <li>Paso 2: Editar</li>
</ol>
```

---

## 11. `<li>` (Ítem de Lista)

**Descripción:**  
Define un ítem dentro de una lista (`<ul>`, `<ol>` o `<menu>`).

**Ejemplo:**

```html
<ul>
  <li>Soy un ítem</li>
</ul>
```
