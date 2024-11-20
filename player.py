# Una clase con las acciones del jugador y su puntaje

class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def increment_score(self):
        self._score += 1