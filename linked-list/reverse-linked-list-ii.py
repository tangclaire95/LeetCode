# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode (next=head)
        p0=dummy 
        for _ in range(left-1):
            p0=p0.next
        
        pre= None
        cur=p0.next
        for _ in range(right-left+1):
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        p0.next.next=cur
        p0.next=pre
        return dummy.next
# time o(n), space o(1)

