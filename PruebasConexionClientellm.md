# Manual: Crear entorno desde cero con `uv init`

## 1. Abrir terminal y ejecutar

```bash
uv init nombre-del-proyecto
```

Esto crea una carpeta llamada `nombre-del-proyecto` con:
- Un entorno virtual (`.venv`)
- Un archivo `pyproject.toml`
- Una estructura básica en `src/`

---

## 2. Entrar al directorio del proyecto

```bash
cd nombre-del-proyecto
```

---

## 3. El entorno ya está listo para usar

Puedes instalar paquetes con:

```bash
uv add nombre-paquete
```

---

## ⚠️ Nota Importante

**Aún no crea el entorno virtual, solo genera la estructura del proyecto:**

```
drwxrwxrwx 1 carlos carlos 4096 Feb  3 11:24 ./
drwxrwxrwx 1 carlos carlos 4096 Feb  3 11:24 ../
drwxrwxrwx 1 carlos carlos 4096 Feb  3 11:24 .git/
-rwxrwxrwx 1 carlos carlos  109 Feb  3 11:24 .gitignore*
-rwxrwxrwx 1 carlos carlos    5 Feb  3 11:24 .python-version*
-rwxrwxrwx 1 carlos carlos    0 Feb  3 11:24 README.md*
-rwxrwxrwx 1 carlos carlos   95 Feb  3 11:24 main.py*
-rwxrwxrwx 1 carlos carlos  163 Feb  3 11:24 pyproject.toml*
```

Al crear una librería recién lo creará con el comando (`uv add`), pero si se quiere crear el ambiente sin instalar nada se puede hacer con:

```bash
uv venv
```

**Salida del comando:**

```bash
carlos@SGKX-P2-04V0:/mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient$ uv venv
Using CPython 3.10.12 interpreter at: /usr/bin/python3.10
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

Y podrás revisar las versiones de Python por ejemplo:

---

## 4. Verificar la versión de Python

```bash
~/.venv/bin/python --version
```

**Salida:**

```bash
carlos@SGKX-P2-04V0:/mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient$ ~/.venv/bin/python --version
Python 3.10.12
carlos@SGKX-P2-04V0:/mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient$ []
```

---

## 📦 Paso 3: Instalar solo lo necesario

```bash
uv add dashscope
```

### ℹ️ ¿Por qué solo `dashscope`?

Porque es el SDK oficial de Alibaba para acceder a Qwen.

No necesitas `openai` ni `requests` para esta prueba básica.

(Los mencioné antes como alternativas, pero para una verificación simple, `dashscope` basta).

**Esto instala:**

- El paquete `dashscope`
- Sus dependencias mínimas

### Ejecuto estos comando para estar seguro de la versión

**Salida del comando:**

```bash
carlos@SGKX-P2-04V0:/mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient$ source .venv/bin/activate
(mcp-pruebaclient) carlos@SGKX-P2-04V0:/mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient$ uv pip show dashscope
Name: dashscope
Version: 1.20.11
Location: /mnt/c/Users/Carlos.Cornejo/Documents/Proyectos/mcp-pruebaclient/.venv/lib/python3.10/site-packages
Requires: certifi, cryptography, requests, websocket-client
Required-by:
```

## 5. Crea archivo client.py en Python

```bash
# prueballm.py
from dashscope import Generation

# 🔑 PON TU TOKEN REAL AQUÍ
API_KEY = "Aquí tu Token"

# Llamada mínima a Qwen-Turbo
r = Generation.call(
    model="qwen-turbo",
    messages=[{"role": "user", "content": "test"}],
    max_tokens=5,
    api_key=API_KEY  # ← Esto es obligatorio en versiones recientes
)

# Verificación segura
if r and hasattr(r, 'output'):
    print("✅ OK")
else:
    print("❌ FAIL")
```



### Realizar Prueba

**comando:**

```bash
uv run python prueballm.py
```