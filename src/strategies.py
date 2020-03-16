from src.exceptions import ServerException
from src.game import Game


def create_room(server, client, options):
    new_game = Game()

    if options and 'room_id' in options:
        new_game = Game(options['room_id'])

    new_game.add_player(client)
    new_game_id = new_game.get_id()

    server.rooms[new_game_id] = new_game
    client.send_action(200, {'id': new_game_id})
    return


def join_room(server, client, options):
    if not options or 'room_id' not in options:
        client.send_action('error', {'message': 'Parameters required'})

    room_id = options['room_id']
    if room_id not in server.rooms:
        create_room(server, client, options)

    try:
        room = server.get_room(room_id)
        room.add_player(client)
    except ServerException as e:
        client.send_response(e.code, {'message': f'{e.message}'})
    return
