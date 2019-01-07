import os
import ast
import shutil
import datetime as dt
# kk = os.listdir("../")
# for i in range(len(kk)):
# 	if kk[i].endswith(".mp4"):
# 		shutil.move("../"+kk[i], os.getcwd())
ngay = 27
thang = 10
minh = open('results.txt', 'r', encoding='utf-8').readlines()
for i in range(len(minh)):
	linh = ast.literal_eval(minh[i])
	b = linh['title']
	c = linh['coment']
	d = linh['tag'][2:-2]
	start_days = dt.datetime(2018,thang,ngay,9,00,00)
	temp = 0
	temp_days = 0
	if (i %4 == 0):
		ngay = (ngay +1) % 31
	elif (i %4 == 1):
		temp = 15
	elif (i %4 == 2):
		temp = 30
	elif (i %4 == 3):
		temp = 45
	if (ngay == 0):
		ngay = 1
		thang = (thang+ 1) % 12
	e = start_days.replace( month = thang ,day = ngay, minute = start_days.minute + temp ).isoformat() + '.0Z'
	a =  u'dm.py --file %s --title "%s" --description "%s" --keywords "%s" --publishAt "%s" '%(str(i)+'.mp4',b, c, d, e)
	# print(a)
	print(e)
	# print('%d/%d'%(i, len(minh)))
	# os.system(a)

# kkk = os.listdir()
# for i in range(len(kkk)):
# 	if kkk[i].endswith(".mp4"):
# 		os.remove(kkk[i])
# --publishedAt "%s"       2018-10-24T15:00:00.0Z