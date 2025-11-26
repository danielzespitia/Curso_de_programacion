# Guía Detallada: Estructura Global y Metadatos HTML

Esta guía cubre las etiquetas fundamentales que conforman la estructura básica de un documento HTML y la configuración de metadatos.

---

## 1. `<!DOCTYPE html>`

**Descripción:**  
No es estrictamente una etiqueta HTML, sino una instrucción para el navegador. Le indica qué versión de HTML se está utilizando. En HTML5, la declaración es muy simple. Sin ella, los navegadores pueden entrar en "Quirks Mode" (modo de compatibilidad), renderizando la página de forma incorrecta.

**Uso:**  
Debe ser siempre la **primera línea** de tu archivo.

**Ejemplo:**

```html
<!DOCTYPE html>
<html>
  ...
</html>
```

---

## 2. `<html>`

**Descripción:**  
Es el elemento raíz (root) de un documento HTML. Todos los demás elementos deben ser descendientes de esta etiqueta.

**Atributos Comunes:**

- `lang`: Especifica el idioma del contenido (ej. "es", "en"). Es crucial para la accesibilidad y los motores de búsqueda.

**Ejemplo:**

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    ...
  </head>
  <body>
    ...
  </body>
</html>
```

---

## 3. `<head>`

**Descripción:**  
Contiene metadatos (datos sobre los datos) del documento. El contenido de `<head>` **no se muestra** directamente en la página web (a excepción del título en la pestaña). Aquí se definen títulos, enlaces a hojas de estilo, scripts y metadatos.

**Ejemplo:**

```html
<head>
  <meta charset="UTF-8" />
  <title>Mi Página</title>
</head>
```

---

## 4. `<title>`

**Descripción:**  
Define el título del documento. Este texto aparece en:

1. La pestaña del navegador.
2. Los resultados de los motores de búsqueda (Google, Bing).
3. Cuando se agrega la página a favoritos.

**Importancia:**  
Es vital para el SEO (Search Engine Optimization).

**Ejemplo:**

```html
<title>Curso de Programación - Módulo 2</title>
```

---

## 5. `<body>`

**Descripción:**  
Contiene todo el contenido visible de un documento HTML, como texto, imágenes, enlaces, tablas, listas, etc. Solo puede haber un elemento `<body>` en un documento.

**Ejemplo:**

```html
<body>
  <h1>Hola Mundo</h1>
  <p>Este es el contenido visible.</p>
</body>
```

---

## 6. `<meta>`

**Descripción:**  
Define metadatos que no tienen una etiqueta específica (como `<title>` o `<link>`). Es una etiqueta vacía (no tiene cierre).

**Usos más comunes:**

- **Charset:** `<meta charset="UTF-8">` (Define la codificación de caracteres, esencial para ñ y tildes).
- **Viewport:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">` (Esencial para diseño responsivo en móviles).
- **Descripción:** `<meta name="description" content="Resumen de la página">` (Usado por buscadores).

**Ejemplo:**

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Tutorial completo de HTML5" />
```

---

## 7. `<link>`

**Descripción:**  
Se usa para vincular el documento actual con un recurso externo. El uso más común es vincular hojas de estilo CSS.

**Atributos:**

- `rel`: Relación del archivo vinculado (ej. "stylesheet").
- `href`: La ruta al archivo.

**Ejemplo:**

```html
<link rel="stylesheet" href="styles.css" />
<link rel="icon" href="favicon.ico" />
```

---

## 8. `<script>`

**Descripción:**  
Se utiliza para incrustar código ejecutable (normalmente JavaScript) o para referenciar un archivo de script externo.

**Atributos:**

- `src`: Ruta al archivo JS externo.
- `defer` / `async`: Controlan cómo se carga el script para no bloquear la renderización de la página.

**Ejemplo:**

```html
<!-- Script en línea -->
<script>
  console.log("Hola desde JS");
</script>

<!-- Script externo -->
<script src="app.js" defer></script>
```
