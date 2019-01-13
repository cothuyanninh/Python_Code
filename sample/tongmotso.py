print("Tinh tong cac chuc so cua mot so")

number = input("Nhap vao mot so nguyen di: ")

result =0

for i in list(number):
	result += int(i)

print("Tong cac chu so la: %d" %(result))