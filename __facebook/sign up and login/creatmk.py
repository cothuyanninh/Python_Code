import random
a = open('password.txt', 'w')
alp = 'a b c d e f g h i k l m n o p q t u v x y z w 0 1 2 3 4 5 6 7 8 9 @ # $ % ^ & * !'.split(' ')
for i in range(1000):
	name = ''
	for j in range(12):
		name += random.choice(alp)

	a.write(name)
	a.write("\n")
