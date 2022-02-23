class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = LLNode(value)
        else: 
            cursor = self.head

            while cursor.next != None:
                cursor = cursor.next
            
            cursor.next = LLNode(value)

    def pop(self):
        prev = None
        cursor = self.head
        while cursor.next != None:
            prev = cursor
            cursor = cursor.next
        
        pop_up_value = cursor.value
        if prev != None:
            prev.next = None      
        return pop_up_value

    def __str__(self):
        buf = []
        cursor = self.head
        if cursor == None:
            return 'Empty()'

        buf.append(f"{cursor.value}")

        while cursor.next != None:
            cursor = cursor.next
            buf.append(f"{cursor.value}")
        
        return ' -> '.join(buf)

    def __len__(self):
        cursor = self.head
        if cursor == None:
            return 0

        size = 1
        while cursor.next != None:
            size += 1
            cursor = cursor.next
        return size

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTree:
    # 값이 크면 오른쪽에
    # 값이 작으면 왼쪽에
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            # 최초면
            self.root = Node(value)
        else:
            # 최초가 아니면
            cursor = self.root
            
            while True:
                if value < cursor.value and cursor.left != None:
                    cursor = cursor.left
                elif value >= cursor.value and cursor.right != None:
                    cursor = cursor.right
                else:
                    break

            if value < cursor.value:
                cursor.left = Node(value)
            elif value >= cursor.value:
                cursor.right = Node(value)
            else:
                print("Unexpected result")

    def find(self, target):
        cursor = self.root

        while True:
            if cursor == None:
                return False

            if cursor.value == target:
                return True
            elif target < cursor.value:
                cursor = cursor.left
            else:
                cursor = cursor.right

    def path(self, target):
        path = LinkedList()
        cursor = self.root

        while True:
            if cursor == None:
                return LinkedList()

            if cursor.value == target:
                path.push(LLNode(f"Found({cursor.value})"))
                return path
            elif target < cursor.value:
                path.push(LLNode(f"Left({cursor.value})"))
                cursor = cursor.left
            else:
                path.push(LLNode(f"Right({cursor.value})"))
                cursor = cursor.right

    def __len__(self):
        pass

    def __contains__(self, target):
        return self.find(target)

    def dfs(self):
        # depth-first search
        # STACK STACK->RECURSIVE
        pass

    def bfs(self):
        # breadth-first search
        # QUEUE
        pass


if __name__ == '__main__':
    tree = BSTree()
    tree.insert(3)    
    tree.insert(5)    
    tree.insert(11)    
    tree.insert(1)    
    tree.insert(2)    
    tree.insert(6)    

    print(tree.find(9)) # False
    print(tree.find(11)) # True

    print(tree.path(9))
    print(tree.path(11))

    if 11 in tree:
        print('11 found')
    else:
        print('not found')
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, value):
#         pass

#     def pop(self):
#         pass

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
