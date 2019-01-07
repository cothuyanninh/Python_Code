import bs4
import requests
import re
# minh = open('Special.html', encoding ='utf-8')
# linh = bs4.BeautifulSoup(minh.read(), 'lxml')
# elems =linh.select('a')
# result = []
# print(elems[100].getText())
# for i in range(len(elems)):
# 	if elems[i].getText().endswith("p=box"):
# 		result.append(elems[i])
# print(result)
minh = open("Special.html", 'r', encoding = 'utf-8').read()
list_link = []
a = re.compile(r'www2.{62}p=box')
b = a.findall(minh)
with open('Special.txt', 'w', encoding='utf-8') as linh:
	for i in range(len(b)):
		linh.write('http://')
		linh.write(b[i])
		linh.write('\n')
