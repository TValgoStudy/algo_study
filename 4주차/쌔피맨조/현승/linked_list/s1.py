class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
head = ListNode(list1[0])
node = head
for i in range(1, len(list1)):
    node.next = ListNode(list1[i])
    node = node.next

node = head
while node.next != None:
    print(node.val, end=' ')
    node = node.next
print('마지막 노드: ', node.val)
