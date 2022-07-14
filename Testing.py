from Class import energy_calculator
import unittest

class TestE1(unittest.TestCase):
    def test_basic(self):
        next_meter_reading_E1 = 50
        last_meter_reading_E1 = 100
        testcase = next_meter_reading_E1, last_meter_reading_E1
        expected = -10.14
        self.assertEqual(energy_calculator.calculate_cost_E1(next_meter_reading_E1, last_meter_reading_E1))

unittest.main()