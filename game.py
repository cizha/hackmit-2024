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
        for player in self.players:
            self.fill_tiles(player)
        self.next_player = 1
        self.curr_player = self.players[0]

    def get_board():
        return self.board

    def fill_tiles(player):
        while len(player.tiles)<PLAYER_MAX_TILES:
            if self.bag.is_empty:
                break
            tile = self.bag.remove_tile()
            player.add_tile(tile)


    # move = tuple of triples - row, col, tile value 
    def make_move(move):
        # place tiles on board and remove tiles from player's tiles
        for tile in move:
            self.board.place_tile(tile)
            value = tile[2]
            self.curr_player.remove_tile(value)
        # take tiles from the bag to replace if one exists
        self.fill_tiles(player)

        # update current and next players to be set up for next move
        self.curr_player = self.players[next_player]
        self.next_player+=1
        self.next_player%=len(self.players)


class Player:
    """
    tiles: array of tile values
    """

    def __init__(self):
        self.tiles = []

    def add_tile(self, val):
        self.tiles.append(val)
    
    def remove_tile(self, val):
        # remove the tile which has value = val
        self.tiles.remove(val)


class Bag:
    """
    tiles: tiles in the bag; initialized in a random order based on the set distribution
    """
    DIST_DEFAULT = {0: 10, 1:10, 2:10, 3:10, 4:10, 5:10, 6:10, 7:10, 8:10, 9:10}

    def __init__(self, distribution=DIST_DEFAULT):
        self.tiles = []
        for (key, val) in distribution:
            self.tiles.extend([key]*val)
        self.tiles.shuffle()
    
    def remove_tile():
        try:
            return self.pop(0)
        except KeyError:
            return None

    def is_empty():
        return len(self.tiles) == 0


def update_board(move):
    """
    takes move data from the frontend, checks if the move is allowed, and makes the move if so
    after the player, board, and bag states of the game are modified, returns updated states to frontend
    """
    # backend stores the board
    if is_valid(move):
        make_move(move)
    else:
        # don't update move
        display_error()
