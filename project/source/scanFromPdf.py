import docx, re, os
from findPhoneFromData import findNumberPhone
from findEmailFromData import findEmail
from findNameFromData import findName
from getDataFromPdf import pdf_to_text

def scanFromPDF(linkFile):
    listformPdf= ['pdf']
    var_name = findName(pdf_to_text(linkFile).split('\n'))
    listformPdf.append(var_name)
    var_phone = findNumberPhone(pdf_to_text(linkFile))
    listformPdf.append(var_phone)
    var_email = findEmail(pdf_to_text(linkFile))
    listformPdf.append(var_email)
    listformPdf.append(os.path.basename(linkFile))

    return listformPdf
