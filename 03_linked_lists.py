# link_list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            index = self.head
            prev_index = index
            while index:
                prev_index = index
                index = index.next
            prev_index.next = node

    def remove(self, value):
        if isinstance(self.is_exist(value), int):
            node = self.head
            if node.value == value:
                self.head = node.next
            else:
                while node:
                    node_next_value = node.next.value
                    if node_next_value == value:
                        node.next = node.next.next
                        return
                    node = node.next
        else:
            print(f'The number {value} is not exist')

    def clear(self):
        self.head = None

    def is_exist(self, value):
        node = self.head
        count = -1
        while node:
            count += 1
            if node.value == value:
                return count
            node = node.next
        return f'The number {value} is not exist'

    def to_array(self):
        node = self.head
        array = []
        while node:
            array.append(node.value)
            node = node.next
        return array

    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def swap(self, index1, index2):
        if index1 == index2:
            return
        node = self.head
        key1 = None
        while node:
            if node.value == index1:
                key1 = node
            node = node.next

        node = self.head
        key2 = None
        while node:
            if node.value == index2:
                key2 = node
            node = node.next
        if key1 and key2:
            key1.value, key2.value = key2.value, key1.value

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


# example_add_first


link_list_add_first = LinkedList()
link_list_add_first.add_first(5)
link_list_add_first.add_first(4)
link_list_add_first.add_first(3)

link_list_add_first.print()
print()
print(link_list_add_first.to_array())
print(link_list_add_first.length())
print()

# example_append

link_list_app = LinkedList()
link_list_app.append(5)
link_list_app.append(4)
link_list_app.append(3)

link_list_app.print()
print(link_list_app.to_array())
print(link_list_app.to_array())
link_list_app.swap(5, 4)
print()
print(link_list_app.to_array())
print(link_list_app.length())
link_list_app.remove(4)
link_list_app.remove(7)
print(link_list_app.length())
print(link_list_app.to_array())
link_list_app.clear()
print(link_list_app.length())
print(link_list_app.to_array())

