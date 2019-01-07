def verify_account():
	list_email = open("email.txt", 'r').readlines()
	for i in range(len(list_email)):
		list_email[i] = list_email[i][:-2]
		list_email[i] = list_email[i].split('\t')
	print(list_email) 
verify_account()