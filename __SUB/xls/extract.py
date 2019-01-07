# import pandas

# df = pandas.read_csv('ll.csv', encoding = 'utf-8')
# print(df.columns)

minh = open('kk.txt', 'r').readlines()
linh = open('result.txt', 'a')

for i in range(1,len(minh)):
	a = minh[i].split('\t')
	# print(str(a[0][2:-2]))
	msv = str(a[0][2:-2])
	name = a[1][4:-3].replace(" ","") + '_t62@hus.edu.vn'
	# print(b)



	linh.write(str(i)+ '\t' + msv + '\t' + name + '\n')
	# a[0] = a[0].replace(" ", "")
	# print(a[0])
	# print(a[2][3:])
	# print(a[1][6:])
	# b = a[1].split('\n')[0].replace(" ", "")[6:] + '_t'+ str(int(a[0].replace(" ","")[0:2]) + 45) +'@hus.edu.vn'
	# # print(b)
	# linh.write(str(i) +'\t' + a[0]+ '\t' + b + '\n')
	# if (minh[4][-12:] == '@hus.edu.vn')