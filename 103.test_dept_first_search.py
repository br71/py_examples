import DeptFirstSearch
import unittest

test1 = DeptFirstSearch.Node("A")
test1.addChild("B").addChild("C").addChild("D")
test1.children[0].addChild("E").addChild("F")
test1.children[2].addChild("G").addChild("H")
test1.children[0].children[1].addChild("I").addChild("J")
test1.children[2].children[0].addChild("K")


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(test1.deptFirstSearch([]), ["A","B","E","F","I","J","C","D","G","K","H"])


if __name__ == "__main__":
    unittest.main()


 #          A
 #         /|\
 #        B C D
 #       /\   /\
 #      E  F  G H
 #        /\  \
 #        I J  K

 


