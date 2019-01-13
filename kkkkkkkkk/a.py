import pyshark
filename='sampledata.pcap'
print("loading")
cap = pyshark.FileCapture(filename)

print(cap)
def countPacket():
	cap.load_packets()
	return len(cap)

def findFile():
	sess_index = [] # to save stream indexes in an array
	for pkt in cap:
		try:
			sess_index.append(pkt.tcp.stream)
		except:
			pass
	print (sess_index)
	if len(sess_index) == 0:
		max_index = 0
		print ("No TCP Found")
	else:
		max_index = int(max(sess_index)) + 1 # max function is used to get the highiest number

	for session in range(0,max_index):
		for pkt in cap:
			try:
				if int(pkt.tcp.stream) == session:
					if pkt.http > 0:
						print("Stream Index :",pkt.tcp.stream) # to print stream index at the start
					print ("HTTP LAYER :",str(pkt.http).replace('\\n','').replace('\\r', ''))
			except:
				pass

