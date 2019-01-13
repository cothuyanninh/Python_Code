import random
import logicProcess
from boardPos import *

def random_run(grid):

	mang = []
	list_come = []

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (grid[i][j][1] == 'Y'):
				mang.append([(i,j), grid[i][j]])

	while (len(list_come) == 0):
		result = []
		random_choice = random.choice(mang)
		result.append(random_choice[0])
		list_come = logicProcess.checkPos(random_choice[0], random_choice[1][0], random_choice[1][1], grid).run()
		if (len(list_come) != 0):
			ahihi = random.choice(list_come)
			result.append(ahihi)

	return result

def find_chess(grid):

	list_X = []
	list_Y = []
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j][1] == 'X':
				list_X.append(int(grid[i][j][0]))
			if grid[i][j][1] == 'Y':
				list_Y.append(int(grid[i][j][0]))
	list_X.sort()
	list_Y.sort()
	return (list_X, list_Y)


def evolution(grid):
	listX , listY = find_chess(grid)
	# listX , listY = ((0,5,7,2),(0,7,1,4))
	# vector don vi
	a = [1000,23,21,23,21,21,21,23,20,23]
	b = [1000,23,21,23,21,21,21,23,20,23]
	#vector ketqua
	c = [0,0,0,0,0,0,0,0,0,0]
	d = [0,0,0,0,0,0,0,0,0,0]
	for i in range(len(listX)):
		c[listX[i]] = a[listX[i]]
	for i in range(len(listY)):
		d[listY[i]] = b[listY[i]]
	
	return sum(d) - sum(c)

def copy_grid(grid):
	b= []
	for i in range(len(grid)):
		b.append([])
		for j in range(len(grid[i])):
			b[i].append(grid[i][j])
	return b

def remove_point(source, destination, mang):
	x1 = int(source[0][0])
	y1 = int(source[0][1])
	x2 = destination[0]
	y2 = destination[1]
	mang[x2][y2] = mang[x1][y1]
	mang[x1][y1] = [None, None]
	# return mang


def check_nuoc_sau(may_choi, grid, flag):
	max_value = 0
	min_value = 0
	# grid2 = grid
	list_cac_node_to = []
	list_cac_node_be = []
	max_temp = 0
	min_temp = -1
	for i in range(len(may_choi)): #len(may_choi)
		list_all_from_each_node = logicProcess.checkPos(may_choi[i][0], may_choi[i][1][0], may_choi[i][1][1],grid).run()
	# print(list_all_from_each_node)
		if (len(list_all_from_each_node) != 0):
			for j in range(len(list_all_from_each_node)):
				grid1 = copy_grid(grid)
				remove_point(may_choi[i] , list_all_from_each_node[j], grid1)
				if (flag == 'Y'):
					max_temp = evolution(grid1)
					min_temp = evolution(grid1)
				if (flag == 'X'):
					max_temp = evolution(grid1)*(-1)
					min_temp = evolution(grid1)*(-1)
				if (max_temp == max_value):
					list_cac_node_to.append((may_choi[i][0], list_all_from_each_node[j]))
				if (max_temp > max_value):
					list_cac_node_to = []
					list_cac_node_to.append((may_choi[i][0],  list_all_from_each_node[j]))
					max_value = max_temp
				if (min_temp == min_value):
					list_cac_node_be.append((may_choi[i][0], list_all_from_each_node[j]))
				if (min_temp < min_value):
					min_value = min_temp
					list_cac_node_be = []
					list_cac_node_be.append((may_choi[i][0], list_all_from_each_node[j]))
	print("Max is: "+ str(max_value))
	print("Min is: "+ str(min_value))
	# print("Bang nhau: "+ str(list_cac_node_to))	
	return (list_cac_node_to, list_cac_node_be)

def check_all_node(grid):
	nguoi_choi = []
	may_choi = []

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (grid[i][j][1] == 'Y'):
				may_choi.append([(i,j), grid[i][j]])
			if (grid[i][j][1] == 'X'):
				nguoi_choi.append([(i,j), grid[i][j]])
	print("May choi:")
	check_quan_minh = check_nuoc_sau(may_choi, grid, 'Y')[0]
	print("***************")
	print("Nguoi choi:")
	check_quan_dich = check_nuoc_sau(nguoi_choi, grid, 'X')[0]
	for i in range(len(check_quan_dich)):
		if check_quan_dich[i] in check_quan_minh:
			check_quan_minh.remove(check_quan_dich[i])
	print("-------------------------")
	return random.choice(check_quan_minh)



# check_all_node(grid)
# print(check_all_node(grid))

