#cach2tinhgiathua
number = int(input("Nhap so di em: "))

def factory(number):
	if number == 0:
		return 1
	return number*factory(number-1)

print(factory(number))