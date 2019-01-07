import os
import random, time
minh = open('./folder/output.txt', 'r').readlines()
for i in range(len(minh)):
	print("Like video : "+ str(i))
	os.system('like.py --videoid "%s"'%(minh[i].split('\n')[0]))
	time.sleep(random.randint(30, 60))