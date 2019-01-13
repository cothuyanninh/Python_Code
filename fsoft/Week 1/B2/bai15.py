string_word = input("Type: ")
sum_digit = 0
sum_letter = 0
for i in string_word:
	if (i >= "0" and i <= "9"):
		sum_digit+= 1
	if (i > "A" and i< "z"):
		sum_letter += 1
print("Digits: ", sum_digit)
print("Letters: ", sum_letter)