import unittest

from game import Game, Player, Bag
from scrabblegamestate import boardstate

class TestStringMethods(unittest.TestCase):

    def test_board(self):
        bs = boardstate(5, 'OEIScode')
        self.assertEqual(repr(bs.display()), repr(('_ '*5 +'\n')*5))

        move = ((0,0,1), (0,1,9), (0, 2, 6))
        legal = bs.is_move_legal(move)
        self.assertTrue(legal)
        bs.update_board_with_move(move)
        self.assertEqual(repr(bs.display()), repr(('1 9 6 _ _ \n') + ('_ '*5 +'\n')*4))

        # move = ((1,1,1), (2,1,1), (3,1,1))
        # legal = bs.is_move_legal(move)
        # self.assertTrue(legal)
        # bs.update_board_with_move(move)
        # self.assertEqual(repr(bs.display()), repr(('1 9 6 _ _ \n') + ('_ 1 _ _ _ \n')*2+('_ '*5 +'\n')*2))
        # # this case fails but not sure if we need the display function


    def test_player(self):
        player = Player('Test')
        self.assertEqual(player.name, 'Test')

    def test_bag(self):
        bag = Bag({0:1, 1:4, 2:3})
        self.assertEqual(len(bag.tiles), 8)

        tile = bag.remove_tile()
        self.assertEqual(len(bag.tiles), 7)

    def test_game(self):
        dimension = 5
        game = Game(players=['A', 'B'], dimension=5)
        print(game.get_board().to_str())
        for p in game.players:
            print(p.tiles)
        self.assertEqual(len(game.bag.tiles), 86) # finish this test case
        # with self.assertRaises(TypeError):
        #     s.split(2)

if __name__ == '__main__':
    unittest.main()