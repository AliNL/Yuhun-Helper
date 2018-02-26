import unittest

from src.shishen import Shishen
from src.yuhun import Yuhun


class ShishenTest(unittest.TestCase):
    def test_attribute_caculation_1(self):
        shishen = Shishen('彼岸花', {'A': 3002, 'H': 11393, 'D': 388, 'CR': 0.08, 'CA': 1.5,
                                  'HR': 0, 'DR': 0, 'S': 107})
        shishen.set_yuhun_list([Yuhun('阴摩罗', 1, {'A': 486, 'AP': 0.1, 'HP': 0.5, 'D': 30, 'DR': 0.3, 'S': 10})])
        self.assertEqual(shishen.final_attributes, {'A': 3788.2, 'H': 17089.5, 'D': 418, 'CR': 0.08, 'CA': 1.5,
                                                    'HR': 0, 'DR': 0.3, 'S': 117})

    def test_attribute_caculation_2(self):
        shishen = Shishen('彼岸花', {'A': 3002, 'H': 11393, 'D': 388, 'CR': 0.08, 'CA': 1.5,
                                  'HR': 0, 'DR': 0, 'S': 107})
        shishen.set_yuhun_list([Yuhun('阴摩罗', 1, {'A': 486, 'HP': 0.5, 'D': 30, 'DR': 0.3, 'S': 10}),
                                Yuhun('阴摩罗', 1, {'S': 10})])
        self.assertEqual(shishen.final_attributes, {'A': 3938.3, 'H': 17089.5, 'D': 418, 'CR': 0.08, 'CA': 1.5,
                                                    'HR': 0, 'DR': 0.3, 'S': 127})


if __name__ == '__main__':
    unittest.main()
