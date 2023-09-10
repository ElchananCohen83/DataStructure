class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def is_balanced_brackets(expr):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if top_char != brackets_map[char]:
                return False

    return stack.is_empty()


# Test cases
test_cases = ["{[(כולכטולר)]}",
              "{[(])}",
              "{{[[(())]]}}",
              "([{}])",
              "{[עלו}]"]

for expression in test_cases:
    result = is_balanced_brackets(expression)
    print(f"{expression} is {'balanced' if result else 'not balanced'}.")
