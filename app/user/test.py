import flask
import unittest
import exp
class TestExperiment(unittest.TestCase):

    def test_ieee(self):
        self.assertEqual(exp.IEEE754(5.5)['final'], '01000000101100000000000000000000')
        self.assertEqual(exp.IEEE754(2.54)['final'], '01000000101100000000000000000000')

if __name__ == '__main__':
    unittest.main()