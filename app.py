from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import time
import math
import json
import os

app = Flask(__name__)
CORS(app)

HISTORIAL_FILE = 'historial.json'

# Inicializa el archivo de almacenamiento si no existe
if not os.path.exists(HISTORIAL_FILE):
    with open(HISTORIAL_FILE, 'w') as f:
        json.dump([], f)

def procesar_señal_csi():
    tiempo_actual = time.time()
    
    # 1. Simulación de Conteo de Personas (Varía suavemente entre 1 y 3 personas)
    usuarios = 1 + int((math.sin(tiempo_actual / 30) + 1) * 1)
    
    # 2. Simulación de Detección de Caídas (3% de probabilidad para pruebas dinámicas)
    if random.random() < 0.03:
        alerta = "¡Caída Detectada!"
        ritmo_cardiaco = random.uniform(115, 135)  # Simula taquicardia por el impacto/susto
        ritmo_respiratorio = random.uniform(24, 28)
        estado = "Ansioso"
    else:
        alerta = "Estable"
        # El ritmo base sube un poco si hay más gente en la sala (actividad)
        base_bpm = 70 + (usuarios * 3)
        ritmo_cardiaco = base_bpm + (math.sin(tiempo_actual) * 10) + random.uniform(-2, 2)
        ritmo_respiratorio = 15 + (math.cos(tiempo_actual / 2) * 4) + random.uniform(-1, 1)
        
        if ritmo_cardiaco > 90 or ritmo_respiratorio > 20:
            estado = "Ansioso"
        else:
            estado = "Relajado"
        
    return {
        "bpm": round(ritmo_cardiaco, 1),
        "rpm": round(ritmo_respiratorio, 1),
        "estado": estado,
        "usuarios": usuarios,
        "alerta": alerta,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route('/api/vitas', methods=['GET'])
def obtener_signos_vitales():
    return jsonify(procesar_señal_csi())

@app.route('/api/historial', methods=['GET'])
def obtener_historial():
    with open(HISTORIAL_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/historial', methods=['POST'])
def guardar_en_historial():
    registro = request.json
    with open(HISTORIAL_FILE, 'r+') as f:
        data = json.load(f)
        data.append(registro)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # El puerto 5000 es el que escucha tu index.html
    app.run(debug=True, port=5000)
