a = int(input("Nhap vao so di: "))

is_check = 1

if a < 2 :
	print("Khong phai so nguyen to")

if a > 2 :
	for i in range(2, int(a/2+1)) :
		if a%i == 0 :
			is_check = 0
			print("Khong phai so nguyen to")
			break

if is_check != 0 : 
	print("La so nguyen to")