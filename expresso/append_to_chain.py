import hashlib

class Block:
    def __init__(self, data, previous_block_hash):
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.hash = self._get_hash()

    def _get_hash(self):
        block_string = f"{self.data}{self.previous_block_hash}".encode()
        return hashlib.sha256(block_string).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = [self._get_genesis_block()]

    def _get_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(data, previous_block_hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block._get_hash():
                return False
            if current_block.previous_block_hash != previous_block.hash:
                return False
        return True

blockchain = BlockChain()
blockchain.add_block("Data for Block 1")
blockchain.add_block("Data for Block 2")

print(blockchain.chain)
print(blockchain.is_valid())