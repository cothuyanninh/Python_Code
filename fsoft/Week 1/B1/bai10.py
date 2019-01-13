def insertion_Sort(list_temp):
   for i in range(1,len(list_temp)):

     temp = list_temp[i]
     id_ = i

     while id_>0 and list_temp[id_-1]>temp:
         list_temp[id_]=list_temp[id_-1]
         id_ = id_-1

     list_temp[id_]=temp

list_temp = [20,18,45,25,23,4,8,3,19,16]
insertion_Sort(list_temp)
print(list_temp)
