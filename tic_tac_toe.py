# Using list as my data sctructure. What I could do here is
# board=[" "," "," "," "," "," "," "," "," "], but i'm
# going to go with list pomprehension:

board = [" " for i in range(9)]

# Let's create a function, you know, to make our board look a lot like real game board!

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8]) # the same can be done using for loop

    print() # just looks nice
    print(row1)
    print(row2)
    print(row3)
    print() # ...same thing here

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
            number = 2
            
    print("Your turn player {}".format(number))
    
    choice = int(input("Please enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon # so if it's X or O, the game works the same way
    else:
        print()
        print("This move is taken!")

def is_victory(icon): # there're 8 ways to win, so...
    if (board[0] == icon and board[1] == icon and board[2] == icon) or\
       (board[3] == icon and board[4] == icon and board[5] == icon) or\
       (board[6] == icon and board[7] == icon and board[8] == icon) or\
       (board[0] == icon and board[3] == icon and board[6] == icon) or\
       (board[1] == icon and board[4] == icon and board[7] == icon) or\
       (board[2] == icon and board[5] == icon and board[8] == icon) or\
       (board[0] == icon and board[4] == icon and board[8] == icon) or\
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
        
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("Congratulations! The winner is X")
        break
    elif is_draw():
        print("Hmmm... It's a draw!")
        break
        
    player_move("O")
    if is_victory("O"):
        print_board()
        print("Congratulations! The winner is O")
        break
    elif is_draw():
        print("Hmmm... It's a draw!")
        break
