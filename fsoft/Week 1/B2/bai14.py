string_word = input("Type: ")
list_result = list(set(string_word.split(" ")))
list_result.sort()
print(list_result)