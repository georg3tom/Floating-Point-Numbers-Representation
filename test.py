import unittest
from app.user.exp import IEEE754,float_bin,decimal_converter
from app.user.models import quizcheck,Quiz
class TestExperiment(unittest.TestCase):
    def test_ieee(self):
        x={'status': 'pass', 'sign': 0, 'exponent': 129, 'exponent_bits': '10000001', 'mantissa': '01100000000000000000000', 'final': '01000000101100000000000000000000'}
        self.assertEqual(IEEE754(5.5), x)
        x={'status': 'pass', 'sign': 1, 'exponent': 136, 'exponent_bits': '10001000', 'mantissa': '10010110000111011001100', 'final': '11000100010010110000111011001100'}
        self.assertEqual(IEEE754(-812.22),x)
        x={'status': 'pass', 'sign': 0, 'exponent': 135, 'exponent_bits': '10000111', 'mantissa': '10111001011001100110011', 'final': '01000011110111001011001100110011'}
        self.assertEqual(IEEE754(441.4),x)
    def test_quiz(self):
        self.assertSequenceEqual(quizcheck([2,4,3,2],[1,2,3,4]),"1001")
        self.assertSequenceEqual(quizcheck([3,3,1,2],[5,6,7,8]),"1111")
        self.assertSequenceEqual(quizcheck([1,2,2,1],[5,6,7,8]),"0000")


if __name__ == '__main__':
    unittest.main()
