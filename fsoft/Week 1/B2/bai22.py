input_word1 = input("Type 1:").split(",")
print(input_word1)
input_word2 = input("Type 2:").split(",")
print(input_word2)
input_word1.sort()
input_word2.sort()
flag = 0
if len(input_word2) == len(input_word1):
	for i in range(len(input_word1)):
		if (input_word1[i] != input_word2[i]):
			flag = 1

if (flag == 1):
	print("Diff")
else:
	print("Same")