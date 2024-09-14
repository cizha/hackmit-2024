class gamestate:
    def __init__(self, dimension):
        self.dimension = dimension
        self.data = [[None] * 10] * self.dimension
        pass
    
    # We expect 'move' to be a tuple of 3-tuples where each 3-tuple is a square
    # in the form (row, col, digit)

    def does_move_fit(self, move):
        for square in move:
            row, col, _ = move
            if self.data[row][col] is not None:
                return False
        return True
    
    def generate_next_data(self, move):
        for square in move:
            row, col, digit = move
            self.data_next = [list[row] for row in self.data] # creates a temporary copy of the gamestate
        if move[0][0] == move [1][0]: # the move is a row move
            row_in_question = list(self.data_next[move[0][0]])

        elif move[0][1] == move[1][1]: # the move is a column move
            col_in_question = [row[move[0][1]] for row in self.data_next]
        else:
            raise ValueError('The move is not confined to one row or one column I think')
    
    def is_number_legal(self, move):



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
