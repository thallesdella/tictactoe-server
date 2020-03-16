class Commands:

    def __init__(self):
        self.commands = {}
        self.server = None
        self.client = None

    def add_command(self, command, strategy, host_only=False):
        self.commands[command] = {}
        self.commands[command]['strategy'] = strategy
        self.commands[command]['host_only'] = host_only

    def bind(self, server, client):
        self.server = server
        self.client = client
        return self

    def verify(self, all_commands=False):
        action = self.client.get_action()
        command_found = False

        for command in self.commands:
            if all_commands:
                if action.command == command and self.commands[command]['host_only']:
                    self.commands[command](self.server, self.client, action.options)

            if action.command == command and not self.commands[command]['host_only']:
                self.commands[command](self.server, self.client, action.options)

        if not command_found:
            self.client.send_action({'action': 'not_found'})
