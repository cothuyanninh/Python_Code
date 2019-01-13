input_words = []
for i in range(4):
	print("Student (name, age, score): ")
	input_words.append(tuple(input().split(",")))
input_words.sort()
print(input_words)