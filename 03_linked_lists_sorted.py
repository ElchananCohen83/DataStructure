class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListsSorted:

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_into_sorted(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        elif node.value < self.head.value:
            self.head, node.next = node, self.head
        else:
            current = self.head
            while current.next and node.value > current.next.value:
                current = current.next
            node.next = current.next
            current.next = node
        self.length += 1

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        print('length linked lists:', self.length)


linked_sorted = LinkedListsSorted()
linked_sorted.insert_into_sorted(4)
linked_sorted.insert_into_sorted(1)
linked_sorted.insert_into_sorted(2)
linked_sorted.insert_into_sorted(8)
linked_sorted.insert_into_sorted(-8)
linked_sorted.insert_into_sorted(243)
linked_sorted.insert_into_sorted(770)
linked_sorted.insert_into_sorted(3.5)
linked_sorted.print()
