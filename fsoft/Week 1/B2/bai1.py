while(type(number) == "int")
	number = int(input("Type your number: "))
if i < 0:
	print("Wrong")
else:
	a = {i:i**2 for i in range(number+1)}
print(a)