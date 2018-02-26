import unittest

from src.target import Target


class TargetTest(unittest.TestCase):
    def test_init_target(self):
        target = Target({'A': (10000, 1), 'CR': (100, 3)})
        self.assertEqual(target.values_and_weights, {'A': 10000, 'AW': 1, 'H': 0, 'HW': 0, 'D': 0, 'DW': 0,
                                                     'CR': 100, 'CRW': 3, 'CA': 0, 'CAW': 0, 'HR': 0, 'HRW': 0,
                                                     'DR': 0, 'DRW': 0, 'S': 0, 'SW': 0})

    def test_get_cost(self):
        target = Target({'A': (10000, 1), 'CR': (100, 3)})
        cost = target.get_cost({'A': 9999, 'H': 10000, 'CR': 95})
        self.assertEqual(cost, 1 + 75)


if __name__ == '__main__':
    unittest.main()
