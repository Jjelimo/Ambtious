import unittest
from prime_numbers import primecreator
class testresults(unittest.TestCase):
	def test_numbers_generated_are_prime_numbers(self):
		self.assertTrue( primecreator(10), 3)
	def test_number_is_prime_number(self):
	    self.assertTrue (primecreator(10),0)
	def test_number_is_prime_number(self):
		self.assert True (primecreator(1000),8)
	def test_number_is_prime_number (self):
        self.assert True (primecreator(-100),-8)
        