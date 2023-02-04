import unittest
from expresso.parse_block import parse_block

class TestParseBlock(unittest.TestCase):
    def test_parse_block(self):
        # Test valid input
        block_data = {
            'timestamp': '2022-12-30T12:34:56',
            'data': 'Sample data',
            'previous_hash': 'abcdefghijklmnopqrstuvwxyz123456'
        }
        expected_output = (
            '2022-12-30T12:34:56',
            'Sample data',
            'abcdefghijklmnopqrstuvwxyz123456'
        )
        self.assertEqual(parse_block(block_data), expected_output)

        # Test missing timestamp
        block_data = {
            'data': 'Sample data',
            'previous_hash': 'abcdefghijklmnopqrstuvwxyz123456'
        }
        self.assertRaises(ValueError, parse_block, block_data)

        # Test missing data
        block_data = {
            'timestamp': '2022-12-30T12:34:56',
            'previous_hash': 'abcdefghijklmnopqrstuvwxyz123456'
        }
        self.assertRaises(ValueError, parse_block, block_data)

        # Test missing previous_hash
        block_data = {
            'timestamp': '2022-12-30T12:34:56',
            'data': 'Sample data'
        }
        self.assertRaises(ValueError, parse_block, block_data)

if __name__ == '__main__':
    unittest.main()