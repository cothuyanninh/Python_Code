print("Tinh tong cac chu so")

start = int(input("Nhap vao so bat dau: "))
stop = int(input("Nhap vao so ket thuc: "))

result = 0

for i in range(start, stop+1):
	result += i

print ("Tong la: %d" % (result))