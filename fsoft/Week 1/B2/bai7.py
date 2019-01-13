while(True):
	number = int(input("Enter a number: "))
	if number == 0:
		break
	# a = [int(i) for i in str(number)]
	# sum_each_number = sum(a)
	if (number<0):
		print("No")
		continue
	for i in range(1,number+1):
		number -= i
		if (number == 0):
			print("Yes")
			break
		if (number < 0):
			print("No")
			break