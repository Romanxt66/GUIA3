from flask import Flask, request, jsonify, Response

app = Flask(__name__)
usuarios_db: list[dict] = []

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario() -> tuple[Response, int]:
  
    datos_entrantes: dict = request.get_json()

  
    if not datos_entrantes or "nombre" not in datos_entrantes:
        return jsonify({"error": "Falta el campo requerido 'nombre'"}), 400 # 400

 
    nuevo_usuario = {
        "id": len(usuarios_db) + 1,
        "nombre": datos_entrantes["nombre"],
        "rol": datos_entrantes.get("rol", "Usuario Estándar")
    }
    usuarios_db.append(nuevo_usuario)

  
    return jsonify({"mensaje": "Usuario creado", "data": nuevo_usuario}), 201

if __name__ == '__main__':
    app.run(debug=True)