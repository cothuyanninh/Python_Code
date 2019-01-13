import docx, os
from scanFromWord import scanFromWORD
from scanFromPdf import scanFromPDF
from scanFromTxt import scanFromTXT
from counterFile import counterFile
from insertDataBase import insertToDataBaseFirst, insertToDataBaseSecond, showDatabase
# from getAvatarFromLink import getLinkPicture


counterFile()

list_word = []
list_pdf  = []
file_input = '..//data//input'
file_word  = file_input + '//' + 'word'
file_pdf   = file_input + '//' + 'pdf'
file_txt   = file_input + '//' + 'txt'

print("Processing link CV in txt")

for var_i in range(len(os.listdir(file_txt))):
 	#print(scanFromTXT(file_txt +'\\' + os.listdir(file_txt)[var_i]))
 	result_txt = scanFromTXT(file_txt +'\\' + os.listdir(file_txt)[var_i])
 	insertToDataBaseFirst(result_txt)
 	# getLinkPicture(file_txt + +'\\' + os.listdir(file_txt)[var_i])

 	#print(result_txt)
 	#file_save_inf.write(str(result_txt).encode('unicode'))
showDatabase()

print("Processing CV Word")
for var_i in range(len(os.listdir(file_word))):
	result_word = scanFromWORD(file_word +'\\' + os.listdir(file_word)[var_i])
	list_word.append(result_word)

insertToDataBaseSecond(list_word)
showDatabase()

print("Processing CV PDF")

for var_i in range(len(os.listdir(file_pdf))):
	minh = file_pdf +'\\' + os.listdir(file_pdf)[var_i]
	if minh.endswith('.pdf'):
		result_pdf = scanFromPDF(file_pdf +'\\' + os.listdir(file_pdf)[var_i])
		list_pdf.append(result_pdf)

insertToDataBaseSecond(list_pdf)


showDatabase()

#download anh

