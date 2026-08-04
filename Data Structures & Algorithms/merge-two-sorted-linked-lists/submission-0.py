# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp = ListNode(-1)
        ans = temp
        i = list1
        j = list2
        while i is not None and j is not None:
            if i.val < j.val:
                temp.next = i
                temp = temp.next
                i = i.next
            else:
                temp.next = j
                temp = temp.next
                j = j.next
        while i is not None:
            temp.next = i
            temp = temp.next
            i = i.next
        while j is not None:
            temp.next = j
            temp = temp.next
            j = j.next
        return ans.next
