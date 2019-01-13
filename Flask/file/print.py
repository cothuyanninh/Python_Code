import csv

with open('capitalsquiz35.txt', 'r') as openFileread:
	#loadFile = csv.reader(openFileread)

	#for somelines in loadFile:
	#	print(".".join(somelines))
	print(openFileread.read())