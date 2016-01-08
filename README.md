# Advanced Tic Tac Toe
This project is meant to analyse a more complex variant of TicTacToe.
## Rules
This variant of TicTacToe is played on a field like this:
```

                  +                 +
                  |                 |
        +    +    |      +    +     |     +    +
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        +    +    |      +    +     |     +    +
                  |                 |
+----------------------------------------------------+
                  |                 |
        +    +    |      +    +     |     +    +
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        +    +    |      +    +     |     +    +
                  |                 |
+----------------------------------------------------+
                  |                 |
        +    +    |      +    +     |     +    +
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        |    |    |      |    |     |     |    |
    +-----------+ |  +-----------+  | +-----------+
        |    |    |      |    |     |     |    |
        +    +    |      +    +     |     +    +
                  |                 |
                  +                 +
```
The inner TicTacToe games are played like classic TicTacToe games. The first
move is played in the inner TicTacToe game at the top left, the field of the
inner game that is chosen, determines the next inner TicTacToe game to be
played. For example let the first move be (2,0) (thus the top right corner of
the top left inner game), then the opponent moves in the top right inner game,
and therefore the game jumps between the fields of the outer TicTacToe game).
If an inner TicTacToe game is won it is marked with the winning player's mark
regarding the outer TicTacToe game (which plays the same winning condition like
classic TicTacToe games).
## Notes
Considering the presented advanced TicTacToe rules some things have to be
noted:
  1. Inner TicTacToe games do not necessarily follow a strict alternation of
players
  2. Already won inner TicTacToe games might be played further (if they are
jumped to) to determin the next outer field to be played in
  3. Jumping into a completed inner game is redirected into the source of the
jump (if this leads to a loop the opposing player might chose the field the
game is continued in)

## Implementation
This is mostly a small project to practice Python. Thus, there is no goal or
ambition where this leads to. Possible future goals might include:
  1. Finding an optimal strategy for small dimensions
  2. Increasing the dimension of the game in order to make a computation of
winning regions impossible
  3. Trying to write an AI to play this game (more interesting for higher
dimensions)

