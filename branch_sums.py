# Write a function that takes binary tree and returns
# list of branch sums (orter from left to right)
# This is recurse solution


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left= None
        self.right = None

tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)

tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)

tree.left.right.right = BinaryTree(10)


# O(n) time, O(n) space
def branchSums(root):
    sums = []
    calculateBranchSums(tree, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    
    # Node that hase one child node
    if node is None:
        return
    
    # Adding node values
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

# Driver code
print(branchSums(tree))


#         1
#        / \
#        2  3
#       /\  /\
#      4  5 6 7
#     / \  \
#    8   9  10
#
#Solution: [15,16,18,10,11]
