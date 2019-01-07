from urllib import request
for i in range(1,3136):
	url = 'https://www2.nhk.or.jp/school/api3/clip.cgi?kyoka=rika&size=1&sort=ranking&from='+str(i)
	r = request.urlopen(url).read()
	a = r.decode('utf-8')

	index = a.index('dasId')
	minh = a[index+8:index+25]
	ahihi = 'http://www2.nhk.or.jp/school/movie/clip.cgi?das_id=' + minh + '&p=box'
	with open('minh.txt', 'a') as linh:
		linh.write(ahihi)
		linh.write('\n')
		# b = ast.literal_eval(c)