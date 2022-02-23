class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def concat(self, nodes):
        self.next = nodes

n1 = Node(5)
n1.next = Node(6)
n1.next.next = Node(7)  # 5 -> 6 -> 7 -> None

head = Node(4) # 4 -> None
head.concat(n1) # 4 -> 5 -> 6 -> 7 -> None