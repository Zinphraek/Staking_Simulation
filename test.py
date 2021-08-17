import unittest
from functions import get_initial_pack


class FunctionTestCase(unittest.TestCase):
    """Does my functions work?"""

    def test_function_1(self):
        """testing"""
        pack_initial = get_initial_pack(5)
        self.assertEqual(pack_initial, 'pack_05')


if __name__ == '__main__':
    unittest.main()
