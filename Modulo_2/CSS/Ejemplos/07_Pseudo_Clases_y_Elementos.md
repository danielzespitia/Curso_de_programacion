# Guía Detallada: Pseudo-clases y Pseudo-elementos

Aunque no son "propiedades" en sí mismas, son selectores fundamentales que se usan junto con propiedades para aplicar estilos en estados específicos o a partes específicas de un elemento.

---

## 1. `:hover`

**Descripción:**  
Selecciona un elemento cuando el usuario pasa el ratón sobre él. Es esencial para la interactividad.

**Ejemplo:**

```css
a:hover {
  color: orange;
  text-decoration: underline;
}
```

---

## 2. `:active`

**Descripción:**  
Selecciona un elemento en el momento en que está siendo activado (ej. mientras se hace clic en un botón).

**Ejemplo:**

```css
button:active {
  transform: scale(0.98); /* Efecto de presionar */
}
```

---

## 3. `:focus`

**Descripción:**  
Selecciona un elemento que tiene el foco (ej. un input donde se está escribiendo). Vital para accesibilidad y formularios.

**Ejemplo:**

```css
input:focus {
  border-color: blue;
  outline: none; /* Quita el borde por defecto del navegador */
}
```

---

## 4. `:first-child` / `:last-child`

**Descripción:**  
`:first-child`: Selecciona el primer hijo de su padre.
`:last-child`: Selecciona el último hijo de su padre.

**Ejemplo:**

```css
li:first-child {
  font-weight: bold;
}
li:last-child {
  border-bottom: none;
}
```

---

## 5. `:nth-child(n)`

**Descripción:**  
Selecciona elementos basándose en su posición en un grupo de hermanos.

**Fórmulas:**

- `2`: El segundo elemento.
- `odd`: Impares (1, 3, 5...).
- `even`: Pares (2, 4, 6...).
- `3n`: Cada tercer elemento.

**Ejemplo:**

```css
/* Filas cebra en una tabla */
tr:nth-child(even) {
  background-color: #f2f2f2;
}
```

---

## 6. `::before`

**Descripción:**  
Crea un pseudo-elemento que es el primer hijo del elemento seleccionado. Se usa a menudo para añadir contenido cosmético con la propiedad `content`.

**Ejemplo:**

```css
.precio::before {
  content: "$";
  color: green;
}
```

---

## 7. `::after`

**Descripción:**  
Crea un pseudo-elemento que es el último hijo del elemento seleccionado.

**Ejemplo:**

```css
a[target="_blank"]::after {
  content: " ↗"; /* Icono de enlace externo */
  font-size: 0.8em;
}
```

---

## 8. `::placeholder`

**Descripción:**  
Selecciona el texto del placeholder (texto de ayuda) de un input o textarea.

**Ejemplo:**

```css
input::placeholder {
  color: #999;
  font-style: italic;
}
```

---

## 9. `:not(selector)`

**Descripción:**  
Selecciona todo elemento que NO coincida con el selector especificado.

**Ejemplo:**

```css
/* Todos los inputs excepto los de tipo submit */
input:not([type="submit"]) {
  width: 100%;
}
```
