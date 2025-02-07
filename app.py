from flask import Flask, request, jsonify
import time

app = Flask(__name__)

start_time = time.time()  # Track uptime

# Default route to avoid 404 errors
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Nimra's Flask Calculator API!"})

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a + b})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/subtract')
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a - b})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/multiply')
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a * b})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/divide')
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        return jsonify({"result": a / b})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/healthz')
def health():
    uptime = time.time() - start_time
    return jsonify({"status": "OK", "uptime": uptime})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
