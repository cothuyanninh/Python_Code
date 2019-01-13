import numpy as np

print("\n"*2)
print("Welcome to Pig_Dice_Game".center(70))
print("Desing by MinhTC4".center(70))
print("\n"*2)
temp = 0

while True:
	try:
		number_player = abs(int(input("Type your number of player: ")))
		break
	except ValueError:
		print("Type again.")

dict_result = {}

while True:
	name = input("Type name of player %d: "%(temp+1))
	if name in dict_result.keys():
		print("Please Type another name. This is not already.")
		continue
	dict_result[name] = 0
	temp += 1
	if temp == number_player:
		break
print("\n"*2)
print("GAME START".center(70))
print("\n"*2)
list_name_player = list(dict_result.keys())

def typeChoice():
	while True:
			try:
				choice_type = int(input("This is number random of this turn: %d. \n1. Again \n2. Hold\nType your choice: "))
				if choice_type in [1,2]:
					return choice_type
			except ValueError:
				print("Type again!")

end_game = 1
while end_game == 1:
	for i in range(len(dict_result)):
		print("This is turn of %s"%(list_name_player[i]))
		number_random = np.random.randint(1,7)
		if (number_random == 1 ):
			print("Sorry! You can't go continue.")
		else:
			flag1 = 0
			score_temp = 0
			while flag1 == 0:
				choice_type = typeChoice()
				if choice_type == 1:
					




