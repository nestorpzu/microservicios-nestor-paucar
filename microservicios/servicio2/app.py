from flask import Flask, jsonify
import json

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    try:
        with open('meteo.json') as f:
            datos = json.load(f)

        if str(municipioid) in datos:
            return jsonify(datos[str(municipioid)]), 200
        else:
            return jsonify({"error": "Municipio no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener datos", "detalle": str(e)}), 500

if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5001)
