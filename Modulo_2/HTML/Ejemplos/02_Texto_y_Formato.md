# Guía Detallada: Texto y Formato en HTML

Estas etiquetas se utilizan para estructurar y dar significado al texto dentro de tu página web.

---

## 1. `<h1>` a `<h6>` (Encabezados)

**Descripción:**  
Representan seis niveles de encabezados de sección. `<h1>` es el más importante y `<h6>` el menos importante.

**Reglas de Oro:**

- Usa solo un `<h1>` por página (generalmente el título principal).
- No te saltes niveles (no pases de `<h1>` a `<h3>`).
- No los uses solo para hacer el texto grande (usa CSS para eso); úsalos para estructura semántica.

**Ejemplo:**

```html
<h1>Título Principal del Artículo</h1>
<h2>Subtítulo de la Sección</h2>
<h3>Sub-sección específica</h3>
```

---

## 2. `<p>` (Párrafo)

**Descripción:**  
Define un párrafo de texto. Los navegadores añaden automáticamente un margen antes y después de cada elemento `<p>`.

**Ejemplo:**

```html
<p>Este es un párrafo de texto. HTML ignorará los espacios extra.</p>
<p>Este es otro párrafo separado.</p>
```

---

## 3. `<span>`

**Descripción:**  
Es un contenedor en línea (inline) genérico. A diferencia de `<div>`, no inicia una nueva línea. Se usa principalmente para aplicar estilos CSS o manipular texto con JavaScript en partes pequeñas de un párrafo.

**Ejemplo:**

```html
<p>Mi color favorito es el <span style="color: blue;">azul</span>.</p>
```

---

## 4. `<br>` (Salto de Línea)

**Descripción:**  
Produce un salto de línea (line break) dentro del texto. Es una etiqueta vacía.

**Cuándo usarla:**  
Para poemas o direcciones postales. **NO** la uses para crear espacio entre párrafos (usa márgenes CSS para eso).

**Ejemplo:**

```html
<p>
  Calle Falsa 123<br />
  Ciudad Gótica<br />
  CP 54321
</p>
```

---

## 5. `<hr>` (Cambio Temático)

**Descripción:**  
Originalmente "Horizontal Rule" (línea horizontal). En HTML5 representa un cambio temático entre párrafos (como un cambio de escena en una historia). Visualmente se renderiza como una línea horizontal.

**Ejemplo:**

```html
<p>Fin de la primera escena.</p>
<hr />
<p>Inicio de la segunda escena.</p>
```

---

## 6. `<strong>` (Importancia Fuerte)

**Descripción:**  
Indica que el texto tiene gran importancia, seriedad o urgencia. Visualmente, los navegadores lo muestran en **negrita**.

**Diferencia con `<b>`:**  
`<b>` solo hace el texto negrita visualmente. `<strong>` aporta significado semántico (importante para lectores de pantalla).

**Ejemplo:**

```html
<p><strong>Precaución:</strong> Piso mojado.</p>
```

---

## 7. `<em>` (Énfasis)

**Descripción:**  
Indica énfasis en el texto (como cuando cambias el tono de voz). Visualmente se muestra en _cursiva_.

**Diferencia con `<i>`:**  
`<i>` es para texto en una voz diferente (términos técnicos, pensamientos), `<em>` es para énfasis.

**Ejemplo:**

```html
<p>No *olvides* comprar leche. (<em>olvides</em>)</p>
```

---

## 8. `<blockquote>`

**Descripción:**  
Indica que una sección de texto es una cita de otra fuente. Los navegadores suelen sangrar (indentar) este contenido.

**Atributo `cite`:**  
URL de la fuente de la cita.

**Ejemplo:**

```html
<blockquote cite="https://www.wikipedia.org">
  La programación es el arte de decirle a otra persona lo que quieres que la
  computadora haga.
</blockquote>
```

---

## 9. `<pre>` (Texto Preformateado)

**Descripción:**  
Muestra el texto exactamente como está escrito en el archivo HTML, respetando espacios y saltos de línea. Usa una fuente monoespaciada.

**Ejemplo:**

```html
<pre>
  Este texto    mantiene
      sus espacios
  y saltos.
</pre>
```

---

## 10. `<code>`

**Descripción:**  
Define un fragmento de código de computadora. Para bloques de código grandes, se suele combinar con `<pre>`.

**Ejemplo:**

```html
<p>Para imprimir usa <code>console.log()</code>.</p>
```
