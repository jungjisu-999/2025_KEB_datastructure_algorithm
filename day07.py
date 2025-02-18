import random
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
@@ -37,9 +41,11 @@ def __str__(self):

if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    print(l)
    print(l.search(999))
    print(l.search(-11))
    i = 0
    while i < 20:
        n = random.randint(1, 20)
        l.append(n)
        print(n, end=' ')
        i = i + 1
    #print(l)
    print(l.search(10))