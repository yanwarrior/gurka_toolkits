from unittest import TestCase
import unittest
from gurka import toolkits


class TestAutonumber(TestCase):
	def test_auto_number(self):
		toolkits.DEFAULT_PREFIX = 'PRD'
		toolkits.DEFAULT_OVERFLOW = 4

		result = toolkits.autonumber()
		expected = "PRD0001"
		self.assertEqual(expected, result)

		result = toolkits.autonumber(data=expected)
		expected = "PRD0002"
		self.assertEqual(expected, result)

		result = toolkits.autonumber(data="PRD0234")
		expected = "PRD0235"
		self.assertEqual(expected, result)

if __name__ == '__main__':
	unittest.main()