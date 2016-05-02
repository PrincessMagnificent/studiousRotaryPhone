from random import randint

board = []
##this creates a list with 5 elements, each of which is actually a list with 5 O's in it.
for x in range(0, 5):
    board.append(["O"] * 5)

##this makes rows that are joined with an empty space instead of [x,d] etc.
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

##to check the right position, tell us where the ship is
print "SHIP LOCATION = X: %i Y: %i" % (ship_row+1,ship_col+1)

# Write your code below!
for turn in range(4):
    print "TURN %i" % (turn+1)
    ##Use except ValueError to avoid non numbers
    try:
        guess_row = int(raw_input("Guess Row:"))-1
        guess_col = int(raw_input("Guess Col:"))-1
    except ValueError:
        print "Not a goddamn number, chummer"
        guess_row = int(raw_input("Guess Row:"))-1
        guess_col = int(raw_input("Guess Col:"))-1
    else:
        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row][guess_col] = "A"
            print_board(board)
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
            print (turn+1)
            print_board(board)
print "THUS THE GAME ENDS"