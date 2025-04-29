from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a = data['a']
    b = data['b']
    operation = data['operation']

    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        try:
            result = divide(a, b)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)