minh = open('minh.txt', 'r', encoding='utf8').readlines()
ahihi = '0.txt'
for i in range(len(minh)):
	if i%20 ==0:
		ahihi = '%d.txt'%(i)
	a = open(ahihi, 'a', encoding= 'utf8')
	a.write(minh[i])