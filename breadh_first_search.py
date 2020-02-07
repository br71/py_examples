class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            currrent = queue.pop(0)
            array.append(currrent.name)
            for child in currrent.children:
                queue.append(child)

        return array    


t = Node("A")
t.addChild("B").addChild("C").addChild("D")
t.children[0].addChild("E")

print (t.breadthFirstSearch([]))

#         A
#       / | \
#      B  C  D
#     /
#    E  
          
#########################################################

#         A
#       / | \
#      B  C  D
#     /\     /\
#    E  F    G H
#       /\   \
#       I J   K
          