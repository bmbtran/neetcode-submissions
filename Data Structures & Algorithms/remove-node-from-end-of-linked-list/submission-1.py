# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        prev, cur = None, head
        firstPassNode = head
        countNodes = 0
        #first pass is count num of nodes
        while firstPassNode:
            countNodes +=1
            firstPassNode = firstPassNode.next
        targetI = countNodes - n
        if targetI == 0:
            return cur.next
        curI = 0
        while cur.next and curI != targetI:
            prev, cur = cur, cur.next
            curI +=1
        prev.next = cur.next
        return head

