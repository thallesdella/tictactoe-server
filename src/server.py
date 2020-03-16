import socket

from src.exceptions import RoomNotFound
from src.client import Client
from src.commands import Commands
from src.strategies import create_room, join_room


class Server:

    def __init__(self, port=7331):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), port))

        self.commands = Commands()
        self.commands.add_command('create_room', create_room)
        self.commands.add_command('join_room', join_room)

        self.rooms = {}

    def run(self):
        self.socket.listen(10)

        while True:
            handler, addr = self.socket.accept()
            self.commands.bind(self, Client(handler, addr))
            self.commands.verify()

    def get_room(self, room_id):
        if room_id not in self.rooms:
            raise RoomNotFound()

        return self.rooms[room_id]
