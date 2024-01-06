import exo2
import unittest

class TestFuncs(unittest.TestCase):
    def test_fifo(self):
        list1 = [1, 2, 3, 4, 5]
        fifo1 = exo2.FIFO()
        for i in list1:
            fifo1.push(i)
        self.assertEqual(list1, fifo1.fifo)
        for i in list1:
            self.assertEqual(i, fifo1.pop())
        self.assertEqual(None, fifo1.pop())

        fifo2 = exo2.FIFO(list1)
        self.assertEqual(list1, fifo2.fifo)
        self.assertEqual(1, fifo2.pop())
        self.assertEqual([2, 3, 4, 5], fifo2.fifo)

    
    def test_lifo(self):
        list1 = [1, 2, 3, 4, 5]
        lifo1 = exo2.LIFO()
        for i in list1:
            lifo1.push(i)
        self.assertEqual(list1, lifo1.lifo)
        for i in list1[::-1]:
            self.assertEqual(i, lifo1.pop())
        self.assertEqual(None, lifo1.pop())
        lifo2 = exo2.LIFO(1, 2, 3, 4, 5)
        self.assertEqual(list1, lifo2.lifo)
        self.assertEqual(5, lifo2.pop())
        self.assertEqual([1, 2, 3, 4], lifo2.lifo)

    def test_lilo(self):
        list1 = [1, 2, 3, 4, 5]
        lilo1 = exo2.LILO()
        for i in list1:
            lilo1.push(i)
        self.assertEqual(list1, lilo1.lilo)
        for i in list1:
            self.assertEqual(i, lilo1.pop())
        self.assertEqual(None, lilo1.pop())
        lilo2 = exo2.LILO(1, 2, 3, 4, 5)
        self.assertEqual(list1, lilo2.lilo)
        self.assertEqual(1, lilo2.pop())
        self.assertEqual([2,3,4,5], lilo2.lilo)

if __name__ == '__main__':
    unittest.main()
