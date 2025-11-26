# Guía Detallada: Layout Moderno (Flexbox y Grid)

Estas son las herramientas más potentes para crear diseños de página complejos y responsivos.

---

## 1. `display: flex` (Flexbox)

**Descripción:**  
Activa el modelo Flexbox en un contenedor. Convierte a los hijos directos en "items flexibles". Es ideal para diseños unidimensionales (una fila o una columna).

**Ejemplo:**

```css
.contenedor-flex {
  display: flex;
}
```

---

## 2. `flex-direction`

**Descripción:**  
Define la dirección en la que se colocan los items flexibles.

**Valores:**

- `row` (Default): Horizontal, de izquierda a derecha.
- `column`: Vertical, de arriba a abajo.
- `row-reverse`: Horizontal invertido.
- `column-reverse`: Vertical invertido.

**Ejemplo:**

```css
.columna {
  flex-direction: column;
}
```

---

## 3. `justify-content`

**Descripción:**  
Alinea los items a lo largo del **eje principal** (horizontal si es `row`, vertical si es `column`).

**Valores:**

- `flex-start`: Al inicio.
- `flex-end`: Al final.
- `center`: Al centro.
- `space-between`: Distribuye espacio entre items (primero al inicio, último al final).
- `space-around`: Espacio alrededor de cada item.

**Ejemplo:**

```css
.menu {
  justify-content: space-between;
}
```

---

## 4. `align-items`

**Descripción:**  
Alinea los items a lo largo del **eje transversal** (perpendicular al principal).

**Valores:**

- `stretch` (Default): Estira los items para llenar el contenedor.
- `flex-start`: Al inicio del eje transversal.
- `flex-end`: Al final.
- `center`: Centrado en el eje transversal.

**Ejemplo:**

```css
.centrado-vertical {
  display: flex;
  align-items: center;
  height: 100px;
}
```

---

## 5. `flex-wrap`

**Descripción:**  
Especifica si los items flexibles deben envolverse (saltar a la siguiente línea) si no hay espacio suficiente.

**Valores:**

- `nowrap` (Default): Todos en una línea (pueden encogerse).
- `wrap`: Saltan a múltiples líneas.

**Ejemplo:**

```css
.galeria {
  flex-wrap: wrap;
}
```

---

## 6. `gap` (Flex y Grid)

**Descripción:**  
Define el espacio (hueco) entre filas y columnas. Funciona tanto en Flexbox como en Grid.

**Ejemplo:**

```css
.contenedor {
  display: flex;
  gap: 20px; /* Espacio entre elementos */
}
```

---

## 7. `display: grid` (CSS Grid)

**Descripción:**  
Activa el modelo Grid. Es ideal para diseños bidimensionales (filas y columnas a la vez).

**Ejemplo:**

```css
.contenedor-grid {
  display: grid;
}
```

---

## 8. `grid-template-columns`

**Descripción:**  
Define el número y ancho de las columnas.

**Unidad `fr`:**  
Fracción del espacio disponible.

**Ejemplo:**

```css
.grid {
  /* 3 columnas: 1ra 100px, 2da flexible, 3ra flexible */
  grid-template-columns: 100px 1fr 1fr;

  /* 3 columnas iguales */
  grid-template-columns: repeat(3, 1fr);
}
```

---

## 9. `grid-template-rows`

**Descripción:**  
Define la altura de las filas.

**Ejemplo:**

```css
.grid {
  grid-template-rows: 100px auto 50px;
}
```

---

## 10. `flex` (Shorthand)

**Descripción:**  
Propiedad abreviada para `flex-grow`, `flex-shrink` y `flex-basis` en los items hijos.

**Valores Comunes:**

- `flex: 1`: El item crecerá para ocupar todo el espacio disponible.

**Ejemplo:**

```css
.sidebar {
  flex: 1; /* Ocupa 1 parte */
}
.contenido {
  flex: 3; /* Ocupa 3 partes (3 veces más ancho) */
}
```
