import math
list_odd_1000_2000 = [i for i in range(1000,1201) if i%2 == 1]
print(list_odd_1000_2000)

print(" ".join(str(i) for i in list_odd_1000_2000 if ( math.sqrt(i) - int(math.sqrt(i)) ) == 0 ))
