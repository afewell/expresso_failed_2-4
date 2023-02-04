import unittest
from expresso.append_to_chain import append_to_chain

class TestAppendToChain(unittest.TestCase):
    def test_append_to_chain(self):
        block_chain = []
        new_block = {
            'index': 1,
            'timestamp': '2022-07-28 12:00:00',
            'data': 'This is block 1',
            'previous_hash': '0'
        }
        append_to_chain(block_chain, new_block)
        self.assertEqual(len(block_chain), 1)
        self.assertEqual(block_chain[0], new_block)
        
    def test_append_to_chain_with_multiple_blocks(self):
        block_chain = []
        new_block_1 = {
            'index': 1,
            'timestamp': '2022-07-28 12:00:00',
            'data': 'This is block 1',
            'previous_hash': '0'
        }
        new_block_2 = {
            'index': 2,
            'timestamp': '2022-07-28 12:05:00',
            'data': 'This is block 2',
            'previous_hash': 'd3b07384d113edec49eaa6238ad5ff00'
        }
        append_to_chain(block_chain, new_block_1)
        append_to_chain(block_chain, new_block_2)
        self.assertEqual(len(block_chain), 2)
        self.assertEqual(block_chain[0], new_block_1)
        self.assertEqual(block_chain[1], new_block_2)
        
if __name__ == '__main__':
    unittest.main()