from BinarySearch import Solution
import BinarySearch
import unittest.test.test_program

class TestProgram(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(BinarySearch.binarySearchRecurse([0,1,21,33,45,45,61,71,72,73],33),3)

    def test_1_2(self):
        self.assertEqual(BinarySearch.binarySearchRecurse([0,1,21,33,45,45,61,71,72,73],72),8)

    def test_1_3(self):
        self.assertEqual(BinarySearch.binarySearchRecurse([0,1,21,33,45,45,61,71,72,73,355],355),10)

    def test_1_4(self):
        self.assertEqual(BinarySearch.binarySearchRecurse([0,1,21,33,45,45,61,71,72,73,355],354),-1)

    def test_1_5(self):
        self.assertEqual(BinarySearch.binarySearchRecurse([0,1,21,33,45,45,61,71,72,73],70),-1)


    
    def test_2_1(self):
        self.assertEqual(Solution().binarySearchIterate([0,1,21,33,45,45,61,71,72,73],33),3)

    def test_2_2(self):
        self.assertEqual(Solution().binarySearchIterate([0,1,21,33,45,45,61,71,72,73],72),8)

    def test_2_3(self):
        self.assertEqual(Solution().binarySearchIterate([0,1,21,33,45,45,61,71,72,73,355],355),10)

    def test_2_4(self):
        self.assertEqual(Solution().binarySearchIterate([0,1,21,33,45,45,61,71,72,73,355],354),-1)

    def test_2_5(self):
        self.assertEqual(Solution().binarySearchIterate([0,1,21,33,45,45,61,71,72,73],70),-1)



    
if __name__=="__main__":
    unittest.main()