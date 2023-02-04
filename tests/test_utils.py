import unittest
from expresso.utils import hash_block

class TestUtils(unittest.TestCase):
    def test_hash_block(self):
        block = {
            'index': 1,
            'timestamp': '2022-12-25 12:00:00',
            'data': 'Test data',
            'previous_hash': '0'
        }
        expected_hash = '3a1d7e13b6d2e0aadfceb935f07b94dbd05a75a7a92ea2b0c7be1d68b16c7eb9'
        
        self.assertEqual(hash_block(block), expected_hash)

if __name__ == '__main__':
    unittest.main()