import sys

chess_table ={'Top-L':' ', 'Top-M':' ', 'Top-R':' ',
			  'Mid-L':' ', 'Mid-M':' ', 'Mid-R':' ',
			  'Low-L':' ', 'Low-M':' ', 'Low-R':' '}

def printChess(board):
	print(board['Top-L']+"|"+board['Top-M'] + "|" + board['Top-R'])
	print('-+-+-+')
	print(board['Mid-L']+"|"+board['Mid-M'] + "|" + board['Mid-R'])
	print('-+-+-+')
	print(board['Low-L']+"|"+board['Low-M'] + "|" + board['Low-R'])
	print('-+-+-+')

printChess(chess_table)

def checkWiner2(number_a, number_b, number_c):
	if number_a == number_b and number_b == number_c and number_a != ' ':
		return True



def checkWiner(chess_table, turn):
	# TTT
	if (checkWiner2(chess_table['Top-L'], chess_table['Top-M'], chess_table['Top-R'])):
		print("%s has won!" %(turn))
		sys.exit()
	# MMM
	if (checkWiner2(chess_table['Mid-L'], chess_table['Mid-M'], chess_table['Mid-R'])):
		print("%s has won!" %(turn))
		sys.exit()
	#LLL
	if (checkWiner2(chess_table['Low-L'], chess_table['Low-M'], chess_table['Low-R'])):
		print("%s has won!" %(turn))
		sys.exit()
	#TML1
	if (checkWiner2(chess_table['Top-L'], chess_table['Mid-L'], chess_table['Low-L'])):
		print("%s has won!" %(turn))
		sys.exit()
	#TML2
	if (checkWiner2(chess_table['Top-M'], chess_table['Mid-M'], chess_table['Low-M'])):
		print("%s has won!" %(turn))
		sys.exit()
	#TML3
	if (checkWiner2(chess_table['Top-R'], chess_table['Mid-R'], chess_table['Low-R'])):
		print("%s has won!" %(turn))
		sys.exit()
	#TMLcheo1
	if (checkWiner2(chess_table['Top-L'], chess_table['Mid-M'], chess_table['Low-R'])):
		print("%s has won!" %(turn))
		sys.exit()
	#TMLcheo2
	if (checkWiner2(chess_table['Top-R'], chess_table['Mid-M'], chess_table['Low-L'])):
		print("%s has won!" %(turn))
		sys.exit()


#main chinh
turn = 'X'
for i in range(9):
	print("This is turn of %s, type your choice: " %turn)
	name = input()
	chess_table[name] = turn
	printChess(chess_table)
	checkWiner(chess_table, turn)
	if turn == 'X':
		turn = 'O'
	else : 
		turn = 'X'
