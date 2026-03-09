
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

CORS(app)

@app.route('/api/config', methods=['GET'])
def obtener_config():

    ambiente_actual = os.getenv("FLASK_ENV", "Producción")
    puerto_asignado = os.getenv("PORT", 5000)

    return jsonify({
        "status": "Servidor seguro en línea",
        "entorno": ambiente_actual,
        "puerto": puerto_asignado
    }), 200

if __name__ == '__main__':
 
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)