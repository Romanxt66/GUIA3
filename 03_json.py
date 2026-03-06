from flask import Flask, jsonify, Response

app = Flask(__name__)

# Base de datos simulada en memoria (Lista de Diccionarios)
sensores_trapiche: list[dict] = [
    {"id": "S1", "tipo": "Temperatura", "valor": 95.5, "estado": "Activo"},
    {"id": "S2", "tipo": "Presion", "valor": 40.2, "estado": "Alerta"}
]

@app.route('/api/sensores', methods=['GET'])
def obtener_sensores() -> Response:
    """Retorna todo el inventario serializado."""
    return jsonify({
        "total_registros": len(sensores_trapiche),
        "data": sensores_trapiche
    })

@app.route('/api/sensores/<string:id_sensor>', methods=['GET'])
def buscar_sensor(id_sensor: str) -> tuple[Response, int]:
    """Búsqueda específica. Retorna el objeto y un Código de Estado HTTP."""
    for sensor in sensores_trapiche:
        if sensor["id"] == id_sensor:
            return jsonify(sensor), 200 # 200 OK

    # Arquitectura resiliente: 404 (Not Found)
    return jsonify({"error": "Sensor no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)