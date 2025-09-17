import random

class ChatBot:
    def __init__(self):

     # Listas para las interacciones y funciones

        self.saludos = ["Hola", "saludo", "ola", "buenas", "holaaa"]
        self.despedidas = ["chau", "adios", "nos vemos", "gracias", "bye"]
        self.formas_desp = ["¡Nos vemos!", "Gracias por usar ChatBot", "¡Adiós!", "Háblame cuando necesites algo."]
        self.comenzar_juego = ["juguemos", "jugar", "juego"]
        self.opciones = ["piedra", "papel", "tijera"]
        self.jugando = False
        self.no_jugar = ["no", "no jugar", "detener", "salir del juego", "cancelar"]
        self.eleccion_bot = None
        self.eleccion_user = None
        self.beats = {
             "piedra" : "tijera",
             "papel" : "piedra",
             "tijera" : "papel"
        }
        self.historial = []

    # Funciones de interaccióm

    def saludar(self, mensaje):
            mensaje = mensaje.lower()
            if any (saludo in mensaje for saludo in self.saludos):
                 return ("Hola!, ¿qué necesitas hoy?")
            return None
    
    def despedir(self, mensaje):
            mensaje = mensaje.lower()
            if any(despedida in mensaje for despedida in self.despedidas):
                 return random.choice(self.formas_desp)
            return None
            
    def jugar(self, mensaje):
            mensaje = mensaje.lower()
            if any(jugar in mensaje for jugar in self.comenzar_juego):
                  self.jugando = True
                  return ("De acuerdo, juguemos a Piedra, papel o tijera. Escoge tu opción.")
                
    # Juego 

    def res_juego(self, mensaje):
         mensaje = mensaje.lower().strip().rstrip("s")

         eleccion = next((op for op in self.opciones if op in mensaje), None)
         if not eleccion:
               return ("No entendí tu elección. Escribe piedra, papel o tijera.")

         self.eleccion_user = eleccion
         self.eleccion_bot = random.choice(self.opciones).lower().rstrip("s")

         resultado = self.comprob()
         resultado_final = (f"Seleccionaste {self.eleccion_user.capitalize()}. Yo selecciono {self.eleccion_bot.capitalize()}. {resultado}")
         self.jugando = False
         return resultado_final
    
    # Si el usuario desea cancelar o no jugar

    def cancelar(self, mensaje):
          mensaje = mensaje.lower()
          if any(op in mensaje for op in self.no_jugar):
                self.jugando = False
                return ("De acuerdo, juego detenido.")
    
    # Comprobación de resultado

    def comprob(self):
         if self.eleccion_bot == self.eleccion_user:
              return "Es un empate."
         elif self.beats[self.eleccion_user] == self.eleccion_bot:
              return "¡Ganaste!"
         else:
              return "¡Perdiste!"
         
    # Manejo de respuestas y mensajes
                
    def responder(self, mensaje):
     mensaje = mensaje.lower()

     respuesta = None

     if self.jugando:
          cancelar = self.cancelar(mensaje)
          if cancelar:
               respuesta = cancelar
          else:
               respuesta = self.res_juego(mensaje)
     else:
          respuesta = self.saludar(mensaje)
          if not respuesta:
               respuesta = self.jugar(mensaje)
          if not respuesta:
               respuesta = self.despedir(mensaje)
          if not respuesta:
               respuesta = "No entendí, ¿podrías repetir?"

     self.historial.append({"mensaje": mensaje, "respuesta": respuesta})

     return respuesta
    
# Función principal y ejecución
        
def main():
        bot = ChatBot()
        print("ChatBot para chatear. Escribe 'salir' para terminar.")
        while True:
            entrada = input("Tu: ")
            if entrada.lower() == "salir":
                break
            respuesta = bot.responder(entrada)
            print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
       main()