import os
from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from game import Game

from flask_cors import CORS

game_instance = None
# games = {}

# def create_game():
#     game_id = str(uuid.uuid4())
#     games[game_id] = Game()
#     return game_id

def create_app(test_config=None):
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
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

    # @app.route('/')
    # def index():
    #     return "Hello, Flask!"

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/scrabble/create-game', methods=['GET'])
    def create_game():
        global game_instance
        game_instance = Game()
        return jsonify({
            'success': True,
            'message': 'Game created successfully'
        }), 200
    # except Exception as e:
    #     # Handle exceptions and respond with an error message
    #     return jsonify({
    #         'success': False,
    #         'message': str(e)
    #     }), 500
    
    @app.route('/scrabble/game-state', methods=['POST'])
    def get_game_state(game):
        global game_instance
        if game_instance is None:
            return jsonify({"message": "No game in progress. Start a new game!"}), 400
        board = game.get_board()
        players = game.get_players()
        dataToSend = {
            "grid": board.data,
            "playerAScore": 0,
            "playerBScore": 0,
            "playerATiles": players[0].get_tiles(),#[1,2,3,4,5,6,7], 
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
    app = create_app()
    app.run(debug=True)


