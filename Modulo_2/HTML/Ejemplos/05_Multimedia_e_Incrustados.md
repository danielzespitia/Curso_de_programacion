# Guía Detallada: Multimedia y Contenido Incrustado

Estas etiquetas permiten enriquecer la página web con imágenes, audio, video y otros recursos externos.

---

## 1. `<img>`

**Descripción:**  
Inserta una imagen en el documento. Es una etiqueta vacía (no tiene cierre).

**Atributos Esenciales:**

- `src`: La ruta (URL) a la imagen.
- `alt`: Texto alternativo (descripción) si la imagen no carga. Vital para accesibilidad y SEO.
- `width` / `height`: Dimensiones de la imagen (recomendado para evitar saltos de diseño al cargar).
- `loading`: `lazy` (carga diferida para mejorar rendimiento).

**Ejemplo:**

```html
<img
  src="foto.jpg"
  alt="Un gato durmiendo"
  width="500"
  height="300"
  loading="lazy"
/>
```

---

## 2. `<figure>` y `<figcaption>`

**Descripción:**  
`<figure>` especifica contenido autónomo, como ilustraciones, diagramas, fotos o listados de código.
`<figcaption>` define un título o leyenda para el contenido de `<figure>`.

**Ejemplo:**

```html
<figure>
  <img src="grafico.png" alt="Gráfico de ventas" />
  <figcaption>Fig. 1: Ventas del año 2025.</figcaption>
</figure>
```

---

## 3. `<audio>`

**Descripción:**  
Se usa para incrustar contenido de sonido.

**Atributos:**

- `controls`: Muestra los controles de reproducción (play, pausa, volumen).
- `autoplay`: Reproduce automáticamente (a menudo bloqueado por navegadores).
- `loop`: Repite el audio al finalizar.
- `muted`: Inicia silenciado.

**Ejemplo:**

```html
<audio controls>
  <source src="cancion.mp3" type="audio/mpeg" />
  Tu navegador no soporta el elemento de audio.
</audio>
```

---

## 4. `<video>`

**Descripción:**  
Se usa para incrustar contenido de video.

**Atributos:**

- `controls`, `autoplay`, `loop`, `muted`.
- `poster`: Imagen que se muestra antes de reproducir el video.
- `width` / `height`.

**Ejemplo:**

```html
<video width="320" height="240" controls poster="miniatura.jpg">
  <source src="pelicula.mp4" type="video/mp4" />
  Tu navegador no soporta video.
</video>
```

---

## 5. `<source>`

**Descripción:**  
Especifica recursos multimedia múltiples para elementos `<video>`, `<audio>` y `<picture>`. El navegador elegirá el primer formato que soporte.

**Ejemplo:**
(Ver ejemplos de audio y video arriba)

---

## 6. `<track>`

**Descripción:**  
Especifica pistas de texto para elementos multimedia (`<audio>` y `<video>`), como subtítulos.

**Atributos:**

- `kind`: Tipo de pista (`subtitles`, `captions`).
- `src`: Archivo `.vtt`.
- `srclang`: Idioma.

**Ejemplo:**

```html
<video controls>
  <source src="video.mp4" type="video/mp4" />
  <track
    src="subtitulos_es.vtt"
    kind="subtitles"
    srclang="es"
    label="Español"
  />
</video>
```

---

## 7. `<iframe>`

**Descripción:**  
Marco en línea (Inline Frame). Se usa para incrustar otra página web dentro de la actual (ej. mapas de Google, videos de YouTube).

**Atributos:**

- `src`: URL de la página a incrustar.
- `width` / `height`.
- `frameborder`: Borde (obsoleto en HTML5, usar CSS).

**Ejemplo:**

```html
<iframe
  src="https://www.google.com/maps/embed?..."
  width="600"
  height="450"
></iframe>
```

---

## 8. `<picture>`

**Descripción:**  
Permite especificar múltiples fuentes de imagen para diferentes situaciones (ej. diferentes tamaños de pantalla o formatos de imagen como WebP). Da más control que `<img>` solo.

**Ejemplo:**

```html
<picture>
  <source media="(min-width: 650px)" srcset="img_grande.jpg" />
  <source media="(min-width: 465px)" srcset="img_mediana.jpg" />
  <img src="img_pequena.jpg" alt="Flores" />
</picture>
```

---

## 9. `<canvas>`

**Descripción:**  
Contenedor para gráficos dibujados sobre la marcha mediante scripts (generalmente JavaScript). Se usa para juegos, visualización de datos, etc.

**Ejemplo:**

```html
<canvas id="miLienzo" width="200" height="100"></canvas>
<script>
  var c = document.getElementById("miLienzo");
  var ctx = c.getContext("2d");
  ctx.fillStyle = "#FF0000";
  ctx.fillRect(0, 0, 150, 75);
</script>
```

---

## 10. `<svg>` (Scalable Vector Graphics)

**Descripción:**  
Define gráficos vectoriales en formato XML directamente en el HTML. Los gráficos SVG no pierden calidad al hacer zoom.

**Ejemplo:**

```html
<svg width="100" height="100">
  <circle
    cx="50"
    cy="50"
    r="40"
    stroke="green"
    stroke-width="4"
    fill="yellow"
  />
</svg>
```
