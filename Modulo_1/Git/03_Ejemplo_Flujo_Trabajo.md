# Ejemplo Práctico: Flujo de Trabajo Paso a Paso

Sigue estos pasos en tu terminal para practicar un ciclo completo de trabajo.

## Paso 1: Crear el proyecto

```bash
# Crear una carpeta
mkdir MiProyecto
cd MiProyecto

# Iniciar Git
git init
```

## Paso 2: Primer Commit

Crea un archivo llamado `hola.txt` con algún texto.

```bash
# Verificar estado (verás el archivo en rojo/untracked)
git status

# Preparar el archivo
git add hola.txt

# Verificar estado (verás el archivo en verde/staged)
git status

# Guardar la foto (commit)
git commit -m "Crear archivo de saludo inicial"
```

## Paso 3: Hacer cambios

Edita `hola.txt` y agrega otra línea de texto.

```bash
# Ver qué cambió
git diff

# Agregar y confirmar en un solo paso (atajo para archivos ya rastreados)
git commit -am "Agregar segunda linea al saludo"
```

## Paso 4: Trabajar en una Rama (Feature Branch)

Imagina que quieres probar algo nuevo sin dañar lo que ya hiciste.

```bash
# Crear y cambiar a la rama 'experimento'
git checkout -b experimento

# Crear un nuevo archivo
echo "Esto es una prueba" > prueba.txt

# Guardar cambios en esta rama
git add .
git commit -m "Añadir archivo de prueba en rama experimento"
```

## Paso 5: Volver y Fusionar

El experimento fue un éxito, vamos a llevarlo a la rama principal.

```bash
# Volver a la rama principal
git checkout main
# (Si miras tus archivos ahora, 'prueba.txt' habrá desaparecido, ¡es magia!)

# Fusionar los cambios de 'experimento' hacia 'main'
git merge experimento

# (Ahora 'prueba.txt' aparece en main)
```

## Paso 6: Limpieza

Ya no necesitas la rama de experimento.

```bash
git branch -d experimento
```
