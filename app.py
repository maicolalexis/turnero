from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Cola de turnos
turnos = deque(maxlen=10)  # solo guarda los últimos 10 turnos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar')
def enviar():
    return render_template('enviar_turno.html')

@app.route('/api/agregar', methods=['POST'])
def agregar_turno():
    data = request.json
    turno = data.get('turno')
    if turno:
        turnos.appendleft(turno)
        return jsonify({"mensaje": "Turno agregado", "turno": turno}), 200
    return jsonify({"error": "Turno vacío"}), 400

@app.route('/api/turnos', methods=['GET'])
def obtener_turnos():
    return jsonify(list(turnos))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
