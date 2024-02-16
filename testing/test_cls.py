import unittest
from cls import Calc

class CalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Setup')
        a = 4
        b = 2
        cls.c = Calc(a, b)

    def test_sumx(self):
        print('test sum')
        expected_result = 6
        actual_result = self.c.sumx()
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        print('test divide')
        expected_result = 2
        actual_result = self.c.divide()
        self.assertEqual(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear down')
        del cls.c



if __name__ == '__main__':
    unittest.main()