from random import randint #importing the randint from the random module

print '--------------Welcome to Battleship!-------------'
print ' How many players are playing?(1/2)'
players = int(raw_input())
while players < 1 or players > 2:  #while loop that checks whether there is a vlid number of players
    print 'Sorry not a valid number of players!'
    print 'Enter again:'
    players = int(raw_input())

listOfPlayers = createPlayers(players)
print 'Ok! Lets play!'
print 'Creating board....'
board = [] #empty board

#creating a 5x5 board filled with "Os"
for x in range(0, 5):
    board.append(["O"] * 5)

#Purpose: Print the board
#Parameters: The 5x5 Board list
#Return: The list printed without commas and braces
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board) #printing the board

#Purpose: To create a random int
#Parameter: The 5x5 Board list
#Return: A random int that represents row number
def random_row(board):
    return randint(0, len(board) - 1)

#Purpose: To create a random int
#Parameter: The 5x5 Board list
#Return: A random int that represents column number
def random_col(board):
    return randint(0, len(board[0]) - 1)

#the random postion
ship_row = random_row(board)
ship_col = random_col(board)

#Purpose: Create a list of player dictionaries
#Parameters: An integer, the number of players
#Return: A list of players
def createPlayers(players):
    contestants = []
    while players > 0:
        new = {
        'Name':'',
        'Turn':0,
        }
        name = int(raw_input('What\'s your name?: '))
        new['Name'] = name
        contestants.append(new)
        player -= 1
    return contestants

def round(contestants):
    for turn in range(4):
        print 'Turn', turn + 1 # print the turn youre one
        guess_row = int(raw_input("Guess Row:"))    #the guessed row input
        guess_col = int(raw_input("Guess Col:"))    #the guessed col input

        if guess_row == ship_row and guess_col == ship_col:     #Case 1: If the user guess correctly
            print "Congratulations! You sunk my battleship!"
            break 
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): #Case 2: if the user guess is not in the range of the board
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):       #Case 3: The user has already guessed that combo
                print "You guessed that one already."
            else:                                           #Case 4: The user guessed incorrectly
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            if turn == 3:                           #keeping track of the turns 
                print 'Game Over'
            print_board(board)

#a for loop that gives the user 4 turns

round(contestants)