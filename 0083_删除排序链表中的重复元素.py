# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if  not head:return None
        pre=ListNode(0)
        p=ListNode(0)
        pre=head
        p=head.next
        while p:
            if p.val==pre.val:
                pre.next=p.next
            else:
                pre=p
            p=p.next
        return head
