import string
import random
_number = string.digits
_spcharector = "!@#$%^&*"
_lowercase = string.ascii_lowercase
_uppercase = string.ascii_uppercase

password = []
for i in range(2):
	password.append(random.choice(_spcharector))
	password.append(random.choice(_number))
	password.append(random.choice(_lowercase))
	password.append(random.choice(_uppercase))

password.append(random.choice(_lowercase))
password.append(random.choice(_uppercase))

random.shuffle(password)
print("".join(password))
