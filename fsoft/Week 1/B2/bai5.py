sum_odd = 0
sum_even = 0
while (True):
	number = int(input("Enter a number (0 to exit): "))
	if number == 0:
		print("Absolute different of even and odd numbers: ", abs(sum_even - sum_odd))
		break
	if number %2 == 0:
		sum_even += number
	else:
		sum_odd += number
	print("Odd sum: %d even sum: %d"%(sum_odd, sum_even))