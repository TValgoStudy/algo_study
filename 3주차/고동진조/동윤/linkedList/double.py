class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DoubleLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0


    def length(self):
        return self.size


    def is_empty(self):
        if self.size:
            return False
        else:
            return True


    def selectNode(self, idx):
        if idx >= self.size or idx < 0:
            print('Overflow')
            return None
        elif idx <= self.size // 2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        elif idx > self.size // 2:
            target = self.tail
            for _ in range(self.size-idx-1):
                target = target.prev
            return target


    def appendleft(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            temp = self.head
            self.head = Node(item, next=temp)
            temp.prev = self.head
        self.size += 1

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            temp = self.tail
            self.tail = Node(item, prev=temp)
            temp.next = self.tail
        self.size += 1

    # def insert(self, item, idx):
    #     if self.is_empty():
    #         self.head = Node(item)
    #         self.tail = Node(None, self.head)
    #         self.head.next = self.tail
    #     else: # 끊고 재연결
    #         temp = self.selectNode(idx)


myLinkedList = DoubleLinkedList()
myLinkedList.append(3)
myLinkedList.append(8)
print(myLinkedList.selectNode(1).item)







