# server.py
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