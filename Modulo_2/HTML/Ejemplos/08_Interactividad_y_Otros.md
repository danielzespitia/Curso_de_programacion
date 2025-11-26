# Guía Detallada: Interactividad y Elementos Especiales

Etiquetas que añaden funcionalidades interactivas nativas sin necesidad de mucho JavaScript.

---

## 1. `<details>` y `<summary>`

**Descripción:**  
Crea un widget de divulgación (acordeón) donde el usuario puede abrir y cerrar contenido.
`<summary>` define el encabezado visible. `<details>` contiene el contenido oculto.

**Ejemplo:**

```html
<details>
  <summary>Más información</summary>
  <p>Aquí están los detalles ocultos que ahora puedes ver.</p>
</details>
```

---

## 2. `<dialog>`

**Descripción:**  
Define un cuadro de diálogo o ventana modal nativa.

**Atributos:**

- `open`: Indica que el diálogo está activo y visible.

**Ejemplo:**

```html
<dialog open>
  <p>¡Hola! Soy una ventana modal.</p>
</dialog>
```

---

## 3. `<meter>`

**Descripción:**  
Define una medida escalar dentro de un rango conocido (como uso de disco, relevancia de búsqueda). No usar para progreso de tareas.

**Atributos:**

- `value`: Valor actual.
- `min`, `max`: Rango.
- `low`, `high`, `optimum`: Rangos para colorear la barra (verde, amarillo, rojo).

**Ejemplo:**

```html
<label>Uso de disco:</label> <meter value="0.6">60%</meter>
```

---

## 4. `<progress>`

**Descripción:**  
Representa el progreso de una tarea (barra de carga).

**Ejemplo:**

```html
<label>Descargando:</label> <progress value="32" max="100">32%</progress>
```

---

## 5. `<map>` y `<area>`

**Descripción:**  
Se usan para crear mapas de imágenes (imágenes con áreas clickeables).
`<map>` define el mapa.
`<area>` define las regiones clickeables dentro del mapa.

**Ejemplo:**

```html
<img src="planetas.jpg" usemap="#mapa-planetas" />

<map name="mapa-planetas">
  <area shape="rect" coords="0,0,82,126" href="sol.html" alt="Sol" />
  <area shape="circle" coords="90,58,3" href="mercurio.html" alt="Mercurio" />
</map>
```

---

## 6. `<template>`

**Descripción:**  
Contenedor para contenido HTML que no se renderiza al cargar la página, pero que puede ser instanciado posteriormente mediante JavaScript. Muy útil para componentes dinámicos.

**Ejemplo:**

```html
<template id="mi-plantilla">
  <div class="tarjeta">
    <h2>Título</h2>
    <p>Descripción</p>
  </div>
</template>
```

---

## 7. `<noscript>`

**Descripción:**  
Define contenido alternativo para usuarios que tienen JavaScript deshabilitado en su navegador.

**Ejemplo:**

```html
<script>
  document.write("¡Hola Mundo!");
</script>
<noscript>Tu navegador no soporta JavaScript.</noscript>
```

---

## 8. `<base>`

**Descripción:**  
Especifica la URL base y/o el objetivo (target) para todos los enlaces relativos en un documento. Debe ir en el `<head>`.

**Ejemplo:**

```html
<head>
  <base href="https://www.ejemplo.com/imagenes/" target="_blank" />
</head>
<body>
  <img src="foto.jpg" />
  <!-- Carga desde https://www.ejemplo.com/imagenes/foto.jpg -->
</body>
```
