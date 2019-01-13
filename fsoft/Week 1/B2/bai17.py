string_word = input("Type: ")
list_result = list(set(string_word.replace(" ","").split(",")))
list_result.sort()
print(list_result)