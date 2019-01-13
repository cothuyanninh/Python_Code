string_word = input("Type: ")
sum_upper = 0
sum_lower = 0
for i in string_word:
	if (i >= "a" and i <= "z"):
		sum_lower += 1
	if (i >= "A" and i <= "Z"):
		sum_upper += 1
print("Upper: ", sum_upper)
print("Lower: ", sum_lower)