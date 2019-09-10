class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def sethead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertbefore(self.head, node)

    def settail(self, node):
        if self.tail is None:
            self.sethead(node)
            return
        self.insertafter(self.tail, node)

    # O(1) time | O(1) space
    def insertbefore(self, node, nodetoinsert):
        if nodetoinsert == self.head and nodetoinsert == self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.prev = node.prev
        nodetoinsert.next = node
        if node.prev is None:
            self.head = nodetoinsert
        else:
            node.prev.next = nodetoinsert
        node.prev = nodetoinsert

    # O(1) time | O(1) space
    def insertafter(self, node, nodetoinsert):
        if nodetoinsert == self.head and nodetoinsert == self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.prev = node
        nodetoinsert.next = node.next
        if node.next is None:
            self.tail = nodetoinsert
        else:
            node.next.prev = nodetoinsert
        node.next = nodetoinsert

    # O(p) time | O(1) space | (p = position)
    def insertatposition(self, position, nodetoinsert):
        if position == 1:
            self.sethead(nodetoinsert)
            return
        node = self.head
        currentposition = 1
        while node is not None and currentposition != position:
            node = node.next
            currentposition += 1
        if node is not None:
            self.insertafter(node,nodetoinsert)
        else:
            self.settail()

    # O(n) time | O(1) space
    def removenodewithvalue(self, value):
        node = self.head
        while node is not None:
            nodetoremove = node
            node = node.next
            if nodetoremove.value == value:
                self.remove(nodetoremove)

#    O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removenodebindings(node)

    # O(n) time | O(1) space
    def containsnodevalue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    # O(1) time | O(1) space
    @staticmethod
    def removenodebindings(node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def get_node_values_head_to_tail(linkedlist):
    values = []
    node = linkedlist.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def get_node_values_tail_to_head(linkedlist):
    values = []
    node = linkedlist.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def remove_nodes(linkedlist, nodes):
    for node in nodes:
        linkedlist.remove(node)




















