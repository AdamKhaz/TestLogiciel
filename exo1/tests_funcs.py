import funcs
import unittest

class TestFuncs(unittest.TestCase):
    def test_max_list(self):
        self.assertEqual(funcs.max_list([0,1,2,3,4,5,6]), (4,5,6))
        self.assertEqual(funcs.max_list([6,5,4,3,2,1,0]),(4,5,6))
        self.assertEqual(funcs.max_list([4,7,34,4,354,654,6532,54]),(354,654,6532))
        self.assertEqual(funcs.max_list([0,2]),None)
        self.assertEqual(funcs.max_list([2]), None)
        self.assertEqual(funcs.max_list([]), None)
        self.assertEqual(funcs.max_list([-7, -14, -9, 1, -2, 0]),(-2,0,1))
        self.assertEqual(funcs.max_list([2,2,2,2,2]), (2,2,2))
        self.assertEqual(funcs.max_list([7,4,3,21,7]), (7,7,21))

    def test_min_list(self):
        self.assertEqual(funcs.min_list([0, 1, 2, 3, 4, 5, 6], 4), [0,1,2,3])
        self.assertEqual(funcs.min_list([6, 5, 4, 3, 2, 1, 0],4), [0,1,2,3])
        self.assertEqual(funcs.min_list([4, 7, 34, 4, 354, 654, 6532, 54],6), [4, 4, 7, 34, 54, 354])
        self.assertEqual(funcs.min_list([0, 2], 3), None)
        self.assertEqual(funcs.min_list([2],-2), None)
        self.assertEqual(funcs.min_list([],1), None)
        self.assertEqual(funcs.min_list([2, 5, -4], 0), None)
        self.assertEqual(funcs.min_list([-7, -14, -9, 1, -2, 0],3), [-14, -9, -7])
        self.assertEqual(funcs.min_list([2, 2, 2, 2, 2], 3), [2, 2, 2])
        self.assertEqual(funcs.min_list([1, 4, 3, 21, 1],4), [1,1,3,4])

    def test_first_number(self):
        self.assertEqual(funcs.first_number(10), False)
        self.assertEqual(funcs.first_number(3), True)
        self.assertEqual(funcs.first_number(1), None)
        self.assertEqual(funcs.first_number(-1), None)
        self.assertEqual(funcs.first_number(-11), None)
        self.assertEqual(funcs.first_number(0), None)

    def test_list_arithm(self):
        self.assertEqual(funcs.list_arithm([1, 3, 5, 7, 9, 11]),True)
        self.assertEqual(funcs.list_arithm([-9, 0, 9, 18, 27, 36]), True)
        self.assertEqual(funcs.list_arithm([1]), False)
        self.assertEqual(funcs.list_arithm([1,2]), True)
        self.assertEqual(funcs.list_arithm([]), False)
        self.assertEqual(funcs.list_arithm([2, 1, 8, 5, 4, 9]), False)
        self.assertEqual(funcs.list_arithm([1, 3, 5, 7, 9, 11, 14]), False)
        self.assertEqual(funcs.list_arithm([1, 3, 5, 7, 8, 11, 13]), False)
        self.assertEqual(funcs.list_arithm([7, 3, -1, -5, -9]), True)
        self.assertEqual(funcs.list_arithm([12, 10, 8, 10, 8, 6]), False)

    def test_list_geom(self):
        self.assertEqual(funcs.list_geom([1, 3, 5, 7, 9, 11]), False)
        self.assertEqual(funcs.list_geom([7, 3, -1, -5, -9]), False)
        self.assertEqual(funcs.list_geom([1]), False)
        self.assertEqual(funcs.list_geom([]), False)
        self.assertEqual(funcs.list_geom([1, 1, 1, 1, 1, 1]), True)
        self.assertEqual(funcs.list_geom([1, 3, 9, 27]), True)
        self.assertEqual(funcs.list_geom([20, 10, 5]), True)
        self.assertEqual(funcs.list_geom([20, 10, 5, 5]), False)
        self.assertEqual(funcs.list_geom([20, 20, 10, 5]), False)
        self.assertEqual(funcs.list_geom([1, -5, 25, -125]), True)
        self.assertEqual(funcs.list_geom([-1, -5, -25, -125]), True)
        self.assertEqual(funcs.list_geom([100, 50, 25, 5]), False)
        self.assertEqual(funcs.list_geom([48, 24, 48, 12]), False)
        self.assertEqual(funcs.list_geom([46, 68, 348, 456]), False)
        
if __name__ == '__main__':
    unittest.main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
