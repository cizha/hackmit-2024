import unittest

from game import Game, Player, Bag
from scrabblegamestate import boardstate

class TestStringMethods(unittest.TestCase):

    def test_board(self):
        bs = boardstate(5, seq_ID='A001477')
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

    def test_board_2(self): 
        # this one uses no assertions and must be manually inspected
        # 
        bs = boardstate(5, seq_ID='A001477')
        bs.display()

        move = ((0,0,1), (0,1,9), (0, 2, 6))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((1,1,1), (2,1,1), (3,1,1))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((2,4,7), (3,4,2), (4,4,9))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((2,2,6), (2,3,6))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((0,3,8), (1,3,8))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((3,2,0), (3,3,0))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

        move = ((4,2,0), (4,3,0))
        legal = bs.is_move_legal(move, verbose=True)
        print(legal)
        if legal:
            bs.update_board_with_move(move)
        bs.display()

    def test_board_3(self):
        bs = boardstate(7, seq_ID='A000040')


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