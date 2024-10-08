# try:
#     from sequences import SequenceManager
# except ImportError:
#     class SequenceManager:
#         def __init__(self, sequence_ID):
#             self.sequence_ID = sequence_ID
#         def verify_number(self, number):
#             print('With no import, {} is allowed. Rule was {}'.format(number, self.sequence_ID))
#             return True

from sequences import SequenceManager

class boardstate:
    def __init__(self, dimension, seq_ID='A001477'):
        self.dimension = dimension
        self.data = [[None] * self.dimension] * self.dimension
        self.sequence_manager = SequenceManager(seq_id='A001477')
        # seq_id='A001477' for the list of all nonnegative integers
    
    # We expect 'move' to be a tuple of 3-tuples where each 3-tuple is a square
    # in the form (row, col, digit)

    def does_move_fit(self, move, verbose=False):
        for square in move:
            row, col, _ = square
            try:
                if self.data[row][col] is not None:
                    print("a space is already taken {}\n".format(move) if verbose else '', end='')
                    return False
            except IndexError:
                print("the move is off the board {}\n".format(move) if verbose else '', end='')
                return False
        return True
    
    def return_next_data(self, move):
        data_next = [list(row) for row in self.data] # creates a temporary copy of the boardstate
        for square in move:
            row, col, digit = square
            data_next[row][col] = digit
        return data_next

    def numbers_from_row(self, row, verbose=False):
        # this takes in a row or column, in the form [1, 2, 6, None, None, 5, None, None] for example
        # and outputs the numbers that need to be tested, for example [126]
        string_expression = ''.join((str(i) if i is not None else '_' for i in row))
        strings = string_expression.split('_')
        strings = tuple(string for string in strings if len(string) >= 2)
        return strings

    def is_number_legal(self, move, verbose=False):
        self.data_next = self.return_next_data(move)
        if move[0][0] == move[1][0]: # the move is a row move
            row_in_question = list(self.data_next[move[0][0]])

        elif move[0][1] == move[1][1]: # the move is a column move
            row_in_question = [row[move[0][1]] for row in self.data_next] # this is actually a column, not a row
            
        else:
            raise ValueError('The move is not confined to one row or one column I think')
        numbers_to_test = self.numbers_from_row(row_in_question)
        print('testing these numbers: {}\n'.format(numbers_to_test) if verbose else '', end='')
        for number in numbers_to_test:
            if not self.sequence_manager.verify_number(int(number)):
                print('this number failed: {}\n'.format(number) if verbose else '', end='')
                return False
        print('they all passed\n' if verbose else '', end='')
        return True

        # number_submitted_as_string = ''
        # print(row_in_question, type(row_in_question))
        # for digit in row_in_question:
        #     if digit is not None:
        #         number_submitted_as_string += str(digit)
        #     else:
        #         break
        # number_submitted = int(number_submitted_as_string)
        # return self.sequence_manager.verify_number(number_submitted)



    def __repr__(self): 
        return 'boardstate({})'.format(self.dimension)
    
    def display(self):
        board_str = ""
        for row in self.data:
            for number in row:
                if number is None:
                    board_str+="_ "
                    print('_', end = ' ')
                else:
                    board_str+=str(number) + ' '
                    print(number, end = ' ')
            board_str+='\n'
            print() # new line
        # board_str+='\n'
        print()
        return board_str

    def to_str(self):
        board_str = ""
        for row in self.data:
            for number in row:
                if number is None:
                    board_str+="_ "
                else:
                    board_str+=str(number) + ' '
            board_str+='\n'
        return board_str
    
    def __str__(self):
        return self.to_str()

    # ##############################
    # is_move_legal and update_board_with_move
    # are the only two functions that need to be
    # accessed from outside the class. 
    # ##############################
    # def is_move_valid(self, move, verbose = False):
    #     return self.does_move_fit(move, verbose=verbose) and self.is_number_legal(move, verbose=verbose)
    def is_move_legal(self, move, verbose=False):
        return self.does_move_fit(move, verbose=verbose) and self.is_number_legal(move, verbose=verbose)


    def update_board_with_move(self, move):
        # print(self.return_next_data(move))
        self.data = self.return_next_data(move)

# def debugging():
#     bs = boardstate(5, 'OEIScode')
#     bs.display()

#     move = ((0,0,1), (0,1,9), (0, 2, 6))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((1,1,1), (2,1,1), (3,1,1))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((2,4,7), (3,4,2), (4,4,9))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((2,2,6), (2,3,6))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((0,3,8), (1,3,8))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((3,2,0), (3,3,0))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

#     move = ((4,2,0), (4,3,0))
#     legal = bs.is_move_legal(move, verbose=True)
#     print(legal)
#     if legal:
#         bs.update_board_with_move(move)
#     bs.display()

if __name__ == '__main__':
    #debugging()
    print('scrabblegamestate.py as __main__')