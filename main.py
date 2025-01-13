class Tic_Tac_Toe:
    def __init__(self):
        self.__board = [[' ' for _ in range(3)] for _ in range(3)]  # Private board
        self.__score_x = 0  # Private score for player X
        self.__score_o = 0  # Private score for player O
        self.__current_player = ''  # Private current player

    def display(self):
        for row in self.__board:  # Accessing the private board
            print('|'.join(row))  # Join and print each row
            print('-' * 5)  # Separator for better display
        print('Score of O:', self.__score_o)  # Accessing private scores
        print('Score of X:', self.__score_x)

    def to_play(self):
        try:
            z = input("Enter your move (i,j,player): ")
            i, j, player = z.split(',')
            i, j = int(i), int(j)  # Convert coordinates to integers

            if player not in ['X', 'O']:
                print("Invalid player! Use 'X' or 'O'.")
                return False

            if 0 <= i < 3 and 0 <= j < 3:  # Ensure valid indices
                if self.__board[i][j] == ' ':
                    if self.__current_player != player:
                        self.__current_player = player
                    else:
                        print(f"Don't repeat player {self.__current_player}")
                        return False
                    self.__board[i][j] = player
                    return True
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid coordinates. Try again.")
        except Exception as e:
            print("Invalid input format. Use 'i,j,player' (e.g., 1,2,X).")
        return False

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] != ' ':  # Row check
                if self.__board[i][0] == 'X':
                    self.__score_x += 1
                else:
                    self.__score_o += 1
                return self.__board[i][0]
            if self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != ' ':  # Column check
                return self.__board[0][i]

        # Check diagonals
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != ' ':
            return self.__board[0][0]
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != ' ':
            return self.__board[0][2]

        return None  # No winner yet

    def is_draw(self):
        for row in self.__board:
            if ' ' in row:  # If there's an empty cell, it's not a draw
                return False
        return True

    def reset_board(self):
        """Resets the board for a new game."""
        self.__board = [[' ' for _ in range(3)] for _ in range(3)]
        self.__current_player = ''

# Create an instance of the game
tic_tac_toe = Tic_Tac_Toe()


# Main game loop
while True:
    tic_tac_toe.display()
    if not tic_tac_toe.to_play():
        continue  # If the move is invalid, retry

    winner = tic_tac_toe.check_winner()
    if winner:
        tic_tac_toe.display()
        print(f"Player {winner} wins!")
        tic_tac_toe.reset_board()  # Reset the board for a new game
        continue

    if tic_tac_toe.is_draw():
        tic_tac_toe.display()
        print("It's a draw!")
        tic_tac_toe.reset_board()  # Reset the board for a new game
