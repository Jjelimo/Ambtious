import unittest
from prime_numbers import primechecker
class testresults(unittest.TestCase):
	def test_numbers_generated_are_prime_numbers(self):
		self.assert True( primechecker(10), 3)
	def test_number_is_prime_number(self):
	    self.assert True (primechecker(10),0)
	def test_number_is_prime_number(self):
		self.assert True (primechecker(1000),8)
	def test_number_is_prime_number (self):
        self.assert True (primechecker(-100),-8)
        