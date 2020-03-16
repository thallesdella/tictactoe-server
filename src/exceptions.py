class ServerException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message


class FullGameException(ServerException):

    def __init__(self):
        super(FullGameException, self).__init__(501, 'The game you are trying to join is full')


class PlayerNotFound(ServerException):

    def __init__(self):
        super(PlayerNotFound, self).__init__(404, 'The player you are trying to obtain was not found')


class RoomNotFound(ServerException):

    def __init__(self):
        super(RoomNotFound, self).__init__(404, 'The room you are trying to obtain was not found')
