import random
from collections import Counter
from constants import MOVES, WINNING_COMBINATIONS
from player import Player

# Una clase con las acciones de la maquina, su puntaje y el registro de los movimientos del jugador
# No he dividio las acciones de la maquina en una clase aparte porque no la clase game se quedaria vacia con unos pocos prints

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name) # El player2 es la "maquina"
        self.player_moves = []
        self.round_counter = 0
        self.machine_losses = 0

    def get_winner(self, move1, move2):
    # Determina el ganador de la ronda
        if move1 == move2:
            return None, "Empate"  # Si los movimientos son iguales, es un empate
        elif move2 in WINNING_COMBINATIONS[move1]:
            return self.player1, WINNING_COMBINATIONS[move1][move2]  # Jugador 1 gana
        else:
            return self.player2, WINNING_COMBINATIONS[move2][move1]  # Jugador 2 (máquina) gana

    def play_round(self, move1, move2):
        # Juega una ronda y actualiza el puntaje
        winner, action = self.get_winner(move1, move2)
        if winner:
            winner.increment_score()
            if winner == self.player1:
                self.machine_losses += 1
        return winner, action

    def get_random_move(self):
        # Elige un movimiento de forma aleatoria
        return random.choice(MOVES)

    def get_predicted_move(self):
        self.round_counter += 1

        # Cada 2-5 movimientos, se elige un movimiento de manera aleatoria
        if self.round_counter % random.randint(2, 5) == 0:
            return self.get_random_move()

        # Cuantas mas derrotas haya mas posibilidades hay de que el if se cumpla y tambien se eliga un movimiento de forma aleatoria
        if random.random() < (self.machine_losses / (self.round_counter + 1)):
            return self.get_random_move()

        if not self.player_moves:
            return self.get_random_move()

        # Contar la frecuencia de cada movimiento del jugador y elegir el movimiento que mas veces ha hecho el jugador
        move_counts = Counter(self.player_moves)
        most_common_move = move_counts.most_common(1)[0][0]
        
        # Obtener los movimientos que ganan contra el movimiento más común del jugador
        winning_moves = [move for move in WINNING_COMBINATIONS if most_common_move in WINNING_COMBINATIONS[move]]
        return random.choice(winning_moves)

    def record_player_move(self, move):
        self.player_moves.append(move)