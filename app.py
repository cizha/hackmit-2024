import os
from flask import Flask, jsonify, request
from game import Game

from flask_cors import CORS


# @app.route('/api/hello', methods=['GET'])
# def hello():
#     return jsonify(message="Hello from Flask!")



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
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
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return send_from_directory(app.instance_path, 'index.html')

    @app.route('/scrabble/create-game', method=['GET'])
    def create_game():
        game = Game()
        return get_game_state(game)

    
    @app.route('/scrabble/game-state', methods=['POST'])
    def get_game_state(game):
        board = game.board
        dataToSend = {
            "grid": board.data,
            "playerAScore": 0,
            "playerBScore": 0,
            "playerATiles": [1,2,3,4,5,6,7], 
            "playerBTiles": [1,2,3,4,5,6,7]  

        }
        return jsonify(dataToSend)
    
    @app.route('/scrabble/update-game', methods=['GET'])
    def update_game(game):
        """
        takes move data from the frontend, checks if the move is allowed, 
            and makes the move if so, modifying the board, player, and bag
        after the player, board, and bag states of the game are modified, returns updated states to frontend
        """
        request_data = request.get_json()
        selected_cell = request_data.get('selectedCell')
        tile = request_data.get('tile')
        player = request_data.get('player')
        mode = request_data.get('mode')

        move = (selected_cell/15,selected_cell%15,tile) #tile index not value
        response = "Success!"
        if game.move_is_valid(move): 
            # move is valid and move has been updated
            game.make_move(move)
        else:
            # don't update move
            response = "Invalid move; please try again."

        return jsonify({"message": response})

    return app

if __name__ == '__main__':
    create_app().app.run(debug=True)