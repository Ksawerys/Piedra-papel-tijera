# Se guardan las opciones de juego y las combinaciones ganadoras con la accion que se realiza en cada caso

MOVES = ["piedra", "papel", "tijeras", "lagarto", "spock"]
WINNING_COMBINATIONS = {
    "piedra": {"tijeras": "Piedra aplasta Tijeras", "lagarto": "Piedra aplasta Lagarto"},
    "papel": {"piedra": "Papel cubre Piedra", "spock": "Papel refuta Spock"},
    "tijeras": {"papel": "Tijeras cortan Papel", "lagarto": "Tijeras decapitan Lagarto"},
    "lagarto": {"spock": "Lagarto envenena Spock", "papel": "Lagarto come Papel"},
    "spock": {"tijeras": "Spock rompe Tijeras", "piedra": "Spock vaporiza Piedra"}
}