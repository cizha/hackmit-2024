from scrabblegamestate import boardstate
import random

class Game:
    """
    board: 2d array (aengus), stored in backend and displayed by frontend
    list of players: (can start with 2, extend to 4 if time)
    bag: list of remaining tiles - game ends when no tiles remain and players have no more moves
    """
    PLAYER_MAX_TILES = 7

    def __init__(self, players=[1,2], dimension=15, sequenceId="OEIScode"):
        self.board = boardstate(dimension, sequenceId)
        self.players = [Player(p) for p in players] # create players with names
        self.bag = Bag()
        for player in self.players:
            # self.fill_tiles(player)
            player.fill_tiles(self.bag)
        self.next_player = 1
        self.curr_player = self.players[0]

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def move_is_valid(self, move):
        return self.board.is_move_valid(move) and self.player.is_valid(move)

    # move = tuple of triples - row, col, tile value 
    def make_move(self, move):
        # place tiles on board and remove tiles from player's tiles
        self.board.write_data_to_board(move)
        self.player.update_move(move)
        self.bag.update_move(move)
        
        # # take tiles from the bag to replace if one exists
        # self.fill_tiles(player)

        # update current and next players to be set up for next move
        self.curr_player = self.players[self.next_player]
        self.next_player+=1
        self.next_player%=len(self.players)


class Player:
    """
    tiles: array of n tile values such that n <= Game.PLAYER_MAX_TILES
    """
    MAX_TILES = 7

    def __init__(self, pname):
        self.tiles = []
        self.name = pname

    def get_tiles(self):
        return self.tiles

    def add_tile(self, val):
        self.tiles.append(val)
    
    def remove_tile(self, val):
        """
        removes a tile from the list of tiles
        throws an exception if the tile does not exist
        """
        # TODO replace with multiset // collection.Counter
        if self.has_tile:
            self.tiles.remove(val)
            return True
        return False

    def has_tile(self, val):
        # TODO replace with multiset / collection.Counter
        return val in self.tiles

    def is_out_of_tiles(self):
        return len(self.tiles) == 0

    def fill_tiles(self, bag):
        while len(self.tiles) < self.MAX_TILES:
            if bag.is_empty():
                break
            tile = bag.remove_tile()
            self.add_tile(tile)
        

    def is_valid(move):
        # TODO: is this necessary? is it better to validate player tiles just in case? 
        return True


class Bag:
    """
    tiles: list of values representing tiles in the bag; values are single characters (int or char)
        initialized in a random order based on the set distribution
    """
    DIST_DEFAULT = {0: 10, 1:10, 2:10, 3:10, 4:10, 5:10, 6:10, 7:10, 8:10, 9:10}

    def __init__(self, distribution=DIST_DEFAULT):
        self.tiles = []
        for key, val in distribution.items():
            self.tiles.extend([key]*val)
        random.shuffle(self.tiles)
    
    def remove_tile(self):
        """
        returns the first tile and removes it from bag state
        returns None when no tiles are left
        """
        try:
            return self.tiles.pop(0)
        except KeyError:
            return None

    def is_empty(self):
        return len(self.tiles) == 0


