# Activación de entorno virtual con `uv`

**Base:** el entorno `.venv` ya está creado.

---

## 📌 Paso a paso (uso diario)

### 1️⃣ Abrir terminal

### 2️⃣ Entrar a la carpeta del proyecto
```bash
cd ruta/del/proyecto
```

### 3️⃣ Activar el entorno virtual
```bash
source .venv/bin/activate
```

### 4️⃣ Verificación (obligatoria)
- Si aparece algo como:
```text
(mcp-pruebas)
```
✔️ El entorno está **activo correctamente**.

> Nota: el texto entre paréntesis corresponde al **nombre del proyecto**, no al nombre de la carpeta `.venv`.

- Verificación adicional (opcional):
```bash
which python
```
Debe apuntar a una ruta similar a:
```text
.../tu_proyecto/.venv/bin/python
```

### 5️⃣ Trabajar normalmente
```bash
uv pip install paquete
python script.py
```

### 6️⃣ Salir del entorno
```bash
deactivate
```

---

## 🧠 Ayuda memoria rápida
```text
cd proyecto
source .venv/bin/activate
ver (nombre_proyecto)
```

---

## ℹ️ Opcional: mostrar `.venv` en el prompt
Si prefieres que el prompt muestre `(.venv)` en lugar del nombre del proyecto:
```bash
uv venv .venv --prompt .venv
```
Luego activar nuevamente:
```bash
source .venv/bin/activate
```

