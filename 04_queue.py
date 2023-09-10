# queue
class Node:
    def __init__(self, value):
        self.value = value
        self.ext = None


class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        node = self.head
        node_prev = None
        if node.next is None:
            self.head = None
            return node.value
        else:
            while node.next:
                node_prev = node
                node = node.next
            value = node.value
            node_prev.next = None
            return value

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.print()
print()

print(queue.pop())
print(queue.pop())
# print(stack.pop())

print()
queue.print()

print(queue.is_empty())
