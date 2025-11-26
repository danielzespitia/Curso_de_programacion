# Guía Detallada: Tipografía y Texto en CSS

Estas propiedades controlan la apariencia visual del texto.

---

## 1. `font-family`

**Descripción:**  
Define la fuente (tipo de letra) del texto. Se suele especificar una lista de fuentes ("stack") como respaldo por si la primera no está disponible.

**Tipos Genéricos:**

- `serif` (con remates, ej. Times New Roman).
- `sans-serif` (sin remates, ej. Arial).
- `monospace` (ancho fijo, ej. Courier).

**Ejemplo:**

```css
body {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

---

## 2. `font-size`

**Descripción:**  
Define el tamaño de la letra.

**Unidades Comunes:**

- `px`: Píxeles (fijo).
- `rem`: Relativo al tamaño de fuente del elemento raíz (`html`). Recomendado para accesibilidad.
- `em`: Relativo al tamaño de fuente del elemento padre.

**Ejemplo:**

```css
h1 {
  font-size: 2.5rem; /* 2.5 veces el tamaño base */
}
```

---

## 3. `font-weight`

**Descripción:**  
Define el grosor (peso) de la fuente.

**Valores:**

- `normal` (400).
- `bold` (700).
- Números: 100, 200, ... 900 (depende de si la fuente soporta esos pesos).

**Ejemplo:**

```css
.negrita {
  font-weight: bold;
}
```

---

## 4. `color`

**Descripción:**  
Define el color del texto (primer plano).

**Formatos de Color:**

- Nombre: `red`, `blue`.
- Hexadecimal: `#ff0000`.
- RGB: `rgb(255, 0, 0)`.
- RGBA: `rgba(255, 0, 0, 0.5)` (con transparencia).
- HSL: `hsl(0, 100%, 50%)`.

**Ejemplo:**

```css
p {
  color: #333333;
}
```

---

## 5. `text-align`

**Descripción:**  
Alinea el texto horizontalmente dentro de su contenedor.

**Valores:**

- `left` (Default).
- `right`.
- `center`.
- `justify` (Estira las líneas para que tengan el mismo ancho).

**Ejemplo:**

```css
h1 {
  text-align: center;
}
```

---

## 6. `line-height`

**Descripción:**  
Define la altura de la línea de texto. Es crucial para la legibilidad. Un valor sin unidad (ej. 1.5) es relativo al tamaño de la fuente actual.

**Ejemplo:**

```css
p {
  line-height: 1.6; /* 1.6 veces el tamaño de la fuente */
}
```

---

## 7. `text-decoration`

**Descripción:**  
Añade decoraciones al texto, como subrayado.

**Valores:**

- `none`: Quita decoraciones (muy usado en enlaces `<a>`).
- `underline`: Subrayado.
- `line-through`: Tachado.

**Ejemplo:**

```css
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
```

---

## 8. `text-transform`

**Descripción:**  
Controla la capitalización del texto.

**Valores:**

- `uppercase`: TODO MAYÚSCULAS.
- `lowercase`: todo minúsculas.
- `capitalize`: Primera Letra De Cada Palabra.

**Ejemplo:**

```css
.titulo {
  text-transform: uppercase;
}
```

---

## 9. `letter-spacing`

**Descripción:**  
Define el espacio entre caracteres.

**Ejemplo:**

```css
h1 {
  letter-spacing: 2px;
}
```
