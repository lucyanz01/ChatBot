from flask import Flask, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/home", methods=["GET"])
def home():
    return "Servidor Flask funcionando"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", " ")
    respuesta = bot.responder(mensaje)
    return jsonify ({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
