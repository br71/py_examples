from two_sum import Solution
import unittest.test.test_program


class TestProgram(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().two_sum(([3,5,-4,8,11,1,-1,6],10), [-1, 11]))

    def test_2(self):
        self.assertEqual(Solution().two_sum([3,5,-4,8,11,1,-1,6,1,5,-9,-4,-6.6,8],19), [8, 11])

    def test_3(self):
        self.assertEqual(Solution().two_sum_brute([3,5,-4,8,11,1,-1,6],10), [11, -1])

    def test_4(self):
        self.assertEqual(Solution().two_sum_brute([3,5,-4,8,11,1,-1,6,1,5,-9,-4,-6.6,8],19), [8, 11])

    def test_5(self):
        self.assertEqual(Solution().two_sum_bict([3,5,-4,8,11,1,-1,6],10), [11,-1])

    def test_6(self):
        self.assertEqual(Solution().two_sum_dict([3,5,-4,8,11,1,-1,6,1,5,-9,-4,-6.6,8],19), [8, 11])


if __name__ == "__main__":
    unittest.main()

