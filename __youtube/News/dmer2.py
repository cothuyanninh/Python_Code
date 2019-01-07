import os
import ast
import shutil
import datetime as dt

minh = open('./file/content.txt', 'r').read()
linh = ast.literal_eval(minh)
b = linh['title']
c = linh['comment']

# start_days = dt.datetime(2018,thang,ngay,gio,00,00)
# temp = 0
# temp_days = 0

# e = start_days.replace( month = thang ,day = ngay, minute = start_days.minute + temp ).isoformat() + '.0Z'
a =  u'dm.py --file %s --title "%s" --description "%s"'%('1.mp4',b, c)
# print(a)
os.system(a)
