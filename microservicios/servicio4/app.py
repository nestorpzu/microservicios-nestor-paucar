from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    
    base_urls = {
    "geo": f"http://servicio1:5000/{municipioid}/geo",
    "meteo": f"http://servicio2:5001/{municipioid}/meteo",
    "demo": f"http://servicio3:5002/{municipioid}/demo"
    }

    datos = {}

    for param in [parametro1, parametro2]:
        if param not in base_urls:
            return jsonify({"error": f"Parámetro desconocido: {param}"}), 400

        try:
            res = requests.get(base_urls[param])
            if res.status_code == 200:
                datos[param] = res.json()
            else:
                datos[param] = {"error": f"Servicio {param} devolvió {res.status_code}"}
        except Exception as e:
            datos[param] = {"error": f"No se pudo conectar al servicio {param}", "detalle": str(e)}

    return jsonify(datos), 200

if __name__ == '__main__':
    app4.run(host='0.0.0.0', port=5003)


