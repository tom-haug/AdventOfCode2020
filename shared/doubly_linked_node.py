from typing import Generic, TypeVar

T = TypeVar('T')


class DoublyLinkedNode(Generic[T]):
    def __init__(self, data: T = None):
        self.data = data
        self.next = self
        self.prev = self

    def remove_self(self):
        prev_node = self.prev
        next_node = self.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return self

    def append(self, new_node: "Node[T]"):
        cur_next_node = self.next
        self.next = new_node
        new_node.prev = self
        new_node.next = cur_next_node
        cur_next_node.prev = new_node

    def min_connected_node(self):
        cur_min = self
        test_node = cur_min.next
        while test_node != self:
            if test_node.data < cur_min.data:
                cur_min = test_node
            test_node = test_node.next
        return cur_min

    def max_connected_node(self):
        cur_max = self
        test_node = cur_max.next
        while test_node != self:
            if test_node.data > cur_max.data:
                cur_max = test_node
            test_node = test_node.next
        return cur_max

    def get_connected_node(self, search_data):
        cur_node = self
        while cur_node.data != search_data:
            cur_node = cur_node.next
        return cur_node
