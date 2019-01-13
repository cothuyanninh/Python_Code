def binary_search(list_src, number):
    lower = 0
    upper = len(list_src)
    while lower < upper: 
        mid = lower + (upper - lower) // 2
        temp = list_src[mid]
        if number == temp:
            return mid
        elif number > temp:
            if lower == mid:   
                print("-1")
                break 
            lower = mid
        elif number < temp:
            upper = mid

# list_input = intput("").split(",")
# list_input.sort()
number_ = int(input("Number: "))
input_list = [2, 4, 6, 8, 10, 12, 15, 17, 19, 20]
print(binary_search(input_list, number_))