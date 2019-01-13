ip_src = input("Type: ").split(".")
ip_new_list = [int(i) for i in ip_src]
print(ip_new_list)
# print("."join(str(i) for i in ip_new_list))
result = ""
for i in ip_new_list:
	result += str(i)
	result += "."
print(result[:-1])