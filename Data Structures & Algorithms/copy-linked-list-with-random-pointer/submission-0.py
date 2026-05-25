class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        prev = None
        res = None
        nodeMap = {}

        # -------- First pass: copy nodes & next pointers --------
        while curr:
            newNode = Node(curr.val)
            nodeMap[curr] = newNode

            if prev is None:
                res = newNode
            else:
                prev.next = newNode   # ✅ FIXED HERE

            prev = newNode
            curr = curr.next

        # -------- Second pass: copy random pointers --------
        curr = head
        temp = res

        while curr:
            temp.random = nodeMap.get(curr.random)
            temp = temp.next
            curr = curr.next

        return res
