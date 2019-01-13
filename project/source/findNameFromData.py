from getDataFromWord import get_docx_text

#var_data = get_docx_text('C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\input\\4.docx').split('\n')
list_first_name = '..//lib//listfirstname.docx'
def findName(var_data):
	var_list_first_name = get_docx_text(list_first_name).split('\n')
	for i in range(len(var_list_first_name)):
		if i%2 == 1 :
			var_list_first_name.remove('')


	#print(var_list_first_name)
	name =[]

	for i in range(len(var_list_first_name)) :
		for j in range(len(var_data)):
			if var_list_first_name[i] in var_data[j] and var_data[j].istitle() == True:
				name.append(var_data[j])
	if len(name) != 0 :
		return name[0]
	else:
		return 'Not scaning name'
	





# import docx, re, codecs
# list_first_name_in_VN = []

# #nameRegex = re.complie(r'')
# #Xu li cac ho o Viet Nam
# #chuyen file word thanh du lieu doc duoc
# def getText(filename):
# 	doc = docx.Document(filename)
# 	fullText = []
# 	for para in doc.paragraphs:
# 		fullText.append(para.text)
# 	return '\n'.join(fullText)

# var_data = getText('C:\\Users\\vanquangcz\\Desktop\\python\\project\\source\\listhoinvietnam.docx')
# print(type(var_data))
# # ahihiFile = codecs.open('minh.txt', 'r', 'utf8').read()
# # clgtFile = open('minh2.txt', 'w')
# # clgtFile.write(ahihiFile)

# #ahihiFile.close()
# # luu cac ho vao mot list
# list_first_name_in_VN = var_data.split('\n')
# # list_first_name_in_VN.save('ahihi.txt')
# print(list_first_name_in_VN)
# def findName(rangeName):
# 	nameRegex = re.compile(r'\w+')
# 	mo3 = nameRegex.findall(rangeName)
# 	# if len(mo3) == None:
# 	# 	print('No name found')
# 	# else :
# 	# 	print(mo3)
# 	for i in range(len(mo3)):
# 	 	if mo3[i].istitle() == True :
# 	 		print(mo3[i], end =' ')
# 	 		#ahihiFile.write(str(mo3[i]))
# 	#print(mo3)

	
# #check xem cai ho co san trong list ho co ton tai trong data hay khong

# def findRangeName(data):
# 	for i in range(len(list_first_name_in_VN)):
# 		if list_first_name_in_VN[i] in data:
# 			indexOfFistName = data.index(list_first_name_in_VN[i])
# 			rangeName = data[(indexOfFistName):(indexOfFistName+20)]
# 			#print(rangeName)
# 			return findName(rangeName)

