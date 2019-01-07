minh = open('./xls_result/hihi.txt', 'r').readlines()
for i in range(len(minh)):
	print(minh[i].split('\t')[0])