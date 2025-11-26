# Guía Detallada: Transiciones, Animaciones y Transformaciones CSS

Estas propiedades permiten dar vida a la web con movimiento y efectos visuales.

---

## 1. `transition`

**Descripción:**  
Permite cambiar valores de propiedades suavemente (durante un tiempo determinado) en lugar de instantáneamente. Es un shorthand.

**Sintaxis:**
`property duration timing-function delay`

**Ejemplo:**

```css
.boton {
  background-color: blue;
  transition: background-color 0.3s ease;
}
.boton:hover {
  background-color: red; /* El cambio tardará 0.3 segundos */
}
```

---

## 2. `transform`

**Descripción:**  
Aplica una transformación 2D o 3D a un elemento. No afecta al flujo del documento (los elementos vecinos no se mueven).

**Funciones Comunes:**

- `translate(x, y)`: Mueve el elemento.
- `scale(x, y)`: Cambia el tamaño.
- `rotate(angle)`: Rota el elemento.
- `skew(x-angle, y-angle)`: Sesga (inclina) el elemento.

**Ejemplo:**

```css
.tarjeta:hover {
  transform: scale(1.1) rotate(5deg);
}
```

---

## 3. `animation`

**Descripción:**  
Aplica una animación definida por `@keyframes`. Es un shorthand para varias propiedades de animación.

**Sintaxis:**
`name duration timing-function delay iteration-count direction fill-mode`

**Ejemplo:**

```css
.caja {
  animation: mover 2s infinite;
}
```

---

## 4. `@keyframes`

**Descripción:**  
Define los pasos de una animación. Especifica qué estilos tiene el elemento en determinados momentos (porcentajes) de la animación.

**Ejemplo:**

```css
@keyframes mover {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(100px);
  }
  100% {
    transform: translateX(0);
  }
}
```

---

## 5. `animation-duration`

**Descripción:**  
Define cuánto tiempo tarda una animación en completar un ciclo.

**Ejemplo:**

```css
div {
  animation-duration: 3s;
}
```

---

## 6. `animation-delay`

**Descripción:**  
Especifica un retraso antes de comenzar la animación.

**Ejemplo:**

```css
div {
  animation-delay: 1s;
}
```

---

## 7. `animation-iteration-count`

**Descripción:**  
Especifica cuántas veces se debe reproducir la animación.

**Valores:**

- Número (ej. `3`).
- `infinite` (para siempre).

**Ejemplo:**

```css
div {
  animation-iteration-count: infinite;
}
```

---

## 8. `transition-timing-function` / `animation-timing-function`

**Descripción:**  
Especifica la curva de velocidad de la transición/animación.

**Valores:**

- `ease` (lento-rápido-lento).
- `linear` (velocidad constante).
- `ease-in` (empieza lento).
- `ease-out` (termina lento).
- `cubic-bezier(n,n,n,n)` (personalizado).

**Ejemplo:**

```css
div {
  transition-timing-function: linear;
}
```
