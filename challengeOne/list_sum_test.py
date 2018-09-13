import unittest
from list_sum import sum_list, list2


class TestList_Sum(unittest.TestCase):
    def test_list_type(self):
        self.assertIsInstance(list2, list)
    
    def test_sum_list(self):
        self.assertEqual(sum_list(list2), 10)
    
    def test_list_values(self):
        self.assertIsInstance(list2[0], int)
        self.assertIsInstance(list2[2][0], int)
        self.assertIsInstance(list2[2], list)
