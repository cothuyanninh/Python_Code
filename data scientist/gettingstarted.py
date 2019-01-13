import pandas as pd 
user_cols = ['user_id', 'ages', 'sex' , 'position', 'zip_code']
table = pd.read_table("http://bit.ly/movieusers", sep = '|', header= None, names = user_cols)
print(table)
