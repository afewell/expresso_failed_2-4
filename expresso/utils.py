import hashlib
import json

def hash_block(block):
    """
    Hashes a block and returns a string representation of it.
    """
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def validate_block(block, previous_hash):
    """
    Validates the block by checking if the previous_hash stored in the block
    matches the hash of the previous block, and if the current hash of the block
    is correct.
    """
    if block['previous_hash'] != previous_hash:
        return False
    if hash_block(block) != block['hash']:
        return False
    return True

def create_genesis_block():
    """
    Creates the first block in the chain and returns it.
    """
    return {
        'previous_hash': '0',
        'index': 0,
        'data': [],
        'hash': hash_block({
            'previous_hash': '0',
            'index': 0,
            'data': []
        })
    }

def format_block(index, previous_hash, data):
    """
    Formats a block for appending to the blockchain by creating a dictionary
    with the required keys, and calculates the hash of the block.
    """
    block = {
        'index': index,
        'previous_hash': previous_hash,
        'data': data,
        'hash': hash_block({
            'index': index,
            'previous_hash': previous_hash,
            'data': data
        })
    }
    return block