#!/usr/bin/env python
from itertools import chain

class IllegalMove(Exception):
    def __init__(self, board, move):
        self.current_board = board
        self.erronous_move = move
    def __str__(self):
        return 'Board:\n' + str(self.current_board) + '\nMove: ' + str(self.erronous_move)

class Tictactoe():
    PLAYER_ENTRY = [0, -1, 1]

    def __init__(self, dimension = 3, base = None):
        
        init_inner_tictactoe = lambda d : list([0] * len(d)  for i in range(len(d)))
        
        if not base:
            self.has_winner = False
            self.winner = 0
            self.dimension = range(0, dimension)
            self.winning_sum = list(map(lambda x: len(self.dimension) * x, Tictactoe.PLAYER_ENTRY))
            self.field = init_inner_tictactoe(d=self.dimension)
        else:
            self.has_winner = base.has_winner
            self.winner = base.winner
            self.dimension = base.dimension
            self.winning_sum = base.winning_sum
            self.field = base.field.copy()

	def possible_moves(self):
		
        is_empty = lambda x, y :(x, y) if self.field[x][y] == 0 else False
        d = len(self.dimensions)
        result = [is_empty(i/d, (i % d)) for i, value in enumerate(chain.from_iterable(self.field))]
		
        return filter(lambda r : r  , result)
		
    def apply_move(self, x, y, player):
        if not self.field[x][y] == 0:
            raise IllegalMove(self, (x, y))
        else:
            def is_on_diagonal(x, y):
                return x == y or x == len(self.dimension) - y - 1

            self.field[x][y] = player
            if not self.has_winner:
                column_sum = sum([Tictactoe.PLAYER_ENTRY[self.field[x][v]] for v in self.dimension])
                row_sum = sum([Tictactoe.PLAYER_ENTRY[self.field[v][y]] for v in self.dimension])
                maindiagonal_sum = sum([Tictactoe.PLAYER_ENTRY[self.field[v][v]] for v in self.dimension])
                counterdiagonal_sum = sum([Tictactoe.PLAYER_ENTRY[self.field[v][len(self.dimension) - v - 1]] for v in self.dimension])
                sums = [column_sum, row_sum, maindiagonal_sum, counterdiagonal_sum]
                if self.winning_sum[player] in sums:
                    self.has_winner = True
                    self.winner = player
    def __str__(self):
        return_string = ''
        for x in self.dimension:
            return_string += str(self.field[x]) + '\n'
        return return_string

class Adv_Tictactoe():
    pass


if __name__ == "__main__":
    game = Tictactoe(3)
    curr_player = 1
    try:
        while not game.has_winner:
            print(game)
            while True:
                print("Player", curr_player, ":")
                curr_x = int(input("x:"))
                curr_y = int(input("y:"))
                if (curr_y, curr_x) in game.possible_moves():
                    break
                else:
                    print('not a valid move, try one of the following:',
                            game.possible_moves())
                    continue
            game.apply_move(curr_y, curr_x, curr_player)
            curr_player = 3 - curr_player
            
        print("Player", game.winner, "has won!")
    except IllegalMove as im:
        print("Ups, something went wrong")
        print("Move:", im.erronous_move, "is not considered valid in:")
        print(im.current_board)
    except (KeyboardInterrupt, EOFError):
        print("\nStopping game...")
