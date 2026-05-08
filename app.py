from flask import Flask, jsonify, request
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Pedro Lacerda"},
    {"id": 2, "nome": "Ana Lucia"},
    {"id": 3, "nome": "Biatris"},
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def criar_usuarios():
    novo = request.json
    novo['id'] = len(usuarios) + 1
    usuarios.append(novo)
    return jsonify(novo), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    app.run(debug=true)
