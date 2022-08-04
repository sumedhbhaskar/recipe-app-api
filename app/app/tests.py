"""
sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_num(self):
        """add num test"""
        res=calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract_num(self):
        """subtract number test"""
        res= calc.sub(15,10)
        self.assertEqual(res,5)