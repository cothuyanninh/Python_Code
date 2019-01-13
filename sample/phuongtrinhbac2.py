print("Tinh cac nghiem cua phuong trinh bac 2 : ax^2 + bx + c= 0")

a = int(input ("Moi nhap a: "))
b = int(input ("Moi nhap b: "))
c = int(input ("Moi nhap c: "))

delta = b*b - 4*a*c

if (a ==0 and b== 0 and c== 0):
	print("Phuong trinh vo so nghiem")
if (a == 0 and b!= 0):
	print("Phuong trinh co nghiem duy nhat: %f" %(float(-c/b)))
if (a!=0):
	if (delta < 0 ):
		print("Phuong trinh vo nghiem")
	if (delta == 0 ):
		print("Phuong trinh co nghiem kep: %f" %(float(-b/2*a)))
	if (delta > 0):
		print("Phuong trinh co 2 nghiem phan biet: %d va %d" %(-delta, delta))
