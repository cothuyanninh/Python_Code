import os
import random, time
minh = open('./folder/output.txt', 'r').readlines()
for i in range(len(minh)):
	print("Comment video : "+ str(i))
	os.system('comment.py --videoid "%s" --text "Great Video You can see more video about Matchstick Art at my channel"'%(minh[i].split('\n')[0]))
	time.sleep(random.randint(30, 60))