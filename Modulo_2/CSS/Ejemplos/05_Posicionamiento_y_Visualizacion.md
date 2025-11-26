# Guía Detallada: Posicionamiento y Visualización

Controla cómo se comportan los elementos en el flujo del documento y su visibilidad.

---

## 1. `display`

**Descripción:**  
Especifica el tipo de caja de renderizado de un elemento.

**Valores Clave:**

- `block`: Ocupa todo el ancho, empieza en nueva línea (ej. `div`, `p`).
- `inline`: Solo ocupa el ancho necesario, no rompe línea (ej. `span`, `a`).
- `inline-block`: Como inline, pero permite definir ancho y alto.
- `none`: Elimina el elemento del documento (no ocupa espacio).

**Ejemplo:**

```css
.oculto {
  display: none;
}
.menu-item {
  display: inline-block;
}
```

---

## 2. `position`

**Descripción:**  
Especifica el método de posicionamiento de un elemento.

**Valores:**

- `static` (Default): Flujo normal. `top`, `left`, etc., no le afectan.
- `relative`: Relativo a su posición normal. Mantiene su espacio original.
- `absolute`: Relativo al ancestro posicionado más cercano (no static). Se sale del flujo normal.
- `fixed`: Relativo a la ventana del navegador (viewport). Se queda fijo al hacer scroll.
- `sticky`: Alterna entre relative y fixed dependiendo del scroll.

**Ejemplo:**

```css
.header-fijo {
  position: fixed;
  top: 0;
  width: 100%;
}
```

---

## 3. `top`, `right`, `bottom`, `left`

**Descripción:**  
Determinan la posición final de un elemento posicionado (que no sea `static`).

**Ejemplo:**

```css
.boton-flotante {
  position: fixed;
  bottom: 20px;
  right: 20px;
}
```

---

## 4. `z-index`

**Descripción:**  
Especifica el orden de apilamiento (eje Z) de los elementos posicionados. Un número mayor se muestra encima de uno menor.

**Nota:** Solo funciona en elementos con `position` (relative, absolute, fixed, sticky).

**Ejemplo:**

```css
.modal {
  z-index: 1000; /* Muy por encima de todo */
}
```

---

## 5. `visibility`

**Descripción:**  
Muestra u oculta un elemento sin cambiar el layout.

**Valores:**

- `visible` (Default).
- `hidden`: El elemento es invisible, pero **sigue ocupando espacio**.

**Diferencia con `display: none`:**
`display: none` quita el elemento del flujo (no ocupa espacio). `visibility: hidden` solo lo hace transparente.

**Ejemplo:**

```css
.fantasma {
  visibility: hidden;
}
```

---

## 6. `float`

**Descripción:**  
Empuja un elemento a la izquierda o derecha, permitiendo que el texto y elementos en línea lo rodeen. (Menos usado hoy en día para layout gracias a Flexbox/Grid, pero útil para imágenes en texto).

**Valores:**
`left`, `right`, `none`.

**Ejemplo:**

```css
img {
  float: left;
  margin-right: 10px;
}
```

---

## 7. `clear`

**Descripción:**  
Especifica qué elementos pueden flotar al lado del elemento limpiado y en qué lado. Se usa para arreglar problemas de layout causados por `float`.

**Valores:**
`left`, `right`, `both`.

**Ejemplo:**

```css
.footer {
  clear: both; /* Asegura que el footer vaya debajo de elementos flotantes */
}
```

---

## 8. `object-fit`

**Descripción:**  
Especifica cómo el contenido de un elemento reemplazado (como `<img>` o `<video>`) debe ajustarse a su contenedor.

**Valores:**

- `fill`: Estira (deforma).
- `contain`: Cabe dentro sin recortar (mantiene proporción).
- `cover`: Cubre todo el contenedor (recorta si es necesario, mantiene proporción).

**Ejemplo:**

```css
img {
  width: 100%;
  height: 200px;
  object-fit: cover; /* Ideal para tarjetas de imágenes */
}
```
