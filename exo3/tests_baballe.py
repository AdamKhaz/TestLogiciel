import unittest
from unittest.mock import MagicMock
from tkinter import Event
from baballe import AppliBaballe

class TestAppliBaballe(unittest.TestCase):
    def setUp(self):
        self.app = AppliBaballe()

    def test_initial_position(self):
        self.assertEqual(self.app.x, 220)
        self.assertEqual(self.app.y, 220)

    def test_initial_size(self):
        self.assertEqual(self.app.size, 50)

    def test_initial_direction(self):
        self.assertIn(self.app.dx, [-20, 20])
        self.assertIn(self.app.dy, [-20, 20])

    def test_incr(self):
        initial_size = self.app.size
        self.app.incr(Event())
        self.assertEqual(self.app.size, min(initial_size + 10, 200))

    def test_decr(self):
        initial_size = self.app.size
        self.app.decr(Event())
        self.assertEqual(self.app.size, max(initial_size - 10, 10))

    def test_boom(self):
        initial_x, initial_y = self.app.x, self.app.y
        event = MagicMock(x=50, y=75)
        self.app.boom(event)
        self.assertEqual(self.app.x, event.x)
        self.assertEqual(self.app.y, event.y)
        self.assertNotEqual(self.app.dx, 0)
        self.assertNotEqual(self.app.dy, 0)

if __name__ == '__main__':
    unittest.main()
