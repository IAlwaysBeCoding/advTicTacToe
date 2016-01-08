#!/usr/bin/env python
DIMENSION = range(0,3)
PLAYER_ENTRY = [0,-1,1]
WINNING_SUM = list(map(lambda x: len(DIMENSION)*x, PLAYER_ENTRY))

class IllegalMove(Exception):
    def __init__(self, board, move):
        self.current_board = board
        self.erronous_move = move
    def __str__(self):
        return 'Board:\n' + str(self.current_board) + '\nMove: ' + str(self.erronous_move)

class Tictactoe():
    def __init__(self, base=None):
        def init_inner_tictactoe():
            inner_field = []
            for i in DIMENSION:
                inner_field.append([])
                for j in DIMENSION:
                    inner_field[i].append(0)
            return inner_field

        if not base:
            self.field = init_inner_tictactoe()
            self.has_winner = False
            self.winner = 0
        else:
            self.field = base.field.copy()
            self.has_winner = base.has_winner
            self.winner = base.winner
    def possible_moves(self):
        moves = []
        for x in DIMENSION:
            for y in DIMENSION:
                if self.field[x][y] == 0:
                    moves.append((x,y))
        return moves

    def apply_move(self, x, y, player):
        if not self.field[x][y] == 0:
            raise IllegalMove(self, (x,y))
        else:
            def is_on_diagonal(x,y):
                return x == y or x == len(DIMENSION) - y - 1
            self.field[x][y] = player
            if not self.has_winner:
                column_sum = sum([PLAYER_ENTRY[self.field[x][v]] for v in DIMENSION])
                row_sum = sum([PLAYER_ENTRY[self.field[v][y]] for v in DIMENSION])
                maindiagonal_sum = sum([PLAYER_ENTRY[self.field[v][v]] for v in DIMENSION])
                counterdiagonal_sum = sum([PLAYER_ENTRY[self.field[v][len(DIMENSION) - v - 1]] for v in DIMENSION])
                sums = [column_sum, row_sum, maindiagonal_sum, counterdiagonal_sum]
                if WINNING_SUM[player] in sums:
                    self.has_winner = True
                    self.winner = player
    def __str__(self):
        return_string = ''
        for x in DIMENSION:
            return_string += str(self.field[x]) + '\n'
        return return_string

class Adv_Tictactoe():
    pass


if __name__ == "__main__":
    game = Tictactoe()
    curr_player = 1
    try:
        while not game.has_winner:
            print(str(game))
            while True:
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
        print("Player ", game.winner, " has won!")
    except IllegalMove as im:
        print("Ups, something went wrong")
        print("Move: ", im.erronous_move, " is not considered valid in:")
        print(im.current_board)
    except (KeyboardInterrupt, EOFError):
        print("\nStopping game...")

