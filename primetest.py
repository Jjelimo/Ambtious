import unittest
from prime_numbers import primechecker
class testresults(unittest.TestCase):
	def test_numbers_generated_are_prime_numbers(self):
		'''To test the code if 2 is a prime number or not'''
		self.assert True( primechecker(100),2)
	def test_number_is_prime_number(self):
		'''To test if 0 is a prime number or not'''
	    self.assert True (primechecker(10),0)
	def test_number_is_prime_number(self):
		'''To test a random number from the list'''
		self.assert True (primechecker(1000),867)
	def test_number_is_prime_number (self):
		'''To test the negative number'''
        self.assert True (primechecker(-100),-10)


        