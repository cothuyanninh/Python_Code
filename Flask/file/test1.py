import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\vanquangcz\\Desktop\\python'): 
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF '+ folderName + ': '+ subfolder)
	for filename in filenames :
		print('File inside '+ folderName + ': ' + filename)

print('End')
