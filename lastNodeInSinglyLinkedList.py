import unittest


def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list

    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: %s' % k
        )

    # Step 1: get the length of the list
    # Start at 1, not 0
    # else we'd fail to count the head node!
    list_length = 1
    current_node = head

    # Traverse the whole list,
    # counting all the nodes
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    # If k is greater than the length of the list, there can't
    # be a kth-to-last node, so we'll return an error!
    if k > list_length:
        raise ValueError(
            'k is larger than the length of the linked list: %s' % k
        )

    # Step 2: walk to the target node
    # Calculate how far to go, from the head,
    # to get to the kth to last node
    how_far_to_go = list_length - k
    current_node = head
    for i in range(how_far_to_go):
        current_node = current_node.next

    return current_node
    

# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)