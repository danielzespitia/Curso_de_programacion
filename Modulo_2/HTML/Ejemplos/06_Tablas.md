# Guía Detallada: Tablas en HTML

Las tablas se utilizan para mostrar datos tabulares (filas y columnas). **NO** deben usarse para el diseño (layout) de la página.

---

## 1. `<table>`

**Descripción:**  
Define una tabla HTML. Es el contenedor principal.

**Ejemplo:**

```html
<table>
  <!-- Contenido de la tabla -->
</table>
```

---

## 2. `<tr>` (Table Row)

**Descripción:**  
Define una fila en una tabla.

**Ejemplo:**

```html
<table>
  <tr>
    <td>Celda 1</td>
    <td>Celda 2</td>
  </tr>
</table>
```

---

## 3. `<th>` (Table Header)

**Descripción:**  
Define una celda de encabezado. El texto suele mostrarse en negrita y centrado por defecto.

**Atributos:**

- `scope`: Define si es encabezado de fila (`row`) o columna (`col`). Ayuda a la accesibilidad.

**Ejemplo:**

```html
<tr>
  <th scope="col">Nombre</th>
  <th scope="col">Edad</th>
</tr>
```

---

## 4. `<td>` (Table Data)

**Descripción:**  
Define una celda de datos estándar en una tabla.

**Atributos de fusión:**

- `colspan`: Número de columnas que ocupa la celda.
- `rowspan`: Número de filas que ocupa la celda.

**Ejemplo:**

```html
<tr>
  <td>Juan</td>
  <td>25</td>
</tr>
```

---

## 5. `<thead>`

**Descripción:**  
Agrupa el contenido del encabezado de una tabla. Útil para imprimir (el encabezado se repite en cada página) y para estilos CSS.

**Ejemplo:**

```html
<table>
  <thead>
    <tr>
      <th>Producto</th>
      <th>Precio</th>
    </tr>
  </thead>
  ...
</table>
```

---

## 6. `<tbody>`

**Descripción:**  
Agrupa el contenido del cuerpo (los datos principales) de una tabla.

**Ejemplo:**

```html
<tbody>
  <tr>
    <td>Manzanas</td>
    <td>$1.00</td>
  </tr>
</tbody>
```

---

## 7. `<tfoot>`

**Descripción:**  
Agrupa el contenido del pie de una tabla (ej. totales).

**Ejemplo:**

```html
<tfoot>
  <tr>
    <td>Total</td>
    <td>$10.00</td>
  </tr>
</tfoot>
```

---

## 8. `<caption>`

**Descripción:**  
Define un título o leyenda para la tabla. Debe ser el primer hijo de `<table>`.

**Ejemplo:**

```html
<table>
  <caption>
    Lista de Precios 2025
  </caption>
  ...
</table>
```

---

## 9. `<colgroup>`

**Descripción:**  
Especifica un grupo de una o más columnas para formatear. Permite aplicar estilos a columnas enteras sin repetir estilos en cada celda.

**Ejemplo:**

```html
<table>
  <colgroup>
    <col span="2" style="background-color: red" />
    <col style="background-color: yellow" />
  </colgroup>
  ...
</table>
```

---

## 10. `<col>`

**Descripción:**  
Especifica las propiedades de columna para cada columna dentro de un elemento `<colgroup>`.

**Ejemplo:**
(Ver ejemplo anterior)
