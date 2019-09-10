from BST_Create import Node
import unittest

t = Node(10)
t.insert(5)
t.insert(15)
t.insert(5)
t.insert(2)
t.insert(14)
t.insert(22)  
t.insert(12)  
t.insert(1)  


#print(t.inorderTraversal(t))  
a = [1, 2, 5, 5, 10, 12, 14, 15, 22]


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(t.inorderTraversal(t),a)

    def test2(self):
        self.assertEqual(t.contains(15),True)


if __name__=="__main__":
    unittest.main()