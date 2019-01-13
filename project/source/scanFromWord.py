import docx, re, os
from findPhoneFromData import findNumberPhone
from findEmailFromData import findEmail
from findNameFromData import findName
from getDataFromWord import get_docx_text, check_Face_in_picture

def scanFromWORD(linkFile):
	listformWord= ['word']
	var_name = findName(get_docx_text(linkFile).split('\n'))
	listformWord.append(var_name)
	var_phone = findNumberPhone(get_docx_text(linkFile))
	listformWord.append(var_phone)
	var_email = findEmail(get_docx_text(linkFile))
	listformWord.append(var_email)
	listformWord.append(os.path.basename(linkFile))

	check_Face_in_picture(linkFile)



	return listformWord