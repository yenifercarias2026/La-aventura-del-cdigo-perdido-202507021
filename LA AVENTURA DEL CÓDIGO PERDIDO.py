# LA AVENTURA DEL CÓDIGO PERDIDO
# Variables del jugador
puntos = 0
objetos = 0
vidas = 3
# Inventario
 def inventario():
 print("\n--- INVENTARIO ---")
 print("Puntos:", puntos)
 print("Objetos:", objetos)
 print("Vidas:", vidas)
# Tutorial
def tutorial():
 print("\n--- TUTORIAL ---")
 print("Resuelve retos de lógica.")
 print("Supera obstáculos.")
 print("Recupera el código perdido.")
 print("¡Buena suerte!")
def nivel1():
 global puntos, objetos
 print("\n=== NIVEL 1 ===")
 print("Misión: encontrar la primera pieza del código.")
 opcion = input("¿Completaste el reto? (si/no): ")
 if opcion.lower() == "si":
 puntos += 10
 objetos += 1
 print("¡Nivel completado!")
      else:
 print("Debes intentarlo nuevamente.")
def nivel2():
 global puntos, objetos
 print("\n=== NIVEL 2 ===")
 print("Misión: resolver el acertijo secreto.")
 opcion = input("¿Resolviste el acertijo? (si/no): ")
 if opcion.lower() == "si":
 puntos += 20
 objetos += 1
 print("¡Nivel completado!")
 else:
 print("No superaste el reto.")
def nivel_final():
 print("\n=== NIVEL FINAL ===")
 if objetos >= 2:
 print("Has recuperado todas las piezas del código.")
 print(" ¡GANASTE EL JUEGO! ")
 else:
 print("Te faltan piezas del código.")
while True:
 print("\n=== LA AVENTURA DEL CÓDIGO PERDIDO ===")
 print("1. Tutorial")
 print("2. Jugar")
 print("3. Inventario")
 print("4. Salir")
 opcion = input("Selecciona una opción: ")
 if opcion == "1":
 tutorial()
 elif opcion == "2":
 nivel1()
 nivel2()
 nivel_final()
 elif opcion == "3":
 inventario()
 elif opcion == "4":
 print("¡Gracias por jugar!")
 break
 else:
 print("Opción no válida.")
"""
Clase padre: JuegoBase. Tiene los atributos puntos, objetos y vidas, y los métodos 
tutorial(), inventario() y mostrarMenu()
clases hijas: Nivel1_PrimeraPieza, Nivel2_AcertijoSecreto y NivelFinal_CodigoPerdido,
que comparten las características del juego y añaden sus propios retos y misiones para 
recuperar el código perdido.
""