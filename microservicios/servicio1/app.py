from flask import Flask, jsonify
import json

app1 = Flask(__name__)

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    try:
        with open('municipio.json', encoding='utf-8') as f:
            data = json.load(f)
        
        str_id = str(municipioid)
        if str_id in data:
            return jsonify(data[str_id]), 200
        else:
            return jsonify({"error": "Municipio no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": "Error interno", "detalle": str(e)}), 500

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)
