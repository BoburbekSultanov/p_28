class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def find(self, val):
        result = 1
        tmp = self.head.next
        while tmp:
            if tmp.val == val:
                print(result)
                break
            tmp = tmp.next
            result += 1
        else:
            print(-1)

    def insert(self, new_val, pos):
        tmp = self.head
        next_pos = 1
        while tmp.next:
            if next_pos == pos:
                new_node = Node(new_val)
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next
            next_pos += 1
        else:
            tmp.next = Node(new_val)

    # def delete(self, new_val):
    #     tmp = self.head
    #     while tmp.next.next:
    #         if tmp.next.val == new_val:
    #             tmp.next = tmp.next.next
    #             break
    #         tmp = tmp.next
    #     else:
    #         if tmp.next.val == new_val:
    #             tmp.next = None

    def delete(self , val):
        tmp = self.head
        while tmp.next.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
        else:
            if tmp.next.val == val:
                tmp.next = None
    def append(self, new_val):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(new_val)

    def print(self):
        tmp = self.head.next
        while tmp.next:
            print(tmp.val, end=' ')
            tmp = tmp.next


l = [4, 2, 36, 3, 4, 5, 6, 7, 89, 9]
linkedlist = LinkedList()
for i in l:
    linkedlist.append(i)

linkedlist.find(70)
linkedlist.print()
