import re

var_search = re.compile(r'\d+\s\w+')
result = var_search.findall('12 bananas , 11 apple , 10 nhan , 9 buoi')
print(result)