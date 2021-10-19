# https://realpython.com/linked-lists-python/
# Node를 따로 구현할 생각을 못하고 linked_list에 class attribute로 생성하려고 함
# 문제점: 별개의 Linked list를 구현 못한다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# Head를 class attribute로 관리 X 하나의 instance가 하나의 linkedlist이다.
# class 생성 시 repr을 어떻게 할지 고민해봐야할 요소이다.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # data만 받고 자동으로 노드 추가
    # def add_first(self, data):
    #     temp = Node(data)
    #     temp.next, self.head = self.head, temp

    # node를 parameter로 설정
    def add_first(self, node):
        self.len += 1
        node.next = self.head
        self.head = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # __iter__ 를 통해서 self(instance가 반복시 무엇을 반환할지 정해주어야 가능한 표현이다.)
    # 밑의 과정을 iter와 분할해서 기능을 구현했다.
    def add_last(self, node):
        self.len += 1
        if self.head is None:
            self.head = node
            return
        for current_node in self: # self == instance
            pass
        current_node.next = node

        # current_node == self.tail
        # current_node.next = new_node
        # self.tail = new_node
        # new_node.prev = current_node
# a = SinglyLinkedList()
# for node in a: # a == self == instance
#     pass
# node == 마지막 노드 == next == none


    # while condition 검사 불필요, last_node 에 할당하는 과정은 동일함
    # def add_last(self, node):
    #     self.len += 1
    #     last_node = self.head
    #     while last_node.next is None:
    #         last_node = last_node.next
    #     last_node.next = node

    def add_after(self, target_node_data, new_node):
        # 기존 리스트가 비어있으면 오류를 발생시켜야 한다.
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                self.len += 1
                return

        raise Exception('Node with data {0} not found'.format(target_node_data))

        # node = self.head
        # 매번 None 인지 확인하는 과정 들어감 + new node 뒤에 연결하느 과정 빼먹음 + 끝까지 뒤져도 없는 경우 생각 안함
        # while node is not None:
        #     if node.data == target_node_data:
        #         break
        #     node = node.next
        # node.next = new_node

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        # 다른 종류의 검사임으로 if로 분기
        if self.head == target_node_data:
            self.add_first(new_node)
            # new_node.next = self.head
            # self.head = new_node

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                # call by reference라서 저장하는 순서는 상관 없다.
                new_node.next = node
                prev_node.next = new_node
                self.len += 1
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        # 다른 정류의 개념을 체크하는 것이므로 elif 말고 if를 사용한다.
        if self.head.data == target_node_data:
            # 틀린 과정 len 도 + - 되서 반영안됨
            # self.add_first(self.head.next)
            self.head = self.head.next
            self.len -= 1
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                pass

    def length(self):
        return self.len

