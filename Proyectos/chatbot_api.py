from flask import Flask, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/home", methods=["GET"])
def home():
    return "Inicio ChatBot"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", " ")
    respuesta = bot.responder(mensaje)
    return jsonify ({"respuesta": respuesta})

@app.route("/historial", methods=["GET"])
def historial():
    return jsonify(bot.historial)

if __name__ == "__main__":
    app.run(debug=True)
