import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


class Game:
    """
    board: 2d array (aengus), stored in backend and displayed by frontend
    list of players: (can start with 2, extend to 4 if time)
    bag: list of remaining tiles - game ends when no tiles remain and players have no more moves
    """
    PLAYER_MAX_TILES = 7
    def __init__(self):
        self.board = new Board()
        self.players = [new Player(), new Player()]
        self.bag = new Bag()
        self.curr_player = 0

    def get_board():
        return self.board

    # move = tuple of triples - row, col, tile value 
    def make_move(move):
        # place tiles on board and remove tiles from player's tiles
        for tile in move:
            self.board.place_tile(tile)
            value = tile[2]
            self.players[self.curr_player].remove(value)
        # take a tiles from the bag to replace if one exists
        # TODO

class Player:
    """
    tiles: array of tile values
    """

    def __init__(self):
        self.tiles = []

    def fill_tiles(self):
        while len(self.tiles)<Game.MAX_TILES:
            pass
            # TODO: fill the tiles array



def update_board(move):
    # backend stores the board
    if is_valid(move):
        make_move(move)
    else:
        # don't update move
        display_error()
