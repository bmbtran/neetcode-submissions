# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        # while both:
        # dummy -> 1 (head list1 become list1.next) -> 1 
        # if l1:
        #     connect to l1
        # if l2: 
        #     connect to l2
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return dummy.next