import LinkedListContruct
import unittest


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


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedlist = LinkedListContruct.DoubleLinkedList()
        first = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(4)
        fifth = Node(4)
        sixth = Node(6)
        seventh = Node(7)
        linkedlist.sethead(first)
        linkedlist.insertafter(first, second)
        linkedlist.insertafter(second, third)
        linkedlist.insertafter(third, fourth)
        linkedlist.insertafter(fourth, fifth)
        linkedlist.insertafter(fifth, sixth)
        linkedlist.insertafter(sixth, seventh)
        self.assertEqual(get_node_values_head_to_tail(linkedlist), [1, 2, 3, 4, 4, 6, 7])
        self.assertEqual(get_node_values_tail_to_head(linkedlist), [7, 6, 4, 4, 3, 2, 1])

        linkedlist.remove(second)
        self.assertEqual(get_node_values_head_to_tail(linkedlist),  [1, 3, 4, 4, 6, 7])
        self.assertEqual(get_node_values_tail_to_head(linkedlist), [7, 6, 4, 4, 3, 1])

        linkedlist.removenodewithvalue(7)
        self.assertEqual(get_node_values_head_to_tail(linkedlist), [1, 3, 4, 4, 6])
        self.assertEqual(get_node_values_tail_to_head(linkedlist), [6, 4, 4, 3, 1])


if __name__ == '__main__':
    unittest.main()