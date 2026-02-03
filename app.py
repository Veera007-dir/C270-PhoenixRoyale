from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "PhoenixRoyal"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        result = str(eval(expression))
        return jsonify({"result": result})
    except (SyntaxError, ZeroDivisionError, NameError):
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
