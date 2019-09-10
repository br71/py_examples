class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # O(Log(n)) - time | O(1) space
    def insert(self, data):
        
        currentNode = self

        while True:
            if data < currentNode.data:
                if currentNode.left is None:
                    currentNode.left = Node(data)
                    break
                else:
                    currentNode = currentNode.left

            else:
                if currentNode.right == None:
                    currentNode.right = Node(data)
                    break
                else:
                    currentNode = currentNode.right

        #return self

    # O(Log(n))  time | O(log(n)) space
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


    # O(Log(n))  time | O(log(n)) space
    def contains(self,data):
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(data)

        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.contains(data)

        else:
            return True

            

