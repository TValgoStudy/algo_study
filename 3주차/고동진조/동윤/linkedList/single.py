class Node:
    # 1 > 1 > 1 > 1>
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


    def push_first(self, node):
        node.next = self.head
        # 노드 인스턴스를 바로 head로 지정합니다.
        self.head = node
        self.count += 1

    def push_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.count += 1

    # 헤드를 헤드 다음 원소로 변경
    def popleft(self):
        tmp = self.head
        self.head = self.head.next
        return tmp.data if tmp else None

    def pop_after(self, prev_node):
        tmp = prev_node.next
        if tmp:
            prev_node.next = tmp.next
            return tmp.data
        else:
            return None

    def length(self):
        return self.count

    def __str__(self):
        node = self.head
        val = ''
        while node:
            val += str(node.data)
            if node.next:
                val += ' -> '
            node = node.next
        return val


my_first_linked_list = linked_list()
node1 = Node(1)
node2 = Node(2)
node3 = Node([0])
node4 = Node([1])
my_first_linked_list.push_first(node1)
my_first_linked_list.push_first(node2)
my_first_linked_list.push_first(node3)
my_first_linked_list.push_after(node3, node4)
my_first_linked_list.pop_after(node2)
print(my_first_linked_list.popleft())
print(my_first_linked_list)
print(my_first_linked_list.length())



