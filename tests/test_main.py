import unittest
from expresso import main

class TestMain(unittest.TestCase):
    def test_append_to_chain(self):
        # Test that the append_to_chain function adds a new block to the chain
        result = main.append_to_chain("This is a test transaction")
        self.assertEqual(result, "Block added to the chain.")
        
    def test_parse_block(self):
        # Test that the parse_block function returns the block's data
        result = main.parse_block(1)
        self.assertEqual(result, "Block data: This is block 1.")
        
    def test_get_chain(self):
        # Test that the get_chain function returns the full chain
        result = main.get_chain()
        self.assertEqual(result, "Chain: [{'index': 0, 'timestamp': 'timestamp_0', 'data': 'This is block 0.'}, {'index': 1, 'timestamp': 'timestamp_1', 'data': 'This is block 1.'}]")

if __name__ == '__main__':
    unittest.main()