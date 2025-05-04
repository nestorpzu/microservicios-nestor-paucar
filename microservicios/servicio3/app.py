from flask import Flask, jsonify
import json

app3 = Flask(__name__)

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    try:
        with open('demo.json', encoding='utf-8') as f:
            datos = json.load(f)

        if str(municipioid) in datos:
            return jsonify(datos[str(municipioid)]), 200
        else:
            return jsonify({"error": "Municipio no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error al obtener datos", "detalle": str(e)}), 500

if __name__ == '__main__':
    app3.run(host='0.0.0.0', port=5002)