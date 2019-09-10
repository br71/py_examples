import FindClosestValue
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

test = BST(180).insert(8).insert(20).insert(3).insert(4).insert(7).insert(6).insert(2) \
    .insert(25).insert(88).insert(200).insert(65).insert(55).insert(98).insert(45).insert(-63)  \
        .insert(45).insert(20).insert(8).insert(-404).insert(57).insert(70).insert(23)


class TestProg(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(FindClosestValue.findClosestBst(test,75),70)
    
    def test_case2(self):
        self.assertEqual(FindClosestValue.findClosestBst(test,208),200)
    
if __name__=="__main__":
    unittest.main()

    

