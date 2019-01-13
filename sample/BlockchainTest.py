import hashlib as hasher
import datetime as date

class Block:

	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):

		sha = hasher.sha256()
		sha.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.previous_hash).encode())
		return sha.hexdigest()

def creat_genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
	this_index = last_block.index +1
	this_timestamp = date.datetime.now()
	this_data = "Hey! I am block " + str(this_index)
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [creat_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

	print("Block %s has been added to the blockchain" %(block_to_add.index))
	print("Hash: %s\n" %(block_to_add.hash))
print(blockchain)
