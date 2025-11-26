# Introducción a Git

## ¿Qué es Git?

Git es un **sistema de control de versiones distribuido**. Imagínalo como una "máquina del tiempo" para tu código. Te permite:

- Guardar el historial de cambios de tus archivos.
- Volver a versiones anteriores si algo sale mal.
- Trabajar en equipo sin sobrescribir el trabajo de otros.
- Experimentar con nuevas funciones (ramas) sin romper el código principal.

## Conceptos Clave

### 1. Repositorio (Repo)

Es la carpeta donde vive tu proyecto y donde Git almacena todo el historial. Puede ser **local** (en tu computadora) o **remoto** (en servidores como GitHub, GitLab).

### 2. Commit (Confirmación)

Es como una "foto" o instantánea de tu proyecto en un momento específico. Cada commit tiene un identificador único (hash) y un mensaje que explica qué cambios se hicieron.
_Analogía:_ Es como guardar partida en un videojuego.

### 3. Staging Area (Área de preparación)

Es una zona intermedia donde eliges qué cambios quieres incluir en tu próxima "foto" (commit). No todos los cambios en tus archivos van automáticamente al commit; primero debes agregarlos aquí.
_Analogía:_ Es como poner los productos en el carrito de compras antes de pagar (hacer el commit).

### 4. Rama (Branch)

Es una línea de tiempo paralela. La rama principal suele llamarse `main` o `master`. Puedes crear ramas para trabajar en nuevas características sin afectar la rama principal.
_Analogía:_ Es como un universo alternativo donde pruebas cosas nuevas. Si funcionan, las fusionas (merge) con el universo original.

### 5. Merge (Fusión)

Es el proceso de unir una rama con otra. Por ejemplo, cuando terminas una nueva función en tu rama `nueva-funcion`, la fusionas con `main` para integrarla al proyecto final.

### 6. Remote (Remoto)

Es la versión de tu repositorio alojada en internet (GitHub, etc.).

- **Push:** Subir tus cambios locales al remoto.
- **Pull:** Bajar los cambios del remoto a tu computadora.

## Estados de un archivo en Git

1.  **Modified (Modificado):** Has cambiado el archivo pero no lo has guardado en Git todavía.
2.  **Staged (Preparado):** Has marcado el archivo modificado para que vaya en el próximo commit.
3.  **Committed (Confirmado):** Los cambios están guardados seguramente en la base de datos de Git.
