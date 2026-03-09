import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)



class Producto:

    def __init__(self, nombre: str, precio: float, stock: int):
        self._id = None
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def asignar_id(self, id_valor: int):
        self._id = id_valor

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "precio": self._precio,
            "stock": self._stock
        }



class Inventario:

    def __init__(self):
        self._productos: list[Producto] = []

    def crear_producto(self, nombre: str, precio: float, stock: int) -> dict:
        producto = Producto(nombre, precio, stock)
        producto.asignar_id(len(self._productos) + 1)

        self._productos.append(producto)

        return producto.to_dict()

    def listar_productos(self):
        return [p.to_dict() for p in self._productos]



gestor = Inventario()


@app.route("/api/productos", methods=["GET"])
def listar() -> tuple[Response, int]:

    datos = gestor.listar_productos()

    return jsonify({
        "total": len(datos),
        "productos": datos
    }), 200


@app.route("/api/productos", methods=["POST"])
def crear() -> tuple[Response, int]:

    try:

        payload = request.get_json()

        nuevo = gestor.crear_producto(
            payload["nombre"],
            payload["precio"],
            payload["stock"]
        )

        return jsonify({
            "mensaje": "Producto creado",
            "data": nuevo
        }), 201

    except KeyError:

        return jsonify({
            "error": "JSON inválido"
        }), 400


if __name__ == "__main__":

    app.run(
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG") == "1"
    )