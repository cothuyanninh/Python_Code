import math
list_result_number = [i**2 for i in range(int(math.sqrt(2030)) +1)]
print(" ".join(str(x) for x in list_result_number))
