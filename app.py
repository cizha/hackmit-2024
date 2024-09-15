import os
from flask import Flask, jsonify, request

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
    
    @app.route('/scrabble/game-state', methods=['POST'])
    def gamestate():
        dataToSend = {}
        return jsonify(dataToSend)
    
    @app.route('/scrabble/update-game', methods=['GET'])
    def updategame():
        response = ''
        return jsonify(response)

    return app


def new_game():
    return new Game()


def update_game(game, move):
    """
    takes move data from the frontend, checks if the move is allowed, 
        and makes the move if so, modifying the board, player, and bag
    after the player, board, and bag states of the game are modified, returns updated states to frontend
    """
    if game.move_is_valid(move): 
        # move is valid and move has been updated
        make_move(move)
        return True, "Success!"
    else:
        # don't update move
        return False, "Invalid move; please try again."
