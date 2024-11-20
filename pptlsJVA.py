from game import Game
from constants import MOVES

# El archivo principal en el que se ejecuta el juego entre el jugador 1 y la máquina

def main():
    nombre_jugador1 = input("Nombre del Jugador 1: ")
    nombre_jugador2 = "Máquina"
    juego = Game(nombre_jugador1, nombre_jugador2)

    rondas = int(input("¿Cuántas rondas quieres jugar? "))

    for _ in range(rondas):
        movimiento1 = input(f"{juego.player1.name}, elige tu movimiento ({', '.join(MOVES)}): ").lower()
        if movimiento1 not in MOVES:
            print("Movimiento no válido. Inténtalo de nuevo.")
            continue
        
         # La máquina predice su movimiento
        movimiento2 = juego.get_predicted_move()
        
        # Se registra el movimiento del jugador
        juego.record_player_move(movimiento1)
        print(f"La máquina elige: {movimiento2}")
        
        # Juega una ronda y muestra el ganador mostrando el resultado de la ronda
        ganador, accion = juego.play_round(movimiento1, movimiento2)
        if ganador:
            print(f"¡{accion}! ¡{ganador.name} gana esta ronda!")
        else:
            print("¡Es un empate!")

    print(f"Puntuación final: {juego.player1.name} {juego.player1.score} - {juego.player2.name} {juego.player2.score}")

if __name__ == "__main__":
    main()