import numpy as np 

list_result = []
for i in range(10):
	score = 0
	print("*"*20)
	temp = 0
	while score < 50:
		# print("This is turn of %dth player."%(i+1))
		step_random = np.random.randint(1,7)
		# print("Player have dice is: %d"%step_random)
		if step_random == 1 and score > 0:
			score -= 1
		elif step_random in [2,3,4,5]:
			score += 1
		else:
			score += np.random.randint(2,7)
		# print("Score in this turn : ", score)
		temp += 1
	list_result.append([i+1, temp])

print(list_result)