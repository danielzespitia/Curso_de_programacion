# Guía Detallada: Texto Avanzado y Semántica Fina

Estas etiquetas se utilizan para dar significados muy específicos a partes del texto, mejorando la accesibilidad y la comprensión del documento.

---

## 1. `<abbr>` (Abreviatura)

**Descripción:**  
Define una abreviatura o acrónimo. El atributo `title` proporciona la expansión completa.

**Ejemplo:**

```html
<p>
  La <abbr title="Organización Mundial de la Salud">OMS</abbr> fue fundada en
  1948.
</p>
```

---

## 2. `<address>`

**Descripción:**  
Define la información de contacto del autor/propietario de un documento o artículo. El texto suele mostrarse en cursiva.

**Ejemplo:**

```html
<address>
  Escrito por <a href="mailto:webmaster@ejemplo.com">Jon Doe</a>.<br />
  Visítanos en: Box 564, Disneyland<br />
  USA
</address>
```

---

## 3. `<cite>`

**Descripción:**  
Define el título de una obra creativa (libro, película, canción).

**Ejemplo:**

```html
<p>La pintura <cite>El Grito</cite> de Edvard Munch.</p>
```

---

## 4. `<q>` (Cita Corta)

**Descripción:**  
Define una cita corta en línea. Los navegadores suelen añadir comillas automáticamente alrededor.

**Ejemplo:**

```html
<p>WWF dice: <q>Nuestro futuro está en riesgo.</q></p>
```

---

## 5. `<mark>`

**Descripción:**  
Define texto marcado o resaltado (como con un resaltador amarillo). Se usa para destacar partes relevantes en un contexto específico.

**Ejemplo:**

```html
<p>No olvides comprar <mark>leche</mark> hoy.</p>
```

---

## 6. `<del>` y `<ins>`

**Descripción:**  
`<del>`: Texto que ha sido eliminado del documento (tachado).
`<ins>`: Texto que ha sido insertado en el documento (subrayado).
Útil para mostrar revisiones o cambios.

**Ejemplo:**

```html
<p>Mi color favorito es <del>azul</del> <ins>rojo</ins>.</p>
```

---

## 7. `<sub>` y `<sup>`

**Descripción:**  
`<sub>`: Subíndice (texto más bajo y pequeño). Ej: H₂O.
`<sup>`: Superíndice (texto más alto y pequeño). Ej: x².

**Ejemplo:**

```html
<p>Fórmula del agua: H<sub>2</sub>O</p>
<p>Ecuación: E = mc<sup>2</sup></p>
```

---

## 8. `<small>`

**Descripción:**  
Define texto más pequeño (como letra pequeña de contratos, derechos de autor, etc.).

**Ejemplo:**

```html
<p><small>&copy; 2025 Todos los derechos reservados.</small></p>
```

---

## 9. `<time>`

**Descripción:**  
Define una fecha u hora específica. El atributo `datetime` permite que las máquinas lean la fecha en formato estándar.

**Ejemplo:**

```html
<p>
  Tenemos una fiesta el
  <time datetime="2025-02-14 20:00">Día de San Valentín</time>.
</p>
```

---

## 10. `<kbd>` (Teclado)

**Descripción:**  
Define una entrada de teclado. Se suele mostrar en fuente monoespaciada.

**Ejemplo:**

```html
<p>Presiona <kbd>Ctrl</kbd> + <kbd>C</kbd> para copiar.</p>
```

---

## 11. `<i>` y `<b>` (Estilos sin semántica fuerte)

**Descripción:**  
`<i>`: Texto en una voz o estado de ánimo alternativo (términos técnicos, frases en otro idioma). Visualmente cursiva.
`<b>`: Texto al que se quiere llamar la atención sin importancia extra. Visualmente negrita.

**Nota:** Preferir `<em>` y `<strong>` si hay importancia semántica.

**Ejemplo:**

```html
<p>El término <i>taxonomía</i> significa clasificación.</p>
```
