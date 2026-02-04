# README

## Guía Paso a Paso: Configuración de MCP en WSL desde cero

**Entorno validado**\
- Windows 11\
- WSL2\
- Ubuntu 22.04\
- Python 3.10\
- MCP v1.26.0

**Última prueba:** 29 de enero de 2026

------------------------------------------------------------------------

## 1. ¿Qué es MCP? (Visión conceptual)

**MCP (Model Context Protocol)** es un protocolo estándar que permite a
los modelos de lenguaje grandes (LLMs) interactuar de forma segura y
estructurada con herramientas externas, como APIs, bases de datos o
sistemas de archivos.

-   Define contratos claros para:
    -   **Tools**
    -   **Resources**
    -   **Prompts**
-   Usa **HTTP/JSON**
-   Soporta autenticación, descubrimiento automático y validación de
    esquemas
-   Se ejecuta como un **servidor ASGI** (uvicorn)
-   Es mantenido por **Anthropic**

En términos simples: MCP es un "traductor universal" que le da *manos* a
la IA.\
Permite que no solo responda, sino que **actúe** (sumar, buscar, leer
archivos, consultar datos).\
Es usado por clientes como **Claude** y **Cursor**.

------------------------------------------------------------------------

## 2. Arquitectura técnica (resumen)

-   Cliente LLM (Claude, Cursor, etc.)
-   Servidor MCP (Python)
-   uvicorn como motor ASGI
-   Comunicación vía HTTP/JSON sobre `localhost`

------------------------------------------------------------------------

## 3. Instalar y configurar WSL

### 3.1 Instalar WSL (PowerShell como Administrador)

``` powershell
wsl --install
wsl --list --online
wsl --install -d Ubuntu-22.04
```

------------------------------------------------------------------------

### 3.2 Configurar recursos de WSL (Windows)

**⚠️ Importante:**\
El archivo **`.wslconfig` se crea en Windows**, directamente en:

    C:\Users\<tu_usuario>\.wslconfig

Contenido del archivo:

``` ini
[wsl2]
memory=2GB
processors=2
swap=1GB
localhostForwarding=true
```

Reiniciar WSL después:

``` powershell
wsl --shutdown
```

------------------------------------------------------------------------

## 4. Primera vez en Ubuntu (WSL)

``` bash
sudo apt update && sudo apt upgrade -y
python3 --version    # Debe ser ≥ 3.10
pip --version        # Si no existe: sudo apt install python3-pip
```

------------------------------------------------------------------------

## 5. Preparar el entorno de trabajo

**Desde la terminal de Ubuntu (WSL), navega al sistema de archivos de
Windows y crea tu carpeta de proyecto:**

``` bash
cd /mnt/c/Users/Carlos.Cornejo/Documents/Proyectos
mkdir -p mcp
cd mcp
```

Esto permite que el proyecto resida en Windows, pero se ejecute
completamente dentro de WSL.

------------------------------------------------------------------------

## 6. Configurar VS Code con WSL

Desde la carpeta del proyecto:

``` bash
code .
```

En VS Code: - Abrir una nueva terminal - Verificar que sea **Ubuntu /
WSL**, no PowerShell ni CMD

------------------------------------------------------------------------

## 7. Instalar el SDK de MCP

``` bash
pip install "mcp[cli]"
```

Verificación:

``` bash
pip show mcp
```

Salida esperada:

    Name: mcp
    Version: 1.26.0
    Author: Anthropic, PBC

------------------------------------------------------------------------

## 8. Requisito adicional: Node.js (solo para modo desarrollo)

⚠️ **Solo necesario para `mcp dev`**, ya que utiliza el MCP Inspector
vía `npx`.

``` bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

------------------------------------------------------------------------

## 9. Instalar uv (opcional, recomendado)

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv --version
```

------------------------------------------------------------------------

## 10. Crear tu servidor MCP

``` python
from mcp.server.fastmcp import FastMCP

app = FastMCP("mi-servidor")

@app.tool()
def sumar(a: int, b: int) -> int:
    return a + b

@app.resource("saludo://{nombre}")
def obtener_saludo(nombre: str) -> str:
    return f"¡Hola {nombre}! 👋"

if __name__ == "__main__":
    app.run()
```

------------------------------------------------------------------------

## 11. Ejecutar el servidor


``` bash
mcp dev server.py
```

Manual

``` bash
npx @modelcontextprotocol/inspector mcp run server.py
```

------------------------------------------------------------------------

## 12. Estado

✅ Flujo completo probado y funcional en entorno **WSL2**\
📅 Validado el **29 de enero de 2026**
