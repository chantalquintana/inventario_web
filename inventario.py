from flask import Flask, jsonify, request, send_from_directory
import os
import json

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------
# Página principal
# -------------------------------
@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


# -------------------------------
# Archivo productos.json
# -------------------------------
@app.route("/productos.json")
def productos():
    return send_from_directory(BASE_DIR, "productos.json")


# -------------------------------
# Actualizar stock desde panel web
# -------------------------------
@app.route("/actualizar_stock", methods=["POST"])
def actualizar_stock():
    data = request.json

    archivo = os.path.join(BASE_DIR, "productos.json")

    if not os.path.exists(archivo):
        return {"error": "productos.json no existe"}, 404

    with open(archivo, "r", encoding="utf-8") as f:
        productos = json.load(f)

    codigo = data.get("codigo")
    nuevo_stock = data.get("existencias")

    actualizado = False

    for p in productos:
        if p["codigo"] == codigo:
            p["existencias"] = nuevo_stock
            actualizado = True
            break

    if not actualizado:
        return {"error": "Producto no encontrado"}, 404

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(productos, f, ensure_ascii=False, indent=4)

    return {"ok": True}

# -------------------------------
# Servir carpeta "imagenes" desde la raíz
# -------------------------------
@app.route("/imagenes/<path:filename>")
def imagenes(filename):
    return send_from_directory(os.path.join(BASE_DIR, "imagenes"), filename)

# -------------------------------
# Servir archivos sueltos desde la raíz (como logo_infopar.png)
# -------------------------------
@app.route("/<path:filename>")
def raiz(filename):
    return send_from_directory(BASE_DIR, filename)


# -------------------------------
# Render usa este puerto
# -------------------------------
if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=puerto)