
data = {'Dog' : 'Cho' ,
		'Cat' : 'Meo' ,
		'Cow' : 'Bo', 
		'Bird': 'Chim'}
print(data)


def anhViet(data):
	name_animals = input("Please add your keywords: ")
	if name_animals in data.keys(): 
		print("%s is: %s" %(name_animals, data[name_animals]))
	else :
		print("Dictionary has no this word")

def vietAnh(data):
	ten_cvat = input("Nhap ten muon tim kiem: ")
	if ten_cvat in data.values():
		for name1, name2 in data.items():
			if ten_cvat == name2:
				print("Ten %s torng tieng anh la: %s" %(ten_cvat, name1))
		
	else :
		print("Tu nay khong co trong tu dien.")


print("Tu dien Viet-Anh, Anh Viet")
model = int(input("Moi nhap che do: \n1. V-A  \n2. A-V:\n "))

if model == 1:
	print("You choose English-Viet Dictionary!")
	anhViet(data)
if model == 2:
	print("Ban da chon tu dien Viet Anh! ")
	vietAnh(data)