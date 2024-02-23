"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test the calc module."""
    def test_add_number(self):
        """Test adding number together."""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res= calc.subtract(15,10)
        self.asserEqual(res,5)
