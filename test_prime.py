

# importing unit test library
import unittest
from prime import is_prime

class PrimeTestCase(unittest.TestCase):
	
	def test_is_five_prime(self):
		"""
			Test to check if 5 is prime number
		"""
		self.assertTrue(is_prime(5))
		
	def test_is_four_nonprime(self):
		"""
		Test to check if 4 is non prime number
		"""
		self.assertFalse(is_prime(4))
		
	def test_is_zero_nonprime(self):
		"""
		Test to check if 0 is non prime number
		"""
		self.assertFalse(is_prime(0))
	
	def test_negative_number(self):
		"""
		Test to check all negative numbers are non prime
		"""
		for index in range(-1,-10,-1):
			self.assertFalse(is_prime(index), msg='{} created problem'.format(index))
		
	
if __name__=='__main__':
	unittest.main()
