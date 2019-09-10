class Node:

    def __init__(self, name):
        # Init Node objects with name (it is first node name)
        # Children array initialized to add Nodes
        self.children = []
        self.name = name

    def addChild(self, name):

        # Add children nodes (Node objects) in children array
        # Because that B starts from index 0 in children array
        # test1.addChild("B").addChild("C").addChild("D")

        self.children.append(Node(name))

        # To stack funcion calls: test1.addChild("B").addChild("C").addChild("D")
        return self

    # O( v + e) - space, O(v) - space
    def deptFirstSearch(self,array):
        # Outside of recursion (at start array is empty -> addaed in function argument)
        # Add first value, in this case it is "A" ->  DeptFirstSearch.Node("A")

        # After that "B" starts from index 1 -> recursion part

        # In this case we are woking with nested lists.
        # test1.children[0].children[1].addChild("I").addChild("J") 

        array.append(self.name)
        for child in self.children:
            # Recursion call
            child.deptFirstSearch(array)
            print(array)
        return array
    