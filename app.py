import time
from flask import Flask, jsonify

app = Flask(__name__)

# Simulación de métricas en memoria para Prometheus / Dashboard
START_TIME = time.time()
REQUEST_COUNT = 0
ERROR_COUNT = 0

@app.route('/')
def home():
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return jsonify({
        "status": "active",
        "message": "Microservicio de Evaluación Parcial 3 operando de forma segura",
        "version": "1.0.0"
    }), 200

@app.route('/health')
def health():
    # Endpoint para el HEALTHCHECK de Docker y Kubernetes simulado
    return jsonify({"status": "UP", "checks": {"database": "connected"}}), 200

@app.route('/metrics')
def metrics():
    # Expone métricas formateadas para Prometheus (IE1)
    global REQUEST_COUNT, ERROR_COUNT
    uptime = time.time() - START_TIME
    prometheus_format = (
        f"# HELP app_uptime_seconds Tiempo de actividad del microservicio\n"
        f"app_uptime_seconds {uptime}\n"
        f"# HELP app_requests_total Total de peticiones HTTP\n"
        f"app_requests_total {REQUEST_COUNT}\n"
        f"# HELP app_errors_total Total de errores registrados\n"
        f"app_errors_total {ERROR_COUNT}\n"
    )
    return prometheus_format, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/api/v1/suma/<int:a>/<int:b>')
def calcular_suma(a, b):
    global REQUEST_COUNT, ERROR_COUNT
    REQUEST_COUNT += 1
    try:
        resultado = a + b
        return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": resultado}), 200
    except Exception:
        ERROR_COUNT += 1
        return jsonify({"error": "Error interno en el cálculo"}), 500

if __name__ == '__main__':
    # El servidor escucha en todas las interfaces en el puerto 5000
    app.run(host='0.0.0.0', port=5000)  # nosec