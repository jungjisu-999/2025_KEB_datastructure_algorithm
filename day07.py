class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:  # if next node exist
            current = current.next  # move
        current.next = Node(data)
    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"
from collections import deque

d = deque()
d.append(7)
d.append(-11)
d.append(8)

if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    print(l)
    for data in d:
        print(data)