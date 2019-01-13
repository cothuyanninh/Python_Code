#tinh giai thua cua mot so

number = int(input("Nhap so: "))

factory =1
for i in range(1, number+1):
	factory *= i

print("Ket qua la: %d" %(factory))