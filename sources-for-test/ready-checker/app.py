from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

# Получаем имя пода из переменной окружения или хоста
pod_name = os.environ.get('HOSTNAME', 'unknown-pod')
start_time = time.time()

@app.route('/')
def home():
    return f"Hello from {pod_name}!"

@app.route('/healthz')
def health_check():
    """Базовая проверка здоровья"""
    return jsonify({
        "status": "healthy",
        "pod": pod_name,
        "uptime": time.time() - start_time
    })

@app.route('/ready')
def ready_check():
    """Readiness probe - через 10 секунд становится готов"""
    uptime = time.time() - start_time
    
    if uptime >= 10:  # Готов через 10 секунд
        return jsonify({
            "status": "ready",
            "pod": pod_name,
            "uptime": uptime
        }), 200
    else:
        return jsonify({
            "status": "not ready",
            "pod": pod_name,
            "uptime": uptime
        }), 503

@app.route('/slow-ready')
def slow_ready():
    """Медленная готовность - через 30 секунд"""
    uptime = time.time() - start_time
    
    if uptime >= 30:
        return jsonify({
            "status": "ready",
            "pod": pod_name,
            "uptime": uptime,
            "message": "Fully warmed up!"
        }), 200
    else:
        return jsonify({
            "status": "warming up",
            "pod": pod_name,
            "uptime": uptime,
            "seconds_left": 30 - uptime
        }), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
