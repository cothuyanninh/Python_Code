tuple_exapmle = (2,0,1,8,6,4,9,5,9,9,3,8,7)
even_tuple = tuple([int(x) for x in tuple_exapmle if x%2 == 0])
print(even_tuple)
square_tuple = {int(i):int(i)**2 for i in even_tuple}
print(square_tuple)
