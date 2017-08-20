from unittest import TestCase
import unittest
from gurka import toolkits

class TestRupiah(TestCase):
	def test_to_rupiah(self):
		expected = 'Rp. 45,000.00'
		number = 45000
		result = toolkits.to_rupiah(number)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	unittest.main()