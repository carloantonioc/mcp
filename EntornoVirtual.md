# Guía: Entorno Aislado con `uv` para Pruebas de MCP

Esta guía describe cómo crear un entorno completamente aislado para experimentar con [MCP (Model Context Protocol)](https://github.com/carloantonioc/mcp), sin modificar tu proyecto original ni otros directorios existentes.

## 📋 Contexto

Tienes una estructura como esta y no deseas contaminar ninguna carpeta existente:
```
Proyectos/
├── Ingles/
├── mcp/                  ← ¡NO tocar!
└── Proyecto-Transcriptor/
```

## 🔍 Diferencia clave: `uv init` vs `uv venv`

### `uv init <nombre>` - Inicializa un proyecto Python

Con `uv init <nombre>` en uv 0.9.27, **NO** solo crea la carpeta, sino que también:

- ✅ Crea la carpeta `<nombre>`
- ✅ Dentro, genera un archivo `pyproject.toml` básico con metadatos del proyecto
- ✅ Crea un `README.md` inicial
- ✅ Define la versión de Python a usar (archivo `.python-version`)
- ✅ Opcionalmente, si usas `--package`, también crea una estructura de paquete Python (carpeta con `__init__.py`)

**Resultado de `uv init mcp-pruebas`:**
```
mcp-pruebas/
├── pyproject.toml    ← Configuración del proyecto
├── README.md         ← Documentación inicial
├── .python-version   ← Versión de Python especificada
└── hello.py          ← Archivo de ejemplo (opcional)
```

### `uv venv` - Crea el entorno virtual

Posteriormente, `uv venv`:

- ✅ Crea la carpeta `.venv/` dentro del proyecto
- ✅ Instala un intérprete de Python aislado
- ✅ Configura un espacio aislado para dependencias
- ✅ **NO** modifica `pyproject.toml` automáticamente

**Resultado después de `uv venv`:**
```
mcp-pruebas/
├── .venv/            ← Entorno virtual aislado
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
├── pyproject.toml
├── README.md
└── .python-version
```

> **En resumen:**
> - `uv init` = Inicializa la **estructura del proyecto**
> - `uv venv` = Crea el **entorno virtual aislado**

### 💡 Nota importante sobre `uv venv`

**`uv venv` es opcional si usas comandos modernos de `uv`:**

- ✅ `uv add` crea `.venv/` automáticamente si no existe
- ✅ `uv sync` crea `.venv/` automáticamente si no existe
- ⚠️ `uv pip install` **requiere** que ejecutes `uv venv` primero

**Ejemplo - sin `uv venv` explícito:**
```bash
uv init proyecto
cd proyecto
uv add "paquete"  # ← Crea .venv/ automáticamente
```

**Ejemplo - con `uv venv` explícito (más claro):**
```bash
uv init proyecto
cd proyecto
uv venv            # ← Crea .venv/ explícitamente
uv add "paquete"   # ← Usa el .venv/ existente
```

En esta guía usamos `uv venv` **explícitamente** para mayor claridad didáctica, aunque técnicamente es opcional con `uv add`.

## 📦 `uv add` vs `uv pip install` - ¿Cuál usar?

### `uv add "paquete"` - ✅ Método moderno recomendado
```bash
uv add "mcp[cli]"
```

**Ventajas:**
- ✅ Instala el paquete en `.venv/`
- ✅ **Crea `.venv/` automáticamente si no existe**
- ✅ **Modifica automáticamente** `pyproject.toml`
- ✅ Registra la dependencia en el proyecto
- ✅ Hace el proyecto **reproducible**
- ✅ Otros pueden ejecutar `uv sync` para obtener las mismas dependencias

**Resultado en `pyproject.toml`:**
```toml
[project]
name = "mcp-pruebas"
version = "0.1.0"
dependencies = [
    "mcp[cli]>=1.0.0",  # ← Se agrega automáticamente
]
```

### `uv pip install "paquete"` - ⚠️ Método antiguo (no recomendado)
```bash
uv pip install "mcp[cli]"
```

**Desventajas:**
- ✅ Instala el paquete en `.venv/`
- ❌ **Requiere `uv venv` previo** (error si no existe)
- ❌ **NO** modifica `pyproject.toml`
- ❌ Las dependencias no quedan registradas
- ❌ Otros deben saber qué instalar manualmente
- ❌ Menos reproducible

### Comparación

| Característica | `uv pip install` | `uv add` |
|----------------|------------------|----------|
| Instala paquete | ✅ | ✅ |
| Crea `.venv/` automáticamente | ❌ | ✅ |
| Modifica `pyproject.toml` | ❌ | ✅ |
| Gestión de dependencias | Manual | Automática |
| Reproducible | ❌ | ✅ |
| Recomendado en 2025 | No | **Sí** |

> **💡 Usa `uv add` para proyectos que quieras mantener o compartir**

## 🚀 Paso a paso seguro (usando `uv v0.9.27`)

### 1. Posiciónate en la carpeta raíz

⚠️ **IMPORTANTE:** Asegúrate de estar **FUERA** de cualquier proyecto existente:
```bash
cd /mnt/c/Users/Carlos.Cornejo/Documents/Proyectos
```

❌ **NO ejecutes desde dentro de `mcp/` u otro proyecto**

### 2. Inicializa un nuevo proyecto

Esto crea la carpeta `mcp-pruebas` con toda la estructura base:
```bash
uv init mcp-pruebas
```

**¿Qué acaba de pasar?**
- ✅ Se creó la carpeta `mcp-pruebas/`
- ✅ Se generó `pyproject.toml` con configuración básica
- ✅ Se creó un `README.md` inicial
- ✅ Se definió la versión de Python en `.python-version`

### 3. Entra al nuevo directorio
```bash
cd mcp-pruebas
```

### 4. Crea el entorno virtual (opcional pero recomendado)

Crea explícitamente el espacio aislado para las dependencias:
```bash
uv venv
```

**¿Qué acaba de pasar?**
- ✅ Se creó la carpeta `.venv/` con un Python aislado
- ✅ Este entorno es independiente de tu sistema
- ✅ Las dependencias se instalarán aquí, no globalmente

> **💡 Nota:** Este paso es **opcional** si vas a usar `uv add` (que crea `.venv/` automáticamente), pero lo incluimos para mayor claridad.

### 5. Activa el entorno (opcional)

La activación es necesaria solo si quieres ejecutar comandos del paquete directamente en tu terminal.

**En Linux/macOS/WSL:**
```bash
source .venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

> **Nota:** Verás `(mcp-pruebas)` al inicio de tu línea de comandos cuando esté activado.

### 6. Instala MCP con soporte CLI (método moderno)

Usa `uv add` para registrar la dependencia automáticamente:
```bash
uv add "mcp[cli]"
```

**¿Qué acaba de pasar?**
- ✅ Si no existía `.venv/`, se creó automáticamente
- ✅ MCP se instaló en `.venv/`
- ✅ `pyproject.toml` se actualizó con la dependencia
- ✅ El proyecto es ahora reproducible

**Método alternativo (no recomendado):**
```bash
# Requiere que hayas ejecutado 'uv venv' previamente
uv pip install "mcp[cli]"  # ⚠️ No actualiza pyproject.toml
```

### 7. Verifica la instalación
```bash
uv pip show mcp
```

O verifica el `pyproject.toml`:
```bash
cat pyproject.toml
```

## ✅ Resultado final
```
Proyectos/
├── Ingles/
├── mcp/                  ← sin cambios
├── Proyecto-Transcriptor/
└── mcp-pruebas/          ← ¡nueva y limpia!
    ├── .venv/            ← Entorno virtual (creado con uv venv o automáticamente por uv add)
    ├── pyproject.toml    ← Config del proyecto (creado con uv init, actualizado con uv add)
    ├── .python-version   ← Versión de Python (creado con uv init)
    ├── README.md         ← Documentación (creado con uv init)
    └── hello.py          ← Ejemplo opcional (creado con uv init)
```

**Contenido de `pyproject.toml` después de `uv add`:**
```toml
[project]
name = "mcp-pruebas"
version = "0.1.0"
dependencies = [
    "mcp[cli]>=1.0.0",
]
requires-python = ">=3.12"
```

## 🔒 ¿Por qué es seguro?

- ✅ Ningún archivo se modifica fuera de `mcp-pruebas/`
- ✅ El entorno virtual (`.venv`) está completamente aislado
- ✅ Tu repositorio original (`mcp/`) permanece intacto
- ✅ Las dependencias se instalan solo en el entorno virtual
- ✅ Puedes eliminar toda la carpeta `mcp-pruebas/` sin afectar nada más
- ✅ `pyproject.toml` gestiona las dependencias del proyecto de forma declarativa
- ✅ El proyecto es reproducible gracias a `uv add`

## 🔄 Reproducir el entorno en otro lugar

Si compartes este proyecto o lo clonas en otra máquina:
```bash
# Clona o copia el proyecto
cd mcp-pruebas

# Sincroniza todas las dependencias desde pyproject.toml
# (crea .venv/ automáticamente si no existe)
uv sync  # ✅ Instala todo automáticamente

# Opcionalmente, activa el entorno
source .venv/bin/activate  # Linux/macOS/WSL
```

Con `uv add`, **no necesitas recordar qué paquetes instalar** - todo está en `pyproject.toml`.

## 📦 Alternativa: `uv init --package`

Si quieres crear un paquete Python distribuible:
```bash
uv init --package mcp-pruebas
```

Esto crea una estructura adicional:
```
mcp-pruebas/
├── pyproject.toml
├── README.md
├── .python-version
└── src/
    └── mcp_pruebas/
        └── __init__.py
```

## 🧹 Limpieza (opcional)

Si deseas eliminar el entorno de prueba:
```bash
# Desactiva el entorno primero (si estaba activado)
deactivate

# Vuelve al directorio padre
cd ..

# Elimina la carpeta completa
rm -rf mcp-pruebas/
```

**¿Esto elimina todo rastro?**
- ✅ Sí, elimina el proyecto completo
- ✅ Elimina el entorno virtual
- ✅ Elimina todas las dependencias del proyecto
- ✅ No deja rastro en tu estructura de `Proyectos/`
- ✅ No afecta otros proyectos
- ✅ **Si nunca hiciste `git add`, Git no tiene registro de esto**

> **Nota:** `uv` mantiene una cache global en `~/.cache/uv/` (Linux/macOS) o `%LOCALAPPDATA%\uv\cache\` (Windows) para optimización, pero no contiene nada específico de tu proyecto. Puedes limpiarla con `uv cache clean` si lo deseas.

## 📚 Recursos adicionales

- [Documentación oficial de uv](https://github.com/astral-sh/uv)
- [MCP GitHub Repository](https://github.com/carloantonioc/mcp)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pyproject.toml specification](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

## 💡 Consejos

- Siempre verifica que el entorno virtual esté activado (verás `(mcp-pruebas)` en tu prompt) si necesitas ejecutar comandos del paquete
- Usa `uv pip list` para ver todas las dependencias instaladas
- Para desactivar el entorno: `deactivate`
- El archivo `pyproject.toml` es donde gestionas las dependencias del proyecto
- Agrega `.venv/` a tu `.gitignore` si decides versionar este proyecto
- **Usa `uv add` en lugar de `uv pip install`** para gestión automática de dependencias
- `uv sync` sincroniza las dependencias definidas en `pyproject.toml` (y crea `.venv/` si no existe)
- `uv remove <paquete>` para eliminar una dependencia y actualizar `pyproject.toml`
- **`uv venv` es opcional con `uv add`**, pero útil para entender la estructura

## 🔄 Flujos de trabajo

### Flujo simplificado (método moderno 2025)
```bash
# 1. Iniciar proyecto (fuera de carpetas existentes)
cd /ruta/a/tus/proyectos
uv init nombre-proyecto

# 2. Entrar al proyecto
cd nombre-proyecto

# 3. Agregar dependencias (crea .venv/ automáticamente)
uv add "paquete1"
uv add "paquete2[extras]"

# 4. Trabajar en tu proyecto
# ... tu código aquí ...

# 5. Si alguien más clona tu proyecto
uv sync  # Instala todas las dependencias automáticamente
```

### Flujo explícito (más didáctico)
```bash
# 1. Iniciar proyecto
cd /ruta/a/tus/proyectos
uv init nombre-proyecto

# 2. Entrar al proyecto
cd nombre-proyecto

# 3. Crear entorno virtual explícitamente
uv venv

# 4. Activar entorno
source .venv/bin/activate  # Linux/macOS/WSL
# o
.venv\Scripts\Activate.ps1  # Windows PowerShell

# 5. Agregar dependencias
uv add "paquete1"
uv add "paquete2[extras]"

# 6. Trabajar en tu proyecto
# ... tu código aquí ...

# 7. Desactivar cuando termines
deactivate
```

### ¿Cuál flujo usar?

| Flujo | Cuándo usarlo |
|-------|---------------|
| **Simplificado** | Proyectos nuevos, flujo rápido, confías en automatización |
| **Explícito** | Aprendiendo, necesitas control, documentación didáctica |

Ambos son válidos. El simplificado es más moderno, el explícito es más claro para entender qué hace cada comando.

## ⚠️ Errores comunes a evitar

### ❌ Ejecutar `uv init` dentro de un proyecto existente
```bash
cd mcp/  # ← Ya estás en un proyecto
uv init mcp-pruebas  # ❌ Esto crea la carpeta DENTRO de mcp/
```

### ✅ Ejecutar `uv init` desde la carpeta padre
```bash
cd /ruta/a/Proyectos  # ← Nivel superior
uv init mcp-pruebas   # ✅ Esto crea una carpeta independiente
```

### ❌ Usar `uv pip install` sin crear `.venv/` primero
```bash
uv init proyecto
cd proyecto
uv pip install "paquete"  # ❌ Error: No virtual environment found
```

### ✅ Crear `.venv/` antes de usar `uv pip install`
```bash
uv init proyecto
cd proyecto
uv venv                    # ✅ Crea .venv/ primero
uv pip install "paquete"   # ✅ Ahora funciona
```

### ❌ Usar `uv pip install` en proyectos que vas a mantener
```bash
uv pip install "mcp[cli]"  # ❌ No actualiza pyproject.toml
```

### ✅ Usar `uv add` para gestión automática
```bash
uv add "mcp[cli]"  # ✅ Actualiza pyproject.toml automáticamente
```

---

¡Listo para experimentar sin riesgos! 🎉