import unittest
import reusable_arithmetic

class test_reusable_arithmetic_library(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(4, reusable_arithmetic.add(2, 2))
		self.assertEqual(4.0, reusable_arithmetic.add(2.0, 2.0))
		self.assertEqual(None, reusable_arithmetic.add(2, 'Ada'))
		self.assertEqual(None, reusable_arithmetic.add('Ada', 'Grace'))
		self.assertEqual(None, reusable_arithmetic.add(2, 'Grace'))	
		self.assertEqual(None, reusable_arithmetic.add(True, 2))
		self.assertEqual(None, reusable_arithmetic.add(False, 2))
		self.assertEqual(None, reusable_arithmetic.add(2, True))
		self.assertEqual(None, reusable_arithmetic.add(2, False))
		
	def test_subtraction(self):	
		self.assertEqual(0, reusable_arithmetic.subtract(2, 2))
		self.assertEqual(0, reusable_arithmetic.subtract(2.0, 2.0))
		self.assertEqual(2, reusable_arithmetic.subtract(2, 0))
		self.assertEqual(-2.0, reusable_arithmetic.subtract(0.0, 2.0))
		self.assertEqual(None, reusable_arithmetic.subtract(2, 'Ada'))
		self.assertEqual(None, reusable_arithmetic.subtract('Ada', 'Grace'))
		self.assertEqual(None, reusable_arithmetic.subtract(2, 'Grace'))	
		self.assertEqual(None, reusable_arithmetic.add(True, 2))
		self.assertEqual(None, reusable_arithmetic.subtract(False, 2))
		self.assertEqual(None, reusable_arithmetic.subtract(2, True))
		self.assertEqual(None, reusable_arithmetic.subtract(2, False))	

	def test_multiply(self):
		self.assertEqual(4, reusable_arithmetic.multiply(2, 2))
		self.assertEqual(4.0, reusable_arithmetic.multiply(2.0, 2.0))
		self.assertEqual(-4.0, reusable_arithmetic.multiply(-2.0, 2.0))
		self.assertEqual(-4.0, reusable_arithmetic.multiply(2.0, -2.0))
		self.assertEqual(None, reusable_arithmetic.multiply(2, 'Ada'))
		self.assertEqual(None, reusable_arithmetic.multiply('Ada', 'Grace'))
		self.assertEqual(None, reusable_arithmetic.multiply(2, 'Grace'))	
		self.assertEqual(None, reusable_arithmetic.multiply(True, 2))
		self.assertEqual(None, reusable_arithmetic.multiply(False, 2))
		self.assertEqual(None, reusable_arithmetic.multiply(2, True))
		self.assertEqual(None, reusable_arithmetic.multiply(2, False))
	
	def test_divide(self):
		self.assertEqual(1, reusable_arithmetic.divide(2, 2))
		self.assertEqual(1.0, reusable_arithmetic.divide(2.0, 2.0))
		self.assertEqual(-1.0, reusable_arithmetic.divide(-2.0, 2.0))
		self.assertEqual(-1.0, reusable_arithmetic.divide(2.0, -2.0))
		self.assertEqual(None, reusable_arithmetic.divide(2, 0))
		self.assertEqual(None, reusable_arithmetic.divide(2, 'Ada'))
		self.assertEqual(None, reusable_arithmetic.divide('Ada', 'Grace'))
		self.assertEqual(None, reusable_arithmetic.divide(2, 'Grace'))	
		self.assertEqual(None, reusable_arithmetic.divide(True, 2))
		self.assertEqual(None, reusable_arithmetic.divide(False, 2))
		self.assertEqual(None, reusable_arithmetic.divide(2, True))
		self.assertEqual(None, reusable_arithmetic.divide(2, False))
	
	def test_square_root(self):
		self.assertEqual(2, reusable_arithmetic.square_root(4))
		self.assertEqual(2.0, reusable_arithmetic.square_root(4.0))		
		self.assertEqual(None, reusable_arithmetic.square_root('Ada'))
		self.assertEqual(None, reusable_arithmetic.square_root(-4))
		self.assertEqual(None, reusable_arithmetic.square_root(True))
		self.assertEqual(None, reusable_arithmetic.square_root(False))
	
	def test_exponent(self):
		self.assertEqual(4, reusable_arithmetic.exponent(2,2))
		self.assertEqual(4.0, reusable_arithmetic.exponent(2.0, 2))	
		self.assertEqual(None, reusable_arithmetic.exponent('Ada', 2))
		self.assertEqual(None, reusable_arithmetic.exponent(2.0, 'Grace'))
		self.assertEqual(None, reusable_arithmetic.exponent(True, 2))
		self.assertEqual(None, reusable_arithmetic.exponent(2.0, False))			
	
	def test_convert2Octal(self):
		self.assertEqual('0o11', reusable_arithmetic,convert2Octal(9))
		self.assertEqual('0o17', reusable_arithmetic. convert2Octal('0xF'))
		selt.assertEqual('0o17', reusable_arithmetic.convert2Octal('0b1111'))
	
	def test_convert2Hex(self):
		self.assertEqual(0xf, reusable_arithmetic.convert2Hex(15))
		self.assertEqual(0xf, reusable_arithmetic.convert2Hex('0o17'))
		self.assertEqual(0xf, reusable_arithmetic.convert2Hex('0b1111'))
	
	def test_convert2Integer(self):
		self.assertEqual(1, reusable_arithmetic.convert2Integer(1.0))
		self.assertEqual(15, reusable_arithmetic.convert2Integer(0xF))
		self.assertEqual(3, reusable_arithmetic.convert2Integer('0b11'))
		self.assertEqual(9, reusable_arithmetic.convert2Integer('0o11'))
	
	def test_convert2Binary(self):
		self.assertEqual('0b11', reusable_arithmetic.convert2Binary(3))
		self.assertEqual('0b1111', reusable_arithmetic.convert2Binary(0xF))
		self.assertEqual('0b1111', reusable_arithmetic.convert2Binary('0o17'))
		
if __name__ == '__main__':
	unittest.main()
	
	
