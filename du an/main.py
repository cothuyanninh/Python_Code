from getDataFromFireBase import *
from logic import *
import os
import datetime

time_each_page =2

def writeData():

	with open('hihi.txt', 'w') as minh:
		raw_data = getToFirebase()
		minh.write(str(raw_data))
	return raw_data


def timeEachData(raw_data):
	
	return 10*int(raw_data["numberOfPrint"])*int(time_each_page)

def creatQueue(raw_data):

	list_key = list(raw_data.keys())
	stack_file_before = []
	for i in range(len(list_key)):
		a = timeEachData(raw_data[list_key[i]])
		stack_file_before.append((list_key[i], a))

	return stack_file_before


def QueueProcess(stack_file_before):

	timeFinishEachID = []
	temp = 0
	for i in range(len(stack_file_before)):
		temp += stack_file_before[i][1]
		temp_hihi = datetime.timedelta(seconds = temp)
		temp_haha  = temp_hihi + 
		timeFinishEachID.append((stack_file_before[i][0], temp_hihi))

	return timeFinishEachID
# print(writeData)
aminh = QueueProcess(creatQueue(writeData()))
print(aminh)
