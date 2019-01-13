import sys

chess_table ={'A-11':'9', 'B-11':'8', 'C-11':'7','D-11':'6', 'E-11':'5', 'F-11':'4','G-11':'3', 'H-11':'2', 'I-11':'1',
			  'A-10':' ', 'B-10':' ', 'C-10':' ','D-10':' ', 'E-10':'0', 'F-10':' ','G-10':' ', 'H-10':' ', 'I-10':' ',
			  'A-9':' ', 'B-9':' ', 'C-9':' ','D-9':' ', 'E-9':' ', 'F-9':' ','G-9':' ', 'H-9':' ', 'I-9':' ',
			  'A-8':' ', 'B-8':' ', 'C-8':' ','D-8':' ', 'E-8':' ', 'F-8':' ','G-8':' ', 'H-8':' ', 'I-8':' ',
			  'A-7':' ', 'B-7':' ', 'C-7':' ','D-7':' ', 'E-7':' ', 'F-7':' ','G-7':' ', 'H-7':' ', 'I-7':' ',
			  'A-6':' ', 'B-6':' ', 'C-6':' ','D-6':' ', 'E-6':' ', 'F-6':' ','G-6':' ', 'H-6':' ', 'I-6':' ',
			  'A-5':' ', 'B-5':' ', 'C-5':' ','D-5':' ', 'E-5':' ', 'F-5':' ','G-5':' ', 'H-5':' ', 'I-5':' ',
			  'A-4':' ', 'B-4':' ', 'C-4':' ','D-4':' ', 'E-4':' ', 'F-4':' ','G-4':' ', 'H-4':' ', 'I-4':' ',
			  'A-3':' ', 'B-3':' ', 'C-3':' ','D-3':' ', 'E-3':' ', 'F-3':' ','G-3':' ', 'H-3':' ', 'I-3':' ',
			  'A-2':' ', 'B-2':' ', 'C-2':' ','D-2':' ', 'E-2':'0', 'F-2':' ','G-2':' ', 'H-2':' ', 'I-2':' ',
			  'A-1':'1', 'B-1':'2', 'C-1':'3','D-1':'4', 'E-1':'5', 'F-1':'6','G-1':'7', 'H-1':'8', 'I-1':'9'}

def printChess(board):
	print(board['A-11']+"|"+board['B-11'] + "|" + board['C-11']+  "|" +  board['D-11']+"|"+board['E-11'] + "|" + board['F-11']+  "|" + board['G-11']+"|"+board['H-11'] + "|" + board['I-11'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-10']+"|"+board['B-10'] + "|" + board['C-10']+ "|" +  board['D-10']+"|"+board['E-10'] + "|" + board['F-10']+  "|" + board['G-10']+"|"+board['H-10'] + "|" + board['I-10'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-9']+"|"+board['B-9'] + "|" + board['C-9']+  "|" + board['D-9']+"|"+board['E-9'] + "|" + board['F-9']+  "|" + board['G-9']+"|"+board['H-9'] + "|" + board['I-9'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-8']+"|"+board['B-8'] + "|" + board['C-8']+  "|" + board['D-8']+"|"+board['E-8'] + "|" + board['F-8']+  "|" + board['G-8']+"|"+board['H-8'] + "|" + board['I-8'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-7']+"|"+board['B-7'] + "|" + board['C-7']+  "|" + board['D-7']+"|"+board['E-7'] + "|" + board['F-7']+  "|" + board['G-7']+"|"+board['H-7'] + "|" + board['I-7'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-6']+"|"+board['B-6'] + "|" + board['C-6']+  "|" + board['D-6']+"|"+board['E-6'] + "|" + board['F-6']+  "|" + board['G-6']+"|"+board['H-6'] + "|" + board['I-6'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-5']+"|"+board['B-5'] + "|" + board['C-5']+  "|" + board['D-5']+"|"+board['E-5'] + "|" + board['F-5']+  "|" + board['G-5']+"|"+board['H-5'] + "|" + board['I-5'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-4']+"|"+board['B-4'] + "|" + board['C-4']+  "|" + board['D-4']+"|"+board['E-4'] + "|" + board['F-4']+  "|" + board['G-4']+"|"+board['H-4'] + "|" + board['I-4'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-3']+"|"+board['B-3'] + "|" + board['C-3']+  "|" + board['D-3']+"|"+board['E-3'] + "|" + board['F-3']+  "|" + board['G-3']+"|"+board['H-3'] + "|" + board['I-3'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-2']+"|"+board['B-2'] + "|" + board['C-2']+  "|" + board['D-2']+"|"+board['E-2'] + "|" + board['F-2']+  "|" + board['G-2']+"|"+board['H-2'] + "|" + board['I-2'] + "|")
	print('-+-+-+-+-+-+-+-+-+')
	print(board['A-1']+"|"+board['B-1'] + "|" + board['C-1']+  "|" + board['D-1']+"|"+board['E-1'] + "|" + board['F-1']+  "|" + board['G-1']+"|"+board['H-1'] + "|" + board['I-1'] + "|")

# printChess(chess_table)



def checknganghaydoc(quanco, vitriquandi):
	#check di doc
	if quanco[:1] == vitriquandi[:1]:
		if abs(int(vitriquandi[2:]) - int(quanco[2:])) <= min(int(quanco[2:]), int(vitriquandi[2:])):
			return True
	#check di ngang
	if  quanco[2:] == vitriquandi[2:]:
		if abs(int(vitriquandi[2:]) - int(quanco[2:])) <= abs(min(int(quanco[2:]), int(vitriquandi[2:]))):
			return True
	return False


def cong(quanco, vitriquandi):
	#checkngang
	if quanco[:1] == vitriquandi[:1] and abs(int(quanco[2:]) - int(vitriquandi[2:])) == 1:
		result = int(quanco[2:]) + int(vitriquandi[2:]) 
		return result
	return False


print("Nhap ten nguoi chơi thu 1 : ")
name1 = input()
print("Nhap ten nguoi chơi thu 2 : ")
name2 = input()
# for i in range(100000):
printChess(chess_table)

for i in range(1000000):
	if i % 2 == 0 :
		turn = name1
	else:
		turn = name2
	print("This is turn of %s, type your choice: " %turn)
	ocoduocchon = input() # nhap vao so se duoc chon 1
	vitriquandodi = input() # nhap vao vi tri cua no se di A-2
	if checknganghaydoc(ocoduocchon, vitriquandodi) == False:
		print("Nhap lai cho dung")
	else :
		for a, b in chess_table.items():
			if ocoduocchon == a :
				chess_table[a] = ' '
				chess_table[vitriquandodi] = b

			# chess_table[]
		printChess(chess_table)
		print('-------------------------------------')	

