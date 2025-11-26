# Guía Detallada: Formularios e Interacción

Estas etiquetas permiten crear interfaces interactivas para recolectar datos del usuario.

---

## 1. `<form>`

**Descripción:**  
Define un formulario HTML para la entrada de datos del usuario.

**Atributos Clave:**

- `action`: URL a donde se envían los datos.
- `method`: Método HTTP (`GET` o `POST`).

**Ejemplo:**

```html
<form action="/enviar-datos" method="POST">
  <!-- Inputs aquí -->
</form>
```

---

## 2. `<input>`

**Descripción:**  
El elemento más versátil de los formularios. Su comportamiento cambia drásticamente según el atributo `type`.

**Tipos Comunes (`type`):**

- `text`: Campo de texto de una línea.
- `password`: Oculta los caracteres.
- `email`: Valida formato de correo.
- `number`: Solo permite números.
- `checkbox`: Casilla de verificación (selección múltiple).
- `radio`: Botón de opción (selección única en un grupo).
- `date`: Selector de fecha.
- `file`: Subida de archivos.
- `submit`: Botón para enviar el formulario.

**Ejemplo:**

```html
<input type="text" placeholder="Nombre" />
<input type="password" placeholder="Contraseña" />
<input type="submit" value="Enviar" />
```

---

## 3. `<label>`

**Descripción:**  
Define una etiqueta para un elemento `<input>`. Es crucial para la accesibilidad y usabilidad (al hacer clic en el texto del label, se activa el input).

**Vinculación:**
Se usa el atributo `for` en el label que debe coincidir con el `id` del input.

**Ejemplo:**

```html
<label for="usuario">Nombre de Usuario:</label>
<input type="text" id="usuario" name="usuario" />
```

---

## 4. `<textarea>`

**Descripción:**  
Define un campo de entrada de texto multilínea.

**Atributos:**

- `rows`: Número de líneas visibles.
- `cols`: Ancho visible en caracteres.

**Ejemplo:**

```html
<textarea name="mensaje" rows="4" cols="50">
  Escribe tu mensaje aquí...
</textarea>
```

---

## 5. `<button>`

**Descripción:**  
Define un botón clickeable.

**Tipos (`type`):**

- `submit`: Envía el formulario (por defecto dentro de un form).
- `reset`: Reinicia el formulario.
- `button`: Botón genérico (para usar con JS).

**Diferencia con `<input type="button">`:**  
`<button>` puede tener contenido HTML dentro (imágenes, texto en negrita), `<input>` solo texto plano en `value`.

**Ejemplo:**

```html
<button type="submit"><strong>Enviar</strong> Ahora</button>
```

---

## 6. `<select>`

**Descripción:**  
Crea una lista desplegable (drop-down list).

**Ejemplo:**

```html
<select name="coches" id="coches">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
</select>
```

---

## 7. `<option>`

**Descripción:**  
Define una opción dentro de un `<select>`, `<optgroup>` o `<datalist>`.

**Atributos:**

- `value`: El valor que se envía al servidor.
- `selected`: Pre-selecciona esta opción.

**Ejemplo:**

```html
<option value="audi" selected>Audi</option>
```

---

## 8. `<fieldset>`

**Descripción:**  
Agrupa elementos relacionados dentro de un formulario, dibujando un recuadro alrededor de ellos.

**Ejemplo:**

```html
<fieldset>
  <legend>Datos Personales</legend>
  <input type="text" placeholder="Nombre" />
</fieldset>
```

---

## 9. `<legend>`

**Descripción:**  
Define un título para el elemento `<fieldset>`.

**Ejemplo:**
(Ver ejemplo anterior)

---

## 10. `<datalist>`

**Descripción:**  
Especifica una lista de opciones predefinidas para un elemento `<input>`. Ofrece funcionalidad de "autocompletar".

**Ejemplo:**

```html
<input list="navegadores" />
<datalist id="navegadores">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Edge"></option>
</datalist>
```
