with open("someFile.txt", "r").readlines() as fb:
	print("\n".join(str(x) for x in fb))
	print("Number of line: ", len(fb))