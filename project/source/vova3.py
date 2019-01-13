from getDataFromWord import get_docx_text
from findPhoneFromData import findNumberPhone

linkfile = 'C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\input\\word\\Nguyen-Van-Nam-TopCV.vn-210918.224852-converted.docx'

print(get_docx_text(linkfile))

print('------------------------------------')

print(findNumberPhone(get_docx_text(linkfile)))