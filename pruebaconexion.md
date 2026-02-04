# Manual: Prueba de Conexión a Qwen-Turbo vía API Compatible

**Documento técnico para verificar la autenticación y comunicación con DashScope**

---

## 1. Objetivo

Este documento describe el procedimiento para validar que un token de DashScope permite acceder al modelo **Qwen-Turbo** mediante la **API compatible con OpenAI**, replicando la configuración utilizada en n8n.

---

## 2. Requisitos

- Token válido de DashScope (formato: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)
- Acceso a internet
- Python ≥ 3.8 con el paquete `requests` instalado

---

## 3. Script de prueba (`test_n8n.py`)

```python
# test_n8n.py
import requests

# 🔑 Token completo (¡incluye el prefijo "sk-"!)
TOKEN = "Aquí tu Token de qwen"

# ✅ URL exacta del modo compatible (igual que en n8n)
URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "model": "qwen-turbo",
    "messages": [{"role": "user", "content": "Hola"}],
    "max_tokens": 10
}

resp = requests.post(URL, headers=headers, json=data)
print("Status:", resp.status_code)
print("Respuesta:", resp.text)
```

### Notas críticas:

- El token **debe incluir el prefijo** `sk-`.
- La URL **debe ser exactamente** `https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions` (sin espacios al final).

---

## 4. Ejecución

### 4.1. Instalar dependencias

```bash
pip install requests
# O si usas uv:
uv add requests
```

### 4.2. Ejecutar el script

```bash
python test_n8n.py
```

---

## 5. Resultados esperados

### ✅ Éxito (token y URL correctos)

```
Status: 200
Respuesta: {"choices": [...], "usage": {...}, "model": "qwen-turbo"}
```

### ❌ Errores comunes

| Resultado | Causa | Solución |
|-----------|-------|----------|
| `Status: 401`<br>`{"code":"InvalidApiKey",...}` | Token sin `sk-` o inválido | Verificar token en [DashScope Console](https://dashscope.console.aliyun.com/) |
| `Status: 400`<br>`{"code":"InvalidParameter","message":"url error"}` | URL incorrecta o con espacios | Usar la URL exacta sin espacios finales |
| `Status: 200` pero respuesta vacía | `max_tokens` muy bajo | Aumentar `max_tokens` a 20+ |

---

## 6. Validación en n8n

Este script replica **exactamente** la llamada que realiza n8n:

- **Misma URL** (`/compatible-mode/v1/chat/completions`)
- **Mismo header** (`Authorization: Bearer sk-...`)
- **Mismo cuerpo de solicitud** (JSON con `model`, `messages`, etc.)

Si funciona en n8n, **este script debe funcionar** con los mismos parámetros.

---

## 7. Conclusión

Esta prueba confirma que:

1. El token tiene permisos para el **modo compatible** de DashScope
2. La comunicación con Qwen-Turbo es funcional
3. La configuración es reusable para integraciones con MCP u otros sistemas

---

## Recursos adicionales

- [Documentación de DashScope](https://help.aliyun.com/zh/dashscope/)
- [API Compatible con OpenAI](https://help.aliyun.com/zh/dashscope/developer-reference/compatibility-of-openai-with-dashscope/)

---

**Nota de seguridad:** Nunca compartas tu token real en repositorios públicos. Usa variables de entorno o archivos `.env` para almacenar credenciales.