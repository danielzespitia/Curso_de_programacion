# Hoja de Trucos de Comandos Git

## 1. Configuración Inicial (Solo una vez)

Configura tu identidad para que los commits lleven tu nombre.

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## 2. Iniciar un Proyecto

```bash
git init            # Inicializa un repositorio en la carpeta actual
git clone <url>     # Descarga un repositorio existente desde internet
```

## 3. Flujo de Trabajo Diario (Básico)

```bash
git status          # Muestra el estado de los archivos (modificados, nuevos, etc.)
git add <archivo>   # Agrega un archivo específico al área de preparación (staging)
git add .           # Agrega TODOS los archivos modificados al área de preparación
git commit -m "Mensaje" # Guarda los cambios preparados con un mensaje descriptivo
```

## 4. Historial y Diferencias

```bash
git log             # Muestra el historial de commits
git log --oneline   # Muestra el historial resumido (una línea por commit)
git diff            # Muestra qué cambios has hecho en los archivos (antes de add)
```

## 5. Ramas (Branches)

```bash
git branch                # Lista las ramas locales
git branch <nombre>       # Crea una nueva rama
git checkout <nombre>     # Cambia a esa rama
git switch <nombre>       # (Moderno) Cambia a esa rama
git checkout -b <nombre>  # Crea y cambia a la rama en un solo paso
git merge <rama>          # Fusiona la <rama> en la rama actual
```

## 6. Repositorios Remotos (Sincronización)

```bash
git remote add origin <url> # Conecta tu repo local con uno remoto
git push -u origin main     # Sube tus cambios al remoto (primera vez)
git push                    # Sube tus cambios (veces siguientes)
git pull                    # Baja y fusiona los cambios del remoto a tu local
git fetch                   # Baja información del remoto pero NO fusiona (seguro)
```

## 7. Deshacer Cambios (¡Cuidado!)

```bash
git restore <archivo>       # Descarta cambios en un archivo (antes de add)
git restore --staged <archivo> # Saca un archivo del staging (deshace el add)
git reset --hard HEAD       # Vuelve todo al estado del último commit (borra cambios no guardados)
```
