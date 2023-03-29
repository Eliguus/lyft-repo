import unittest


from refactor.willough import willough
from refactor.engine import engine

class test_willough(unittest.TestCase):
    def test_needs_service_true(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = willough(last_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = willough(last_mileage, current_mileage)
        self.assertFalse(engine.needs_service())