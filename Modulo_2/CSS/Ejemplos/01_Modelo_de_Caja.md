# Guía Detallada: El Modelo de Caja (Box Model) en CSS

El Modelo de Caja es el concepto fundamental de diseño en CSS. Cada elemento en una página web es considerado una caja rectangular.

---

## 1. `width` y `height`

**Descripción:**
Definen el ancho y la altura del área de contenido de un elemento.

**Valores Comunes:**

- `px`: Píxeles (absoluto).
- `%`: Porcentaje del contenedor padre.
- `vw` / `vh`: Porcentaje del viewport (ventana del navegador).
- `auto`: El navegador calcula el tamaño (por defecto).

**Ejemplo:**

```css
div {
  width: 100%;
  height: 200px;
}
```

---

## 2. `padding` (Relleno)

**Descripción:**
Es el espacio **interno** entre el contenido del elemento y su borde. El padding toma el color de fondo del elemento.

**Sintaxis (Shorthand):**

- `padding: 10px;` (Todos los lados).
- `padding: 10px 20px;` (Arriba/Abajo 10px, Izquierda/Derecha 20px).
- `padding: 10px 20px 30px 40px;` (Arriba, Derecha, Abajo, Izquierda - Sentido horario).

**Propiedades individuales:**

- `padding-top`, `padding-right`, `padding-bottom`, `padding-left`.

**Ejemplo:**

```css
.caja {
  padding: 20px; /* Espacio interno */
}
```

---

## 3. `margin` (Margen)

**Descripción:**
Es el espacio **externo** alrededor del elemento, fuera de su borde. Es transparente. Se usa para separar elementos entre sí.

**Truco de Centrado:**
`margin: 0 auto;` centra horizontalmente un elemento de bloque con ancho definido.

**Colapso de Márgenes:**
Los márgenes verticales adyacentes a veces se combinan en uno solo (el mayor de los dos).

**Ejemplo:**

```css
.tarjeta {
  margin-bottom: 20px; /* Separación con el siguiente elemento */
}
```

---

## 4. `border` (Borde)

**Descripción:**
Define la línea que rodea el padding y el contenido.

**Sintaxis (Shorthand):**
`border: [ancho] [estilo] [color];`

**Estilos comunes:** `solid`, `dashed`, `dotted`, `none`.

**Ejemplo:**

```css
.boton {
  border: 2px solid red;
}
```

---

## 5. `box-sizing`

**Descripción:**
Controla cómo se calcula el ancho y alto total de un elemento. Esta es quizás la propiedad más importante para evitar dolores de cabeza con el layout.

**Valores:**

- `content-box` (Default): El `width` solo incluye el contenido. Padding y Border se suman al tamaño total.
  - _Ancho Total = width + padding + border_.
- `border-box` (Recomendado): El `width` incluye el contenido, el padding y el borde.
  - _Ancho Total = width_.

**Ejemplo (Reset Global):**

```css
* {
  box-sizing: border-box;
}
```

---

## 6. `max-width` / `min-width`

**Descripción:**Establecen restricciones al ancho de un elemento.

- `max-width`: El elemento no puede ser más ancho que esto (útil para responsividad, para que no se desborde en pantallas pequeñas).
- `min-width`: El elemento no puede ser más estrecho que esto.

**Ejemplo:**

```css
img {
  max-width: 100%; /* La imagen nunca será más ancha que su contenedor */
  height: auto;
}
```

---

## 7. `overflow`

**Descripción:**
Controla qué sucede si el contenido es demasiado grande para caber en el área del elemento.

**Valores:**

- `visible` (Default): El contenido se desborda y es visible fuera de la caja.
- `hidden`: El desbordamiento se recorta y no es visible.
- `scroll`: Añade barras de desplazamiento siempre.
- `auto`: Añade barras de desplazamiento solo si es necesario.

**Ejemplo:**

```css
.contenedor-scroll {
  height: 100px;
  overflow: auto;
}
```
