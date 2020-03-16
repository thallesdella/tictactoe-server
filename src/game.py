import json

from src.exceptions import FullGameException, PlayerNotFound


def generate_uniq_id():
    return 0


class Board:

    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def __str__(self):
        return json.dumps(self.board)


class Game:

    def __init__(self, game_id=None):
        if not game_id:
            game_id = generate_uniq_id()

        self.id = game_id
        self.board = Board()
        self.players = {}
        self.current_player = 0

    def add_player(self, client):
        if len(self.players) == 2:
            raise FullGameException()

        player = Player(client)
        player_id = player.get_id()

        self.players[player_id] = player

        if self.current_player == 0:
            self.current_player = player_id

        return player_id

    def get_player(self, player_id):
        if player_id not in self.players:
            raise PlayerNotFound()

        return self.players[player_id]

    def get_id(self):
        return self.id


class Player:

    def __init__(self, handler):
        self.id = generate_uniq_id()
        self.handler = handler

    def get_id(self):
        return self.id
