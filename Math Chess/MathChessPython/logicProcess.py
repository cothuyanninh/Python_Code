class checkPos():

	def __init__(self, source_point, value_point, type_point,  mang):

		# threading.Thread.__init__(self)
		self.source_point  = source_point
		self.value_point = value_point
		self.type_point = type_point
		self.mang = mang


	def run(self):

		if self.type_point == None:
			return False

		def check_out_of_board_tru(a1, vl1):
			if (a1 - vl1 < 0):
				return 0
			return a1- vl1
		def check_out_of_board_plus(a2, vl2, vl3):
			if (a2 + vl2 >  vl3):
				return vl3
			return a2 +vl2

		# threading.Lock().acquire()
		list_can_move = []
		_x = self.source_point[1]
		_y = self.source_point[0]
		value = self.value_point
		mang = self.mang

		temp_left = check_out_of_board_tru(_x, value)
		temp_right = check_out_of_board_plus(_x, value, 8)
		temp_top = check_out_of_board_tru(_y, value)
		temp_under = check_out_of_board_plus(_y, value, 10)

		#add them nhung phan tu tu ben trai
		if (_x -1 > 0 and mang[_y][_x-1][1] != None):
			if(mang[_y][_x][1] == mang[_y][_x-1][1]):#check xem cung quan hay khong
				h1, h2 = int(mang[_y][_x][0]) , int(mang[_y][_x-1][0])
				tong = (h1 + h2)%10
				hieu = (h1-h2)
				tich = (h1*h2)%10
				if (h2 != 0):
					thuong = h1%h2
				if (_x - tong-1) >= 0:# an bang phep cong
					if (mang[_y][_x-tong-1][1] != None and mang[_y][_x-tong-1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x - tong -1))
				if (hieu > 0 and _x-hieu-1 >= 0): # an bang phep tru
					if (mang[_y][_x-hieu-1][1] != None and mang[_y][_x-hieu-1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x - hieu -1))
				if (_x - tich - 1) >= 0:
					if (mang[_y][_x-tich-1][1] != None and mang[_y][_x-tich-1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x - tich -1))
				if (h2 != 0):
					if (_x - thuong -1 ) >= 0 and thuong != 0:
						if (mang[_y][_x-thuong-1][1] != None and mang[_y][_x-thuong-1][1] != mang[_y][_x][1]):
							list_can_move.append((_y, _x - thuong -1))
		for i in range(_x - 1, temp_left-1, -1):
			if (i< 0):
				break
			if (mang[_y][i][1] == None):
				list_can_move.append((_y, i))
			else:
				break

		#add them tu nhung phan tu tu ben phai
		if (_x+1 < 9 and mang[_y][_x+1][1] != None):
			if(mang[_y][_x][1] == mang[_y][_x+1][1]):
				h1, h2 = int(mang[_y][_x][0]), int(mang[_y][_x+1][0])
				tong = (h1+ h2)%10
				hieu = (h1-h2)
				tich = (h1*h2)%10
				if (h2 != 0):
					thuong = h1%h2
				if (_x + tong +1) < 9:
					if (mang[_y][_x+tong+1][1] != None and mang[_y][_x+tong+1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x + tong +1))
				if (_x + hieu +1 ) < 9 and hieu > 0:
					if (mang[_y][_x+hieu+1][1] != None and mang[_y][_x+hieu+1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x + hieu +1))
				if (_x + tich +1) < 9:
					if (mang[_y][_x+tich+1][1] != None and mang[_y][_x+tich+1][1] != mang[_y][_x][1]):
						list_can_move.append((_y, _x + tich +1))
				if (h2 != 0):
					if (_x + thuong +1 ) < 9 and thuong != 0:
						if (mang[_y][_x+thuong+1][1] != None and mang[_y][_x+thuong+1][1] != mang[_y][_x][1]):
							list_can_move.append((_y, _x + thuong +1))
		for i in range(_x +1, temp_right+1):
			if (mang[_y][i][1] == None):
				list_can_move.append((_y, i))
			else :
				break

		#add them tu nhung phan tu tu tren
		if (_y -1 > 0 and mang[_y-1][_x][1] != None):
			if(mang[_y][_x][1] == mang[_y-1][_x][1]):
				h1, h2 = int(mang[_y][_x][0]), int(mang[_y-1][_x][0])
				tong = (h1 +h2)%10
				hieu = (h1-h2)
				tich = (h1*h2)%10
				if (h2 != 0):
					thuong = h1%h2
				if (_y-1-tong>= 0):
					if (mang[_y-1-tong][_x][1] != None and mang[_y-1-tong][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y-1-tong, _x))
				if (_y-1-hieu>= 0 and hieu >0):
					if (mang[_y-1-hieu][_x][1] != None and mang[_y-1-hieu][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y-1-hieu, _x))
				if (_y-1-tich>= 0):
					if (mang[_y-1-tich][_x][1] != None and mang[_y-1-tich][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y-1-tich, _x))
				if (h2 != 0):
					if (_y-1-thuong>= 0 and thuong != 0):
						if (mang[_y-1-thuong][_x][1] != None and mang[_y-1-thuong][_x][1] != mang[_y][_x][1]):
							list_can_move.append((_y-1-thuong, _x))

		for i in range(_y -1, temp_top-1, -1):
			if (i <0):
				break
			if (mang[i][_x][1] == None):
				list_can_move.append((i, _x))
			else:
				break

		#add them tu nhugn phan tu tu duoi
		if (_y +1 < 9 and mang[_y+1][_x][1] != None):
			if (mang[_y][_x][1] == mang[_y+1][_x][1]):
				h1, h2 = int(mang[_y][_x][0]), int(mang[_y+1][_x][0])
				tong = (h1+ h2)%10
				hieu = (h1-h2)
				tich = (h1*h2)%10
				if (h2 != 0):
					thuong = h1%h2
				if (_y +1 +tong < 9):
					if (mang[_y+1+tong][_x][1] != None and mang[_y+1+tong][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y+1+tong, _x))
				if (_y +1 +hieu < 9 and hieu >0):
					if (mang[_y+1+hieu][_x][1] != None and mang[_y+1+hieu][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y+1+hieu, _x))
				if (_y +1 +tich < 9):
					if (mang[_y+1+tich][_x][1] != None and mang[_y+1+tich][_x][1] != mang[_y][_x][1]):
						list_can_move.append((_y+1+tich, _x))
				if (h2 != 0):
					if (_y +1 +thuong < 9) and thuong != 0:
						if (mang[_y+1+thuong][_x][1] != None and mang[_y+1+thuong][_x][1] != mang[_y][_x][1]):
							list_can_move.append((_y+1+thuong, _x))
		for i in range(_y+1, temp_under+1): 
			if (mang[i][_x][1] == None):
				list_can_move.append((i, _x))
			else:
				break
		return list_can_move

def remove(source, destination, mang):
	x1 = source[0]
	y1 = source[1]
	x2 = destination[0]
	y2 = destination[1]
	mang[x2][y2] = mang[x1][y1]
	mang[x1][y1] = [None, None]
	# return mang
		

# nuoc1 = checkPos((10,2), 3, 'X', grid).run()
# print(nuoc1)
