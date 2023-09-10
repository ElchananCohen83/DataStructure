# stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if self.head:
            node = self.head
            value = node.value
            self.head = node.next
            self.length -= 1
            return value
        else:
            return None

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


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
print(stack.length,88)

print(stack.pop())
print(stack.pop())
print(stack.length,88)
# print(stack.pop())

print()
stack.print()

print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())

print(stack.pop())

print()