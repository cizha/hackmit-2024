try:
    from sequences import SequenceManager
except ImportError:
    class SequenceManager:
        def __init__(self, sequence_ID):
            self.sequence_ID = sequence_ID
        def verify_number(self, number):
            print('With no import, {} is allowed. Rule was {}'.format(number, self.sequence_ID))
            return True

class gamestate:
    def __init__(self, dimension, sequence_ID):
        self.dimension = dimension
        self.data = [[None] * self.dimension] * self.dimension
        self.sequence_manager = SequenceManager(sequence_ID)
        pass
    
    # We expect 'move' to be a tuple of 3-tuples where each 3-tuple is a square
    # in the form (row, col, digit)

    def does_move_fit(self, move):
        for square in move:
            row, col, _ = square
            if self.data[row][col] is not None:
                return False
        return True
    
    def return_next_data(self, move):
        data_next = [list(row) for row in self.data] # creates a temporary copy of the gamestate
        for square in move:
            row, col, digit = square
            data_next[row][col] = digit
        return data_next

    def is_number_legal(self, move):
        self.data_next = self.return_next_data(move)
        if move[0][0] == move[1][0]: # the move is a row move
            row_in_question = list(self.data_next[move[0][0]])[move[0][1]:]

        elif move[0][1] == move[1][1]: # the move is a column move
            row_in_question = [row[move[0][1]] for row in self.data_next][move[0][0]] # this is actually a column, not a row
            
        else:
            raise ValueError('The move is not confined to one row or one column I think')
        
        number_submitted_as_string = ''
        print(row_in_question, type(row_in_question))
        for digit in row_in_question:
            if digit is not None:
                number_submitted_as_string += str(digit)
            else:
                break
        number_submitted = int(number_submitted_as_string)
        return self.sequence_manager.verify_number(number_submitted)


    def is_move_legal(self, move):
        return self.does_move_fit(move) and self.is_number_legal(move)

    def update_data_with_move(self, move):
        # print(self.return_next_data(move))
        self.data = self.return_next_data(move)




    ##############################
    # This is the only function 
    # that needs to be called
    # from outside of the class.
    ##############################
    # If the move is illegal, it returns False.
    # If the move is legal, it it returns True
    # and updates self.data
    ##############################
    def receive_move(self, move):
        if not self.does_move_fit(move):
            return False
        elif not self.is_number_legal(move):
            return False
        self.update_data_with_move(move)
        return True


    def __repr__(self): 
        return 'gamestate({})'.format(self.dimension)
    
    def display(self):
        for row in self.data:
            for number in row:
                if number is None:
                    print('_', end = ' ')
                else:
                    print(number, end = ' ')
            print() # new line
        print()

def debugging():
    gs = gamestate(5, 'OEIScode')
    gs.display()

    move = ((1,1,1), (1,2,1))
    print(gs.receive_move(move))
    gs.display()

    move = ((2,1,1), (3,1,1))
    print(gs.receive_move(move))
    gs.display()

if __name__ == '__main__':
    debugging()