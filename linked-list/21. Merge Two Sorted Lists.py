# type:ignore

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = ListNode()
        node = head
        while curr1 and curr2:
            if curr1.val > curr2.val:
                node.next = curr2
                curr2 = curr2.next
            else:
                node.next = curr1
                curr1 = curr1.next
            node = node.next
        
        if curr1:
            node.next = curr1
        
        if curr2:
            node.next = curr2

        return head.next