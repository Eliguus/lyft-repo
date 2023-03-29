import unittest


from refactor.nuin import nuin
from refactor.attery import attery

class test_nuin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = "2020-05-15"
        last_service_date = "2016-01-25"
        attery = nuin(current_date, last_service_date)
        self.assertTrue(attery.needs_service())

    def test_needs_service_false(self):
        current_date = "2020-05-15"
        last_service_date = "2019-01-10"
        attery = nuin(current_date, last_service_date)
        self.assertFalse(attery.needs_service())