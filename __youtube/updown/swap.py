import os
a = os.listdir()
for i in range(len(a)):
	if a[i].endwith("mp4") == True:
		a[i] = a[i].replace("S13", "Season 13 2018 Episodul")