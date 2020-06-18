# from Ipython.display import clear_output
import random
def display_board(board):
	print('\n'*100)
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

# test_board = ['#' , 'X' , 'O' ,'X' , 'O' ,'X' , 'O' ,'X' , 'O' ,'X']
# display_board(test_board)

def player_input():
	'''
	OUTPUT  = (Player 1 marker , Player 2 marker)

	'''
	marker = ''

	while marker != 'X' and marker != 'O':
		marker = input('Player 1 : Choose your marker X or O : ').upper()

	if marker == 'X':
		return ('X' , 'O')

	else:
		return ('O' , 'X')

def place_marker(board , marker , position):
	board[position] = marker

# place_marker(test_board , '$' , 8)
# display_board(test_board)

def win_check(board , mark):
	# win tic tac toe?
	return board[7] == mark and board[8] == mark and board [9] == mark or  board[4] == mark and board[5] == mark and board [6] == mark or board[1] == mark and board[2] == mark and board [3] == mark or board[7] == mark and board[4] == mark and board [1] == mark or board[8] == mark and board[5] == mark and board [2] == mark or board[9] == mark and board[6] == mark and board [3] == mark or board[7] == mark and board[5] == mark and board [3] == mark or board[7] == mark and board[5] == mark and board [1] == mark

# res = win_check(test_board , 'X')
# print(res)
def choose_first ():
	flip = random.randint(0,1)
	if(flip == 0):
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board , position):
	#check if the position selected is blank or not
	return board[position] == ' '

def full_board_check(board):
	#check for the entire board that whether any space left or not
	for i in range(1,10):
		if space_check(board , i):
			return False

	return True
			
def player_choice (board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board , position ):
		position = int (input('Choose a postion : (1-9)'))

	return position

def replay():
	choice = input("Play Again ? Yes or No :")

	return choice == 'Yes'

#Now we'll write the block to run the game
print("Welcome to the Tic Tac Toe designed by - Shivam")
while True:

#set up all the variables
	the_board = [' ']*10  #initially the board will be empty 

	( player1_marker , player2_marker ) = player_input()

	turn = choose_first()  # randomly decide which player will move first

	play_game = input('Ready to play ? y or n ? ') #ask for the last time whether want to play or not

	if play_game.lower() == 'y':
		game_on = True  #A boolean variable to keep the user's wish 
	else:
		game_on = False


## game on 
	while game_on:
		if turn == 'Player 1':
			##player one turn
			
			#show the board to user at starting
			display_board(the_board) 
			#choose a position where the user want to put his marker
			position = player_choice(the_board)
			#place the marker on the selected position 
			place_marker(the_board , player1_marker , position)

			#check if won 
			if win_check(the_board , player1_marker) :
				display_board(the_board)
				print("Player 1 Won !!")
				game_on = False
			else:
				turn = 'Player 2'

		else:
			## player two turn
			#show the board to user at starting
			display_board(the_board) 
			#choose a position where the user want to put his marker
			position = player_choice(the_board)
			#place the marker on the selected position 
			place_marker(the_board , player2_marker , position)

			#check if won 
			if win_check(the_board , player2_marker) :
				display_board(the_board)
				print("Player 1 Won !!")
				game_on = False
			else:
				turn = 'Player 1'

# Ask if want to play again ?

	if not replay():
		break