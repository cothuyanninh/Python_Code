tuple_exapmle = (2,0,1,8,6,4,9,5,9,9,3,8,7)
a = [str(x) for x in tuple_exapmle if x%2 == 0]
print(tuple(a))