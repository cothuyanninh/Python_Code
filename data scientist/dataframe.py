import pandas as pd 
csv_file = pd.read_csv('http://bit.ly/uforeports')
# print(csv_file.head())
# print(csv_file['City'][0])
# print(csv_file)
# for i in range(len(csv_file)):
# 	if csv_file.City[i] =='Lodi':
# 		print(i)

csv_file['location'] = csv_file.City + ', ' + csv_file.State
print(csv_file.head())