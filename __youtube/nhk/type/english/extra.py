minh = 'http://www2.nhk.or.jp/school/movie/clip.cgi?das_id=D0005350158_00000&p=box'
a= 'http://www2.nhk.or.jp/school/movie/clip.cgi?das_id=D000'
b= '_00000&p=box'
with open('url.txt', 'w', encoding = 'utf-8') as linh:
	for i in range(5350158, 5350567):
		linh.write(a+ str(i) + b)
		linh.write('\n')