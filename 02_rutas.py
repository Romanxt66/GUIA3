from flask import Flask

app = Flask(__name__)

# Ruta DINÁMICA: Extraemos un texto (String) de la URL
@app.route('/api/saludar/<string:nombre>', methods=['GET'])
def saludar(nombre: str) -> str:
    return f"Hola {nombre}, tu solicitud fue enrutada exitosamente."

# Ruta DINÁMICA: Extraemos un entero (Integer) de la URL
@app.route('/api/calcular_iva/<int:precio>', methods=['GET'])
def calcular(precio: int) -> str:
    iva: float = precio * 0.19
    total: float = precio + iva
    return f"Precio: ${precio} | IVA: ${iva} | Total: ${total}"

if __name__ == '__main__':
    app.run(debug=True)

