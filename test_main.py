import unittest
from main import minEatingSpeed

class test_main(unittest.TestCase):
    def setUp(self):
        self.first_test_list = ([3, 6, 7, 11])
        self.first_test_hour = 8
        self.second_test_list = ([30, 11, 23, 4, 20])
        self.second_test_hour = 5
        self.third_test_list = ([30, 11, 23, 4, 20])
        self.third_test_hour = 6
        self.first_result = 4
        self.second_result = 30
        self.third_result = 23

    def test_first(self):
        self.assertEqual(minEatingSpeed(self.first_test_list,self.first_test_hour), self.first_result)

    def test_second(self):
        self.assertEqual(minEatingSpeed(self.second_test_list,self.second_test_hour), self.second_result)

    def test_third(self):
        self.assertEqual(minEatingSpeed(self.third_test_list,self.third_test_hour), self.third_result)

if __name__ == '__main__':
    unittest.main( )