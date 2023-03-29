import unittest


from refactor.sternman import sternman
from refactor.engine import engine

class test_sternman(unittest.TestCase):
    def test_needs_service_true(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = sternman(last_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = sternman(last_mileage, current_mileage)
        self.assertFalse(engine.needs_service())