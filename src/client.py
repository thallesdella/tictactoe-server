import json
import time


class Action:

    def __init__(self, data=None):
        self.command = None
        self.options = None

        if data:
            data = json.dumps(data)
            self.command = data['command']
            self.options = data['options']

    def __str__(self):
        return json.dumps({'command': self.command, 'options': self.options})


class Client:

    def __init__(self, handler=None, addr=None):
        self.handler = handler
        self.addr = addr
        self.last_seen = 0

    def get_action(self):
        buf_data = None

        if not self.is_alive():
            self.offline_client()
            return Action(buf_data)

        try:
            buf_header = self.handler.recv(10)

            if not buf_header:
                return Action()

            buf_len = int(buf_header.decode('utf-8').strip())
            buf_data = self.handler.recv(buf_len).decode('utf-8')

            self.last_seen = time.time()
        except:
            self.last_seen = 0
            self.offline_client()
        finally:
            return Action(buf_data)

    def send_response(self, command, data=None):
        if not self.is_alive():
            self.offline_client()
            return

        if data is None:
            data = {}

        buf = json.dumps({'code': command, 'data': data})

        try:
            self.handler.send(bytes(f'{len(buf):<10}{buf}', 'utf-8'))
            self.last_seen = time.time()
        except:
            self.last_seen = 0
            self.offline_client()
        return

    def is_alive(self):
        pass

    def offline_client(self):
        pass
