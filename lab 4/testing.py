from randomGame import check_guess
import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):

    def test_TooLow(self):
        self.assertEqual(check_guess(4,9),'Too Low, try using larger  numbers ')
        self.assertEqual(check_guess(0,1), 'Too Low, try using larger  numbers ')

    def test_TooHigh(self):
        self.assertEqual(check_guess(8,4),'Too High , try again')
        self.assertEqual(check_guess(9,6), 'Too High , try again')
        self.assertEqual(check_guess(20,11), 'Too High , try again')

    def test_Win(self):
        self.assertEqual(check_guess(11,11),'Well played you got it')
        self.assertEqual(check_guess(2,2), 'Well played you got it')
        self.assertEqual(check_guess(8,8), 'Well played you got it')



