import DeptFirstSearchIterate
import unittest

vertices = {1: [2, 3], 2: [4, 5], 3: [5], 4: [6], 5: [6], 6: [7], 7: []}

test = DeptFirstSearchIterate.dfs_iterative(vertices, 1)


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(test, [1, 3, 5, 6, 7, 2, 4])


if __name__ == "__main__":
    print(test)
    unittest.main()
    

# Path is 1 -> 3 -> 5 because stack (LIFO), 3 last enters and because that first pop out
# [1, 3, 5, 6, 7, 2, 4]

#     1
#    / \
#   2   3
#   | \ |
#   4   5
#   |  /
#    6 -- 7