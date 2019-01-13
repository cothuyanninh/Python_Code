print("**************************")
print("Tu dien Anh Viet, Viet Anh")
print("**************************")


data = {'Dog' : 'Cho' ,
		'Cat' : 'Meo' ,
		'Cow' : 'Bo', 
		'Bird': 'Chim'}

def catalogy():
	print("1. Anh - Viet\t 2. Viet - Anh")
	choose = int(input("Choose your number: "))
	if choose == 1:
		showMenu()
	if choose == 2:
		return danhSach()

def showMenu():
	print("1. Add Word")
	print("2. Delete Word")
	print("3. Find Word")
	print("4. See All")
	print("0. Exit")
	print("**************")

	choice = int(input("What is your choice: "))
	while (choice != 0):
		if choice == 1:
			addWord()
		elif choice == 2:
			deleteWord()
		elif choice == 3:
			findWord()
		elif choice == 4:
			showAll()
		elif choice == 0:
			break
		else :
			print("Have no this choice")
		choice = int(input("What is your choice: "))

	print("Good Bye!!")
#
#
# xu li Anh Viet
#
#
# Add word to data
def addWord():
	word = input("Add your word: ")
	mean = input("Mean is : ")
	data[word] = mean;
	print("Add successfully.")

#delete word from data
def deleteWord():
	word = input("Add your word to delete")
	if word in data.keys():
		del data[word]
		print("Delete successfully!")
	else:
		print("Disionary have no this word!!")
#find a word
def findWord():
	word = input("Add your word to find: ")
	if word in data.keys():
		for name1, name2 in data.items():
			if name1 == word:
				print("%s is : %s" %(name1, name2))
				print("Find successfully")
	else: 
		print("Disionary have no this word")

#show all
def showAll():
	for name1, name2 in data.items():
		print("%s is: %s" %(name1, name2))

#
#
# xu li Viet Anh
#
#

#them tu 
def danhSach():
	print("1. Them Tu")
	print("2. Xoa Tu")
	print("3. Tim Tu")
	print("4. Xem ta ca")
	print("0. Thoat")
	print("************")
	luachon = int(input("Ban dinh lam gi: "))
	while (luachon != 0):
		if luachon == 1:
			themTu()
		elif luachon == 2:
			xoaTu()
		elif luachon == 3:
			timTu()
		elif luachon == 4:
			xemHet()
		elif luachon == 0:
			break
		else :
			print("Khong co lua chon nay")
		luachon = int(input("Ban dinh lam gi: "))


	print("Xin chao!!")

#them tu
def themTu():
	tumoi = input("Nhap tu moi: ")
	nghia = input("Nghia la: ")
	data[tumoi] = nghia

#xoa tu
def xoaTu():
	tucanxoa = input("Nhap tu can xoa: ")
	if tucanxoa in data.values():
		for name1, name2 in data.items():
			if name2 == tucanxoa:
				del data[name1]
				print("Xoa thanh cong.")

	else: 
		print("Tu nay khong co trong tu dien.")	

#tim Tu 
def timTu():
	ten_cvat = input("Nhap ten muon tim kiem: ")
	if ten_cvat in data.values():
		for name1, name2 in data.items():
			if ten_cvat == name2:
				print("Ten %s trong tieng anh la: %s" %(ten_cvat, name1))
		
	else :
		print("Tu nay khong co trong tu dien.")

#xem tat ca
def xemHet():
	for name1, name2 in data.items():
		print("Tu %s co nghia la: %s" %(name2, name1))



## Xu li Anh Viet


## main chinh
catalogy()


# xu li Anh Viet
def anhViet(data):
	name_animals = input("Please add your keywords: ")
	if name_animals in data.keys(): 
		print("%s is: %s" %(name_animals, data[name_animals]))
	else :
		print("Dictionary has no this word")
