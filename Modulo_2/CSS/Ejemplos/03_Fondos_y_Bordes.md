# Guía Detallada: Fondos, Bordes y Efectos Visuales en CSS

Estas propiedades permiten controlar el aspecto visual de las cajas, añadiendo colores, imágenes, bordes redondeados y sombras.

---

## 1. `background-color`

**Descripción:**  
Establece el color de fondo de un elemento.

**Ejemplo:**

```css
body {
  background-color: #f0f0f0;
}
```

---

## 2. `background-image`

**Descripción:**  
Establece una o más imágenes de fondo para un elemento.

**Sintaxis:**
`url('ruta/a/la/imagen.jpg')`

**Gradientes:**
También se usa para crear degradados: `linear-gradient(...)`.

**Ejemplo:**

```css
div {
  background-image: url("fondo.png");
}
.gradiente {
  background-image: linear-gradient(to right, red, yellow);
}
```

---

## 3. `background-size`

**Descripción:**  
Especifica el tamaño de la imagen de fondo.

**Valores:**

- `auto`: Tamaño original.
- `cover`: Escala la imagen para cubrir todo el contenedor (puede recortarse).
- `contain`: Escala la imagen para que se vea completa (puede dejar espacios).
- `100% 100%`: Estira la imagen.

**Ejemplo:**

```css
.hero {
  background-size: cover;
}
```

---

## 4. `background-position`

**Descripción:**  
Establece la posición inicial de la imagen de fondo.

**Valores:**
`center`, `top`, `bottom`, `left`, `right`, o porcentajes/píxeles.

**Ejemplo:**

```css
div {
  background-position: center center;
}
```

---

## 5. `background-repeat`

**Descripción:**  
Define si la imagen de fondo se repite y cómo.

**Valores:**

- `repeat` (Default): Se repite en mosaico.
- `no-repeat`: No se repite.
- `repeat-x`: Solo horizontal.
- `repeat-y`: Solo vertical.

**Ejemplo:**

```css
div {
  background-repeat: no-repeat;
}
```

---

## 6. `border-radius`

**Descripción:**  
Define el radio de las esquinas del borde de un elemento. Permite crear esquinas redondeadas o círculos.

**Valores:**

- `px`: Radio en píxeles.
- `%`: 50% crea un círculo perfecto (si el elemento es cuadrado).

**Ejemplo:**

```css
.boton {
  border-radius: 5px;
}
.circulo {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
```

---

## 7. `box-shadow`

**Descripción:**  
Añade efectos de sombra alrededor del marco de un elemento.

**Sintaxis:**
`offset-x offset-y blur-radius spread-radius color`

**Ejemplo:**

```css
.tarjeta {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
}
```

---

## 8. `opacity`

**Descripción:**  
Establece el nivel de opacidad (transparencia) de un elemento.

**Valores:**
De `0.0` (totalmente transparente) a `1.0` (totalmente opaco).

**Nota:**
Afecta a todo el elemento, incluido su contenido (texto). Si solo quieres fondo transparente, usa `rgba` en `background-color`.

**Ejemplo:**

```css
img:hover {
  opacity: 0.8;
}
```

---

## 9. `cursor`

**Descripción:**  
Especifica el tipo de cursor del ratón que se muestra cuando el puntero está sobre un elemento.

**Valores Comunes:**

- `pointer`: Mano (indica enlace o botón).
- `default`: Flecha normal.
- `text`: I de texto.
- `not-allowed`: Prohibido.

**Ejemplo:**

```css
.boton-falso {
  cursor: pointer;
}
```
