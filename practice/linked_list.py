class Value:
    def __init__(self, value, type):
        self.value = value
        self.type = type

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else: 
            cursor = self.head

            while cursor.next != None:
                cursor = cursor.next
            
            cursor.next = Node(value)

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

    def concat(self, other):
        pass

    def sort(self):
        pass

    def __str__(self):
        buf = []
        cursor = self.head
        if cursor == None:
            return ''

        buf.append(f"{cursor.value}")

        while cursor.next != None:
            cursor = cursor.next
            buf.append(f"{cursor.value}")
        
        return ' -> '.join(buf)

    def __len__(self): 
        cursor = self.head
        counter = 0
        if cursor != None:
            counter += 1
        while cursor.next != None:
            cursor = cursor.next
            counter += 1
        return counter

x = LinkedList()

x.push(1) 
x.push(2) 
x.push(3)

y = LinkedList()

y.push(2)
y.push(3)
y.push(5)

x.concat(y)
len(x) == 6
print(x) # 1 -> 2 -> 3 -> 2 -> 3 -> 5

x.sort()
print(x) # 1 -> 2 -> 2 -> 3 -> 3 -> 5


def calc(expr):
    pass

expr = LinkedList() # Stack, Queue
expr.push(Value(5, 'NUMBER'))
expr.push(Value('+', 'PLUS'))
expr.push(Value(3, 'NUMBER'))
expr.push(Value('*', 'MUL'))
expr.push(Value(2, 'NUMBER'))
answer = calc(expr)
print(answer)

# 트리
# 주소록 (파일 입출력)
# 숫자야구 게임
# 사칙연산 계산기
# 훌라 카드 게임
# 장기