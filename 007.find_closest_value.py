# O(Log(n)) time , O(Log(n)) space - awerage
# O(n) time , O(n) space - worst

def findClosestBst(tree,target):
    return findClosestBstUtil(tree, target, float("inf"))

def findClosestBstUtil(tree, target, closest):

    if tree is None:
        return closest

    if abs(target - closest) > abs (target - tree.value):
        closest = tree.value
    
    if target < tree.value:
        return findClosestBstUtil(tree.left, target, closest)

    elif target > tree.value:
        return findClosestBstUtil(tree.right, target, closest)
    else:
        return closest



