# 📝 Examen Práctico de JavaScript: Módulos 1-3

**Instrucciones:**  
Resuelve los siguientes 10 ejercicios. Escribe el código JavaScript necesario para cumplir con los requisitos de cada problema. Se evaluará la correcta utilización de variables, operadores, condicionales y bucles.

---

## 1️⃣ Perfil de Producto

Declara variables para describir un producto de una tienda online:

- Usa `const` para el nombre del producto (`nombreProducto`), que será **"Tablet 10 pulgadas"**.
- Usa `let` para el precio (`precio`), que será **450.99**.
- Usa `let` para la cantidad en stock (`stock`), que será **25**.
- Usa `const` para si el producto tiene envío gratis (`envioGratis`), que será **true**.

Finalmente, muestra cada una de estas variables en la consola con un mensaje descriptivo.  
Ejemplo: `Nombre del producto: Tablet 10 pulgadas`.

---

## 2️⃣ Cálculo de Total de Compra

Usando las variables del ejercicio anterior, un cliente compra **2 tablets**.  
- Calcula el subtotal (`precio * cantidad`).  
- Luego, calcula el total final añadiendo un **7% de impuesto** sobre el subtotal.  
- Muestra en la consola el subtotal y el total final formateado a 2 decimales.

---

## 3️⃣ Verificación de Edad para Conducir

Crea una variable `edadUsuario` con un valor de **20**.  
Usando una estructura `if/else`, determina si el usuario es mayor de edad para conducir (edad mínima 18 años).

- Si es mayor o igual a 18, muestra en consola: **"Puedes obtener tu licencia de conducir."**
- Si es menor de 18, muestra: **"Aún no tienes la edad para obtener la licencia."**

---

## 4️⃣ Sistema de Semáforo

Declara una variable `colorSemaforo` y asígnale un valor ("verde", "amarillo" o "rojo").  
Usando `if`, `else if` y `else`, crea un programa que muestre un mensaje diferente según el color:

- Si es "verde", muestra **"Puede avanzar."**
- Si es "amarillo", muestra **"Reduzca la velocidad, precaución."**
- Si es "rojo", muestra **"Debe detenerse."**
- Si es cualquier otro color, muestra **"Color no válido."**

---

## 5️⃣ Menú del Día con switch

Crea una variable `diaSemana` con el valor **3**.  
Usando una estructura `switch`, crea un programa que muestre el plato del día según el número:

- **Lunes:** Lentejas
- **Martes:** Pollo al horno
- **Miércoles:** Pescado a la plancha
- **Jueves:** Pasta
- **Viernes:** Paella

Para cualquier otro número, debe mostrar **"Día no válido para menú."**

---

## 6️⃣ Números Pares con for

Usando un bucle `for`, escribe un programa que imprima en la consola **todos los números pares del 2 al 20** (inclusive).

---

## 7️⃣ Cuenta Regresiva con while

Usando un bucle `while`, crea un programa que simule una cuenta regresiva para un cohete.  
Debe imprimir en la consola los números del **10 al 1**, y al final, imprimir **"¡Despegue!"**.

---

## 9️⃣ Suma de los Primeros 100 Números

Crea una variable `sumaTotal` inicializada en **0**.  
Usando un bucle `for`, calcula la suma de todos los números del **1 al 100** y almacena el resultado en `sumaTotal`.  
Al final del bucle, imprime el valor de `sumaTotal` en la consola.

---

## 🔟 Acceso a Evento Exclusivo

Un usuario quiere entrar a un evento. Las condiciones son:  
- Ser mayor de edad (`edad >= 18`) **Y**  
- Tener una entrada (`tieneEntrada = true`)

Declara dos variables:  
- `edad` con valor **19**  
- `tieneEntrada` con valor **false**

Usando operadores lógicos (`&&`), evalúa si el usuario puede pasar.  
Muestra en consola **"Acceso concedido"** o **"Acceso denegado"** según el resultado.  
Cambia los valores de las variables para probar ambos casos.

---