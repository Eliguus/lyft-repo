import unittest


from refactor.capulet_engine import capulet
from refactor.engine import engine

class test_capulet(unittest.TestCase):
    def test_needs_service_true(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = capulet(last_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_mileage = 1000000000
        current_mileage = 2000000000
        attery = capulet(last_mileage, current_mileage)
        self.assertFalse(engine.needs_service())